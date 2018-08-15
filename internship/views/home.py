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
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators import http

from internship import models as mdl_internship
from internship.models.cohort import Cohort


@login_required
@permission_required('internship.is_internship_manager', raise_exception=True)
def cohort_home(request, cohort_id):
    cohort = get_object_or_404(Cohort, pk=cohort_id)
    blockable = mdl_internship.internship_offer.get_number_selectable(cohort) > 0
    context = {
        'section': 'internship',
        'blockable': blockable,
        'cohort': cohort,
    }
    return render(request, "internships_home.html", context=context)


@http.require_http_methods(['GET'])
@login_required
@permission_required('internship.is_internship_manager', raise_exception=True)
def view_cohort_selection(request):
    cohorts = Cohort.objects.all()
    return render(request, 'cohort/selection.html', {'cohorts': cohorts})
