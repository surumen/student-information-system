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
import factory
import factory.fuzzy
import string
from django.utils import timezone
from base.tests.factories.academic_year import AcademicYearFactory
from osis_common.utils.datetime import get_tzinfo


def generate_start_date(academic_calendar):
    if academic_calendar.academic_year:
        return academic_calendar.academic_year.start_date
    else:
        return datetime.date(timezone.now().year, 9, 30)


def generate_end_date(academic_calendar):
    if academic_calendar.academic_year:
        return academic_calendar.academic_year.end_date
    else:
        return datetime.date(timezone.now().year+1, 9, 30)


class AcademicCalendarFactory(factory.DjangoModelFactory):
    class Meta:
        model = 'base.AcademicCalendar'

    external_id = factory.fuzzy.FuzzyText(length=10, chars=string.digits)
    changed = factory.fuzzy.FuzzyDateTime(datetime.datetime(2016, 1, 1, tzinfo=get_tzinfo()),
                                          datetime.datetime(2017, 3, 1, tzinfo=get_tzinfo()))
    academic_year = factory.SubFactory(AcademicYearFactory)
    title = factory.Sequence(lambda n: 'Academic Calendar - %d' % n)
    start_date = factory.LazyAttribute(generate_start_date)
    end_date = factory.LazyAttribute(generate_end_date)
    highlight_title = factory.Sequence(lambda n: 'Highlight - %d' % n)
    highlight_description = factory.Sequence(lambda n: 'Description - %d' % n)
    highlight_shortcut = factory.Sequence(lambda n: 'Shortcut Highlight - %d' % n)
    reference = None

