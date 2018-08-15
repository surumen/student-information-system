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
import urllib.request
import unicodedata
from xml.dom import minidom
import logging
from internship.models.organization import Organization
from osis_common.models.serializable_model import SerializableModel, SerializableModelAdmin


class OrganizationAddressAdmin(SerializableModelAdmin):
    list_display = ('organization', 'label', 'location', 'postal_code', 'city', 'country', 'latitude', 'longitude')
    fieldsets = ((None, {'fields': ('organization', 'label', 'location', 'postal_code', 'city', 'country', 'latitude',
                                    'longitude')}),)
    raw_id_fields = ('organization',)
    search_fields = ['organization__name', 'city']


class OrganizationAddress(SerializableModel):
    organization = models.ForeignKey('Organization', related_name='addresses', related_query_name='address')
    label = models.CharField(max_length=20)
    location = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=255)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    country = models.CharField(max_length=255)

    def __str__(self):
        return u"%s" % self.organization

    def save(self, *args, **kwargs):
        has_organization = False
        try:
            has_organization = (self.organization is not None)
        except Exception:
            self.organization = Organization.objects.latest('id')

        self.label = "Addr"+self.organization.name[:14]
        super(OrganizationAddress, self).save(*args, **kwargs)


def search(**kwargs):
    kwargs = {k: v for k, v in kwargs.items() if v}
    return OrganizationAddress.objects.filter(**kwargs).select_related("organization")


def find_by_id(organization_address_id):
    return OrganizationAddress.objects.get(pk=organization_address_id)
