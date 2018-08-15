##############################################################################
#
#    OSIS stands for Open Student Information System. It's an application
#    designed to manage the core business of higher education institutions,
#    such as universities, faculties, institutes and professional schools.
#    The core business involves the administration of students, teachers,
#    courses, programs and so on.
#
#    Copyright (C) 2015-2017 Université catholique de Louvain (http://www.uclouvain.be)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    A copy of this license - GNU General Public License - is available
#    at the root of the source code of this program.  If not,
#    see http://www.gnu.org/licenses/.
#
##############################################################################
import datetime

from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import Q
from django.utils import timezone

from base.models.enums import entity_type
from base.models.enums.organization_type import MAIN
from osis_common.utils.datetime import get_tzinfo


class EntityVersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'entity', 'acronym', 'parent', 'title', 'entity_type', 'start_date', 'end_date',)
    search_fields = ['entity__id', 'entity__external_id', 'title', 'acronym', 'entity_type', 'start_date', 'end_date']
    raw_id_fields = ('entity', 'parent')
    readonly_fields = ('find_direct_children', 'count_direct_children', 'find_descendants', 'get_parent_version')


class EntityVersion(models.Model):
    external_id = models.CharField(max_length=100, blank=True, null=True)
    changed = models.DateTimeField(null=True, auto_now=True)
    entity = models.ForeignKey('Entity')
    title = models.CharField(db_index=True, max_length=255)
    acronym = models.CharField(db_index=True, max_length=20)
    entity_type = models.CharField(choices=entity_type.ENTITY_TYPES, max_length=50, db_index=True, blank=True, null=True)
    parent = models.ForeignKey('Entity', related_name='parent_of', blank=True, null=True)
    start_date = models.DateField(db_index=True)
    end_date = models.DateField(db_index=True, blank=True, null=True)

    def __str__(self):
        return "{} ({} - {} - {} to {})".format(
            self.acronym,
            self.title,
            self.entity_type,
            self.start_date,
            self.end_date
        )

    def save(self, *args, **kwargs):
        if self.can_save_entity_version():
            super(EntityVersion, self).save()
        else:
            raise AttributeError('EntityVersion invalid parameters')

    def exists_now(self):
        now = datetime.datetime.now().date()
        return (not self.end_date) or (self.end_date and self.start_date < now < self.end_date)

    def can_save_entity_version(self):
        return self.count_entity_versions_same_entity_overlapping_dates() == 0 and \
               self.count_entity_versions_same_acronym_overlapping_dates() == 0 and \
               self.parent != self.entity

    def search_entity_versions_with_overlapping_dates(self):
        if self.end_date:
            qs = EntityVersion.objects.filter(
                    Q(start_date__range=(self.start_date, self.end_date)) |
                    Q(end_date__range=(self.start_date, self.end_date)) |
                    (
                        Q(start_date__lte=self.start_date) & Q(end_date__gte=self.end_date)
                    )
                )
        else:
            qs = EntityVersion.objects.filter(
                    end_date__gte=self.start_date
                )

        return qs.exclude(id=self.id)

    def count_entity_versions_same_entity_overlapping_dates(self):
        return self.search_entity_versions_with_overlapping_dates().filter(entity=self.entity).count()

    def count_entity_versions_same_acronym_overlapping_dates(self):
        return self.search_entity_versions_with_overlapping_dates().filter(acronym=self.acronym).count()

    def _direct_children(self, date):
        if date is None:
            date = timezone.now().date()

        if self._contains_given_date(date):
            return EntityVersion.objects.filter(parent=self.entity, start_date__lte=date)\
                                            .filter(Q(end_date__gte=date) | Q(end_date__isnull=True))
        else:
            return None

    def find_direct_children(self, date=None):
        direct_children = self._direct_children(date)
        return list(direct_children) if direct_children else []

    def count_direct_children(self, date=None):
        direct_children = self._direct_children(date)
        return direct_children.count() if direct_children else 0

    def find_descendants(self, date=None):
        descendants = []
        if self.count_direct_children(date) > 0:
            direct_children = self.find_direct_children(date)
            descendants.extend(direct_children)
            for child in direct_children:
                descendants.extend(child.find_descendants(date))

        return sorted(descendants, key=lambda an_entity: an_entity.acronym)

    def get_parent_version(self, date=None):
        if date is None:
            date = timezone.now().date()

        if self._contains_given_date(date):
            qs = EntityVersion.objects.filter(entity=self.parent, start_date__lte=date) \
                                      .filter(Q(end_date__gte=date) | Q(end_date__isnull=True))
            try:
                return qs.get()
            except ObjectDoesNotExist:
                return None
        else:
            return None

    def _contains_given_date(self, date):
        if self.start_date and self.end_date:
            return self.start_date <= date <= self.end_date
        elif self.start_date and not self.end_date:
            return self.start_date <= date
        else:
            return False

    def get_organogram_data(self, level):
        level += 1
        if level < 3:
            return {
                'id': self.id,
                'acronym': self.acronym,
                'children': [child.get_organogram_data(level) for child in self.find_direct_children()]
            }
        else:
            return {
                'id': self.id,
                'acronym': self.acronym,
                'children': []
            }


