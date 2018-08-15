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
import datetime

from django.test import TestCase
from django.utils.translation import ugettext_lazy as _

from base.tests.factories.academic_year import AcademicYearFactory
from base.tests.models.test_academic_calendar import create_academic_calendar
from base.tests.factories.offer_year_calendar import OfferYearCalendarFactory
from base.tests.factories.offer_year import OfferYearFactory
from base.forms.academic_calendar import AcademicCalendarForm


class TestAcademicCalendarForm(TestCase):
    def setUp(self):
        self.an_academic_year = AcademicYearFactory()

    def test_with_start_and_end_dates_not_set(self):
        form = AcademicCalendarForm(data={
            "academic_year": self.an_academic_year.pk,
            "title": "Academic event",
            "description": "Description of an academic event"
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['start_date'], _('dates_mandatory_error'))

    def test_with_start_date_higher_than_end_date(self):
        form = AcademicCalendarForm(data={
            "academic_year": self.an_academic_year.pk,
            "title": "Academic event",
            "description": "Description of an academic event",
            "start_date": datetime.date.today(),
            "end_date": datetime.date.today() - datetime.timedelta(days=2)
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['start_date'], _('start_date_must_be_lower_than_end_date'))

    def test_with_end_date_inferior_to_offer_year_calendar_end_date(self):
        an_academic_calendar = create_academic_calendar(an_academic_year=self.an_academic_year)
        an_offer_year = OfferYearFactory(academic_year=self.an_academic_year)
        an_offer_year_calendar = OfferYearCalendarFactory(academic_calendar=an_academic_calendar,
                                                          offer_year=an_offer_year, customized=True)

        form = AcademicCalendarForm(data={
            "academic_year": self.an_academic_year.pk,
            "title": "New title",
            "start_date": an_academic_calendar.start_date,
            "end_date": an_offer_year_calendar.end_date - datetime.timedelta(days=2)
        }, instance=an_academic_calendar)
        self.assertFalse(form.is_valid())
        date_format = str(_('date_format'))
        self.assertEqual(form.errors['end_date'], "%s." % (_('academic_calendar_offer_year_calendar_end_date_error')
                                                           % (an_academic_calendar.title,
                                                           an_offer_year_calendar.end_date.strftime(date_format),
                                                           an_academic_calendar.title,
                                                           an_offer_year_calendar.offer_year.acronym)))

    def test_with_correct_form(self):
        form = AcademicCalendarForm(data={
            "academic_year": self.an_academic_year.pk,
            "title": "Academic event",
            "description": "Description of an academic event",
            "start_date": datetime.date.today(),
            "end_date": datetime.date.today() + datetime.timedelta(days=2)
        })
        self.assertTrue(form.is_valid())
