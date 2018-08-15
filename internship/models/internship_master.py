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
from django.utils.translation import ugettext_lazy as _

from osis_common.models.serializable_model import (SerializableModel,
                                                   SerializableModelAdmin)


class InternshipMasterAdmin(SerializableModelAdmin):
    list_display = ('reference', 'organization', 'first_name', 'last_name', 'civility', 'type_mastery', 'speciality')
    fieldsets = ((None, {'fields': ('reference', 'organization', 'first_name', 'last_name', 'civility', 'type_mastery',
                                    'speciality')}),)
    raw_id_fields = ('organization',)


class InternshipMaster(SerializableModel):
    CIVILITY_CHOICE = (('PROFESSOR', _('Professor')),
                       ('DOCTOR', _('Doctor')))
    TYPE_CHOICE = (('SPECIALIST', _('Specialist')),
                   ('GENERALIST', _('Generalist')))
    SPECIALITY_CHOICE = (('INTERNAL_MEDICINE', _('Internal Medicine')),
                         ('SURGERY', _('Surgery')),
                         ('GYNEC_OBSTETRICS', _('Gynec-Obstetrics')),
                         ('PEDIATRICS', _('Pediatrics')),
                         ('EMERGENCY', _('Emergency')),
                         ('GERIATRICS', _('Geriatrics')))

    organization = models.ForeignKey('internship.Organization', null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True, db_index=True)
    last_name = models.CharField(max_length=50, blank=True, null=True, db_index=True)
    reference = models.CharField(max_length=50, blank=True, null=True)
    civility = models.CharField(max_length=50, blank=True, null=True)
    type_mastery = models.CharField(max_length=50, blank=True, null=True)
    speciality = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return u"%s" % self.reference


def find_masters():
    return InternshipMaster.objects.all().select_related("organization")


def search(**kwargs):
    kwargs = {k: v for k, v in kwargs.items() if v}
    return InternshipMaster.objects.filter(**kwargs).select_related("organization")
