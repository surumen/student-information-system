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
from django.contrib import admin

from internship.models.internship import Internship

class InternshipEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'internship_offer', 'place', 'period', 'internship')
    fieldsets = ((None, {'fields': ('student', 'internship_offer', 'place', 'period', 'internship')}),)
    raw_id_fields = ('student', 'internship_offer', 'place', 'period')


class InternshipEnrollment(models.Model):
    student = models.ForeignKey('base.student')
    internship_offer = models.ForeignKey('internship.InternshipOffer')
    place = models.ForeignKey('internship.Organization')
    period = models.ForeignKey('internship.Period')
    internship = models.ForeignKey('internship.Internship')

    def __str__(self):
        return u"%s - %s" % (self.student, self.internship_offer.title)


def search(**kwargs):
    kwargs = {k: v for k, v in kwargs.items() if v}
    return InternshipEnrollment.objects.filter(**kwargs)\
                                       .select_related("student", "internship_offer", "place", "period")


def search_by_student_and_internship(student, internship):
    return InternshipEnrollment.objects.filter(student=student, internship=internship)


def find_by_student(student):
    return InternshipEnrollment.objects.filter(student=student)


def find_for_non_mandatory_internship():
    return InternshipEnrollment.objects.filter(internship_choice__gte=1).\
        select_related("student", "internship_offer", "place", "period")

def find_for_internships_for_cohort(cohort):
    internship_ids = Internship.objects.filter(cohort=cohort).values_list("id", flat=True)
    return InternshipEnrollment.objects.filter(internship_id__in=internship_ids).\
        select_related("student", "internship_offer", "internship", "place", "period")
