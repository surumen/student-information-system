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
from django.core import serializers
from osis_common.models.serializable_model import SerializableModel, SerializableModelAdmin


class DecreeAdmin(SerializableModelAdmin):
    list_display = ('name', 'start_date', 'end_date')
    fieldsets = ((None, {'fields': ('name', 'start_date', 'end_date')}),)
    ordering = ('name',)
    search_fields = ['name']


class Decree(SerializableModel):
    external_id = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=80, unique=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    # def save(self, *args, **kwargs):
    #     # WARNING
    #     # In case a new decree is created, we MUST migrate data from domain and ExternalOffer to the last domain.
    #     super(models.Model, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


def serialize_list(list_decrees):
    """
    Serialize a list of "Decree" objects using the json format.
    Use to send data to osis-portal.
    :param list_decrees: a list of "Decree" objects
    :return: the serialized list (a json)
    """
    return serializers.serialize("json", list_decrees)
