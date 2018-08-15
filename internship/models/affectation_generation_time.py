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
from django.contrib import admin
from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class AffectationGenerationTimeAdmin(admin.ModelAdmin):
    list_display = ('start_date_time', 'end_date_time', 'generated_by', 'cohort')
    fieldsets = ((None, {'fields': ('start_date_time', 'end_date_time', 'generated_by', 'cohort')}),)


class AffectationGenerationTime(models.Model):
    start_date_time = models.DateTimeField()
    end_date_time = models.DateTimeField()
    generated_by = models.CharField(max_length=255, default='None')
    cohort = models.ForeignKey('internship.cohort', null=False, on_delete=models.CASCADE)

    def __str__(self):
        return u"%s - %s" % (self.start_date_time, self.end_date_time)


def get_latest():
    try:
        return AffectationGenerationTime.objects.latest('start_date_time')
    except ObjectDoesNotExist:
        return None
