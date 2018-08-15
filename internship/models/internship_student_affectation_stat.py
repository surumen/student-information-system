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
from django.db import models
from osis_common.models.serializable_model import SerializableModel, SerializableModelAdmin


class InternshipStudentAffectationStatAdmin(SerializableModelAdmin):
    list_display = ('student', 'organization', 'speciality', 'period', 'choice', 'cost', 'consecutive_month',
                    'type_of_internship')
    fieldsets = ((None, {'fields': ('student', 'organization', 'speciality', 'period', 'choice', 'cost',
                                    'consecutive_month', 'type_of_internship')}),)
    raw_id_fields = ('student', 'organization', 'speciality', 'period')
    search_fields = ['student__first_name', 'student__last_name']
    list_filter = ('period', 'choice')


class InternshipStudentAffectationStat(SerializableModel):
    student = models.ForeignKey('base.Student')
    organization = models.ForeignKey('internship.Organization')
    speciality = models.ForeignKey('internship.InternshipSpeciality')
    period = models.ForeignKey('internship.Period')
    choice = models.CharField(max_length=1, blank=False, null=False, default='0')
    cost = models.IntegerField(blank=False, null=False)
    consecutive_month = models.BooleanField(default=False, null=False)
    type_of_internship = models.CharField(max_length=1, blank=False, null=False, default='N')

    def __str__(self):
        return u"%s : %s - %s (%s)" % (self.student, self.organization, self.speciality, self.period)


def search(**kwargs):
    kwargs = {k: v for k, v in kwargs.items() if v}
    return InternshipStudentAffectationStat.objects.filter(**kwargs)\
        .select_related("student__person", "organization", "speciality", "period")\
        .order_by("student__person__last_name", "student__person__first_name", "period__date_start")


def find_by_id(affectation_id):
    return InternshipStudentAffectationStat.objects.get(pk=affectation_id)


def find_non_mandatory_affectations(period_ids):
    return InternshipStudentAffectationStat.objects.filter(period__id__in=period_ids).\
        select_related("student", "organization", "speciality")

def find_affectations(period_ids):
    return InternshipStudentAffectationStat.objects.filter(period__id__in=period_ids).\
        select_related("student", "organization", "speciality")
