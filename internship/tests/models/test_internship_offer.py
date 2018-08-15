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
from django.test import TestCase

from internship.models import internship_offer
from internship.tests.factories.cohort import CohortFactory
from internship.tests.factories.offer import OfferFactory
from internship.tests.models import test_organization, test_internship_speciality


def create_internship_offer(cohort=None):
    if cohort is None:
        cohort = CohortFactory()
    organization = test_organization.create_organization(cohort=cohort)
    speciality = test_internship_speciality.create_speciality(cohort=cohort)

    return OfferFactory(
        speciality=speciality,
        organization=organization,
        title="offer_test",
        maximum_enrollments=20,
        cohort=cohort,
    )


def create_specific_internship_offer(organization, speciality, title="offer_test", cohort=None):
    return OfferFactory(
        speciality=speciality,
        organization=organization,
        title=title,
        cohort=cohort,
        maximum_enrollments=20
    )


class TestInternshipOffer(TestCase):
    def setUp(self):
        self.offer = create_internship_offer()

    def test_find_by_pk(self):
        pk = self.offer.pk
        actual_offer = internship_offer.find_by_pk(pk)
        self.assertEquals(self.offer, actual_offer)

        pk = 45
        self.assertFalse(internship_offer.find_by_pk(pk))
