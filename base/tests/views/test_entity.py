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
import json
from base.tests.factories.entity_version import EntityVersionFactory
from base.tests.factories.user import UserFactory
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from rest_framework.test import APITestCase


class EntityViewTestCase(APITestCase):

    def setUp(self):
        user = UserFactory()
        token = Token.objects.create(user=user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_create_valid_entity(self):
        entity_version = EntityVersionFactory.build()
        valid_entity = {
            'organization': entity_version.entity.organization.id,
            'external_id': entity_version.entity.external_id,
            'entityversion_set': [
                {
                    "title": entity_version.title,
                    "acronym": entity_version.acronym,
                    "entity_type": entity_version.entity_type,
                    "parent": entity_version.parent.id,
                    "start_date": entity_version.start_date,
                    "end_date": entity_version.end_date
                }
            ],
            'location': entity_version.entity.location,
            'postal_code': entity_version.entity.postal_code,
            'city': entity_version.entity.city,
            'country': entity_version.entity.country_id,
            'website': entity_version.entity.website
        }
        response = self.client.post(
            reverse('post_entities'),
            data=json.dumps(valid_entity),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_entity(self):
        invalid_entity = {
            'organization': 'zfeinvzepn',
        }
        response = self.client.post(
            reverse('post_entities'),
            data=json.dumps(invalid_entity),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
