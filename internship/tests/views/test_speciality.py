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
from django.contrib.auth.models import Permission, User
from django.core.urlresolvers import reverse
from django.test import TestCase

from base.tests.factories.learning_unit import LearningUnitFactory
from internship.models.internship_speciality import InternshipSpeciality
from internship.tests.factories.cohort import CohortFactory
from internship.tests.factories.speciality import SpecialityFactory


class SpecialityViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('demo', 'demo@demo.org', 'passtest')
        permission = Permission.objects.get(codename='is_internship_manager')
        self.user.user_permissions.add(permission)
        self.client.force_login(self.user)

        self.cohort = CohortFactory()

    def test_home(self):

        url = reverse('internships_specialities', kwargs={
            'cohort_id': self.cohort.id,
        })

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'specialities.html')

    def test_create(self):
        url = reverse('speciality_create', kwargs={
            'cohort_id': self.cohort.id,
        })

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'speciality_create.html')

    def test_delete(self):
        specialities = InternshipSpeciality.objects.filter(cohort=self.cohort).count()
        self.assertEqual(specialities, 0)

        speciality = SpecialityFactory(cohort=self.cohort)

        specialities = InternshipSpeciality.objects.filter(cohort=self.cohort).count()
        self.assertEqual(specialities, 1)

        url = reverse('speciality_delete', kwargs={
            'cohort_id': self.cohort.id,
            'speciality_id': speciality.id
        })

        response = self.client.get(url)

        specialities = InternshipSpeciality.objects.filter(cohort=self.cohort).count()
        self.assertEqual(specialities, 0)

        self.assertRedirects(response, reverse('internships_specialities', kwargs={
            'cohort_id': self.cohort.id,
        }))

    def test_modification(self):
        speciality = SpecialityFactory(cohort=self.cohort)

        url = reverse('speciality_modification', kwargs={
            'cohort_id': self.cohort.id,
            'speciality_id': speciality.id,
        })

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'speciality_create.html')
        self.assertEqual(response.context['speciality'], speciality)

    def test_new(self):
        learning_unit = LearningUnitFactory(acronym='DEMO')
        speciality = SpecialityFactory.build(learning_unit=learning_unit)

        url = reverse('speciality_new', kwargs={
            'cohort_id': self.cohort.id,
        })

        response = self.client.post(url, data={
            'learning_unit': learning_unit.acronym,
            'mandatory': True,
            'name': speciality.name,
            'order_position': speciality.order_position,
            'acronym': speciality.acronym,
        })
        self.assertRedirects(response, reverse('internships_specialities', kwargs={
            'cohort_id': self.cohort.id,
        }))

    def test_save(self):
        speciality = SpecialityFactory(name='SUPERMAN', cohort=self.cohort)

        url = reverse('speciality_save', kwargs={
            'cohort_id': self.cohort.id,
            'speciality_id': speciality.id,
        })

        response = self.client.post(url, data={
            'learning_unit': speciality.learning_unit.acronym,
            'mandatory': speciality.mandatory,
            'name': 'DEMO',
            'order_position': speciality.order_position,
            'acronym': speciality.acronym,
        })

        self.assertRedirects(response, reverse('internships_specialities', kwargs={
            'cohort_id': self.cohort.id,
        }))
