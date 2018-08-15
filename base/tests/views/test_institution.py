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
import json
from unittest import mock
from base.tests.factories.entity_version import EntityVersionFactory
from base.tests.factories.entity import EntityFactory
from base.tests.factories.user import UserFactory
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from base.views import institution
from reference.tests.factories.country import CountryFactory


class EntityViewTestCase(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.entity = EntityFactory(country=CountryFactory())
        self.parent = EntityFactory()
        self.start_date = datetime.date(2015, 1, 1)
        self.end_date = datetime.date(2015, 12, 31)

        self.entity_version = EntityVersionFactory(
            entity=self.entity,
            acronym="ENTITY_CHILDREN",
            title="This is the entity version ",
            entity_type="FACULTY",
            parent=self.parent,
            start_date=self.start_date,
            end_date=self.end_date
        )
        self.parent_entity_version = EntityVersionFactory(
            entity=self.parent,
            acronym="ENTITY_PARENT",
            title="This is the entity parent version",
            entity_type="SECTOR",
            start_date=self.start_date,
            end_date=self.end_date
        )

    def test_entities(self):
        self.client.force_login(self.user)
        url = reverse('entities')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_entities_search(self):
        self.client.force_login(self.user)
        url = reverse('entities_search')
        response = self.client.get(url+"?acronym=%s&title=%s&type_choices=%s" % ("ENTITY_CHILDREN", "", ""))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context[-1]['entities_version']), 1)

    def test_entity_read(self):
        self.client.force_login(self.user)
        url = reverse('entity_read', args=[self.entity_version.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_entity_diagram(self):
        self.client.force_login(self.user)
        url = reverse('entity_diagram', args=[self.entity_version.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    @mock.patch('base.models.entity_version.find_by_id')
    @mock.patch('django.contrib.auth.decorators')
    def test_get_entity_address(self,  mock_decorators, mock_find_by_id):
        mock_decorators.login_required = lambda x: x
        mock_decorators.permission_required = lambda *args, **kwargs: lambda func: func
        entity = EntityFactory()
        entity_version = EntityVersionFactory(entity=entity, acronym='SSH', title='Sector of sciences', end_date=None)
        mock_find_by_id.return_value = entity_version
        request = mock.Mock(method='GET')
        response = institution.get_entity_address(request, entity_version.id)
        address_data = ['location', 'postal_code', 'city', 'country_id', 'phone', 'fax']
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode('utf-8'))
        self.assertTrue(data.get('entity_version_exists_now'))
        self.assertIsNotNone(data.get('recipient'))
        for field_name in address_data:
            self.assertEqual(getattr(entity, field_name), data['address'].get(field_name))

    @mock.patch('base.models.entity_version.find_by_id')
    @mock.patch('django.contrib.auth.decorators')
    def test_get_entity_address_case_no_current_entity_version_exists(self,  mock_decorators, mock_find_by_id):
        mock_decorators.login_required = lambda x: x
        mock_decorators.permission_required = lambda *args, **kwargs: lambda func: func
        entity = EntityFactory()
        entity_version = EntityVersionFactory(entity=entity,
                                              acronym='SSH',
                                              title='Sector of sciences',
                                              start_date=datetime.datetime(year=2004, month=1, day=1).date(),
                                              end_date=datetime.datetime(year=2010, month=1, day=1).date())
        mock_find_by_id.return_value = entity_version
        request = mock.Mock(method='GET')
        response = institution.get_entity_address(request, entity_version.id)
        address_data = ['location', 'postal_code', 'city', 'country_id', 'phone', 'fax']
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content.decode('utf-8'))
        self.assertFalse(data.get('entity_version_exists_now'))
        self.assertIsNotNone(data.get('recipient'))
        for field_name in address_data:
            self.assertEqual(getattr(entity, field_name), data['address'].get(field_name))
