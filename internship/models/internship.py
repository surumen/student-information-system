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
from osis_common.models.serializable_model import SerializableModelAdmin, SerializableModel

class InternshipAdmin(SerializableModelAdmin):
    list_display = (
            'name',
            'speciality',
            'alternate_speciality'
            'cohort',
            'length_in_periods')
    fieldsets = ((None, {'fields':
        (
            'name',
            'speciality',
            'alternate_speciality',
            'cohort',
            'length_in_periods'
        )}),)


class Internship(SerializableModel):
    name = models.CharField(max_length=255, blank=False)
    speciality = models.ForeignKey('internship.InternshipSpeciality', null=True, blank=True)
    alternate_speciality = models.ForeignKey('internship.InternshipSpeciality', null=True, blank=True, related_name="alternate_speciality")
    cohort = models.ForeignKey('internship.Cohort', null=False)
    length_in_periods = models.IntegerField(null=False, default=1)

    def __str__(self):
        return u"%s" % self.name

