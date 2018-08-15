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
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU General Public License for more details.
#
#    A copy of this license - GNU General Public License - is available
#    at the root of the source code of this program.  If not,
#    see http://www.gnu.org/licenses/.
#
##############################################################################
import functools
import contextlib
import factory
from django.test import TestCase
from django.test import override_settings
from base.models import person
from base.models.enums import person_source_type
from base.tests.factories.person import PersonFactory, generate_person_email


def create_person(first_name, last_name, email=None):
    a_person = person.Person(first_name=first_name, last_name=last_name, email=email)
    a_person.save()
    return a_person


def create_person_with_user(user):
    a_person = person.Person(first_name=user.first_name, last_name=user.last_name, user=user)
    a_person.save()
    return a_person


class PersonTestCase(TestCase):
    @contextlib.contextmanager
    def assertDontRaise(self):
        try:
            yield
        except AttributeError:
            self.fail('Exception not excepted')


class PersonTest(PersonTestCase):
    def test_find_by_id(self):
        tmp_person = PersonFactory()
        db_person = person.find_by_id(tmp_person.id)
        self.assertIsNotNone(tmp_person.user)
        self.assertEqual(db_person.id, tmp_person.id)
        self.assertEqual(db_person.email, tmp_person.email)

    @override_settings(INTERNAL_EMAIL_SUFFIX='osis.org')
    def test_person_from_extern_source(self):
        person_email = functools.partial(generate_person_email, domain='osis.org')
        p = PersonFactory.build(email=factory.LazyAttribute(person_email),
                                user=None,
                                source=person_source_type.DISSERTATION)
        with self.assertRaises(AttributeError):
            p.save()

    @override_settings(INTERNAL_EMAIL_SUFFIX='osis.org')
    def test_person_from_internal_source(self):
        person_email = functools.partial(generate_person_email, domain='osis.org')
        p = PersonFactory.build(email=factory.LazyAttribute(person_email), user=None)
        with self.assertDontRaise():
            p.save()

    @override_settings(INTERNAL_EMAIL_SUFFIX='osis.org')
    def test_person_without_source(self):
        person_email = functools.partial(generate_person_email, domain='osis.org')
        p = PersonFactory.build(email=factory.LazyAttribute(person_email),
                                user=None,
                                source=None)
        with self.assertDontRaise():
            p.save()

    def test_find_by_global_id(self):
        a_person = person.Person(global_id="123")
        a_person.save()
        dupplicated_person = person.Person(global_id="123")
        dupplicated_person.save()
        found_person = person.find_by_global_id("1234")
        return self.assertEqual(found_person, None, "find_by_global_id should return None if a record is not found.")

    def test_search_employee(self):
        a_lastname = "Dupont"
        a_firstname = "Marcel"
        a_person = person.Person(last_name=a_lastname,
                                 first_name=a_firstname,
                                 employee=True)
        a_person.save()
        self.assertEqual(person.search_employee(a_lastname)[0], a_person)
        self.assertEqual(len(person.search_employee("{}{}".format(a_lastname, a_firstname))), 0)
        self.assertEqual(person.search_employee("{} {}".format(a_lastname, a_firstname))[0], a_person)
        self.assertIsNone(person.search_employee(None))
        self.assertEqual(len(person.search_employee("zzzzzz")), 0)

        a_person_2 = person.Person(last_name=a_lastname,
                                   first_name="Hervé",
                                   employee=True)
        a_person_2.save()
        self.assertEqual(len(person.search_employee(a_lastname)), 2)
        self.assertEqual(len(person.search_employee("{} {}".format(a_lastname, a_firstname))), 1)