def find(acronym, date=None):
    if date is None:
        date = timezone.now()
    try:
        entity_version = EntityVersion.objects.get(acronym=acronym,
                                                   start_date__lte=date,
                                                   end_date__gte=date
                                                   )
    except ObjectDoesNotExist:
        return None

    return entity_version


def find_latest_version(date):
    return EntityVersion.objects.filter(Q(end_date__gte=date) | Q(end_date__isnull=True),
                                        start_date__lte=date)\
                                .order_by('-start_date')


def get_last_version(entity, date=None):
    qs = EntityVersion.objects.filter(entity=entity)

    if date:
        qs = qs.filter(Q(end_date__gte=date) | Q(end_date__isnull=True),
                       start_date__lte=date)

    return qs.latest('start_date')
    # find_latest_version(academic_year.current_academic_year().start_date).get(entity=entity)


def get_by_entity_and_date(entity, date):
    if date is None:
        date = timezone.now()
    try:
        entity_version = EntityVersion.objects.filter(Q(end_date__gte=date) | Q(end_date__isnull=True),
                                                      entity=entity, start_date__lte=date)
    except ObjectDoesNotExist:
        return None
    return entity_version


def search(**kwargs):
    queryset = EntityVersion.objects

    if 'entity' in kwargs:
        queryset = queryset.filter(entity__exact=kwargs['entity'])

    if 'title' in kwargs:
        queryset = queryset.filter(title__exact=kwargs['title'])

    if 'acronym' in kwargs:
        queryset = queryset.filter(acronym__exact=kwargs['acronym'])

    if 'entity_type' in kwargs:
        queryset = queryset.filter(entity_type__exact=kwargs['entity_type'])

    if 'start_date' in kwargs:
            queryset = queryset.filter(start_date__exact=kwargs['start_date'])

    if 'end_date' in kwargs:
            queryset = queryset.filter(end_date__exact=kwargs['end_date'])

    return queryset.select_related('parent')


def count(**kwargs):
    return search(**kwargs).count()


def search_entities(acronym=None, title=None, type=None):
    queryset = EntityVersion.objects
    if acronym:
        queryset = queryset.filter(acronym__iexact=acronym)
    if title:
        queryset = queryset.filter(title__icontains=title)
    if type:
        queryset = queryset.filter(entity_type=type)
    return queryset


def find_by_id(entity_version_id):
    return EntityVersion.objects.get(pk=entity_version_id)


def count_identical_versions(same_entity, version):
    return count(entity=same_entity,
                 title=version.get('title'),
                 acronym=version.get('acronym'),
                 entity_type=version.get('entity_type'),
                 parent=version.get('parent'),
                 start_date=version.get('start_date'),
                 end_date=version.get('end_date')
                 )


def find_update_candidates_versions(entity, version):
    to_update_versions = search(entity=entity,
                                title=version.get('title'),
                                acronym=version.get('acronym'),
                                entity_type=version.get('entity_type'),
                                parent=version.get('parent'),
                                start_date=version.get('start_date')
                                )
    return [v for v in to_update_versions if not _match_dates(v.end_date, version.get('end_date'))]


def _match_dates(osis_date, esb_date):
    if osis_date is None:
        return esb_date is None
    else:
        return osis_date.strftime('%Y-%m-%d') == esb_date


def find_main_entities_version():
    entities_version = find_latest_version(date=datetime.datetime.now(get_tzinfo()))\
        .filter(entity_type__in=[entity_type.SECTOR, entity_type.FACULTY, entity_type.SCHOOL,
                                 entity_type.INSTITUTE, entity_type.DOCTORAL_COMMISSION],
                entity__organization__type=MAIN).order_by('acronym')
    return entities_version


def find_first_latest_version_by_period(ent,start_date, end_date):
    return EntityVersion.objects.filter(Q(end_date__lte=end_date) | Q(end_date__isnull=True),
                                        start_date__gte=start_date, entity=ent) \
        .order_by('-start_date').first()


def find_parent_faculty_version(child_entity_ver, academic_yr):
    if child_entity_ver:
        if child_entity_ver.parent is None:
            return None
        else:
            entity_parent_version = find_latest_version_by_entity(child_entity_ver.parent,
                                                                  academic_yr.start_date)
            if entity_parent_version is None:
                return None
            else:
                if entity_parent_version.entity_type == entity_type.FACULTY:
                    return entity_parent_version
                else:
                    return find_parent_faculty_version(entity_parent_version, academic_yr)
    return None


def find_latest_version_by_entity(ent,date):
    return EntityVersion.objects.filter(Q(end_date__gte=date) | Q(end_date__isnull=True),
                                        start_date__lte=date, entity=ent).select_related('entity',
                                                                                         'parent') \
        .first()
