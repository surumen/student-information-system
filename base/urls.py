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
from django.conf.urls import url, include

from base.views import learning_unit, offer, common, institution, organization, academic_calendar, \
    my_osis, entity, student, education_group

urlpatterns = [
    url(r'^$', common.home, name='home'),

    url(r'^academic_actors/$', institution.academic_actors, name='academic_actors'),

    url(r'^academic_calendars/', include([
        url(r'^$', academic_calendar.academic_calendars, name='academic_calendars'),
        url(r'^search$', academic_calendar.academic_calendars_search, name='academic_calendars_search'),
        url(r'^(?P<academic_calendar_id>[0-9]+)/$', academic_calendar.academic_calendar_read, name='academic_calendar_read'),
        url(r'^form(?:/(?P<academic_calendar_id>[0-9]+))?/$', academic_calendar.academic_calendar_form,
            name='academic_calendar_form'),
    ])),

    url(r'^academic_year/$', common.academic_year, name='academic_year'),

    url(r'^admin/', include([
        url(r'^data/$', common.data, name='data'),
        url(r'^data/maintenance$', common.data_maintenance, name='data_maintenance'),
        url(r'^storage/$', common.storage, name='storage'),
    ])),

    url(r'^api/v1/entities/$', entity.post_entities, name='post_entities'),

    url(r'^catalog/$', common.catalog, name='catalog'),

    url(r'^entities/', include([
        url(r'^$', institution.entities, name='entities'),
        url(r'^search$', institution.entities_search, name='entities_search'),
        url(r'^(?P<entity_version_id>[0-9]+)/', include([
            url(r'^$', institution.entity_read, name='entity_read'),
            url(r'^address/$', institution.get_entity_address, name='entity_address'),
            url(r'^diagram/$', institution.entity_diagram, name='entity_diagram'),
            url(r'^versions/$', institution.entities_version, name='entities_version'),
        ]))
    ])),

    url(r'^institution/', include([
        url(r'^$', institution.institution, name='institution'),
        url(r'^mandates/$', institution.mandates, name='mandates'),
    ])),

    url(r'^learning_units/', include([
        url(r'^$', learning_unit.learning_units, name='learning_units'),
        url(r'^by_activity/', learning_unit.learning_units_activity, name='learning_units_activity'),
        url(r'^by_service_course/', learning_unit.learning_units_service_course, name='learning_units_service_course'),
        url(r'^new/', include([
            url(r'^academic_year_id=(?P<academic_year>[0-9]+)$', learning_unit.learning_unit_create,
                name="learning_unit_create"),
            url(r'^learning_unit_year_add/$', learning_unit.learning_unit_year_add, name='learning_unit_year_add')
        ])),
        url(r'^(?P<learning_unit_year_id>[0-9]+)/', include([
            url(r'^$', learning_unit.learning_unit_identification, name='learning_unit'),
            url(r'^formations/$', learning_unit.learning_unit_formations, name="learning_unit_formations"),
            url(r'^components/$', learning_unit.learning_unit_components, name="learning_unit_components"),
            url(r'^pedagogy/$', learning_unit.learning_unit_pedagogy, name="learning_unit_pedagogy"),
            url(r'^pedagogy/edit/$', learning_unit.learning_unit_pedagogy_edit, name="learning_unit_pedagogy_edit"),
            url(r'^attributions/$', learning_unit.learning_unit_attributions,
                name="learning_unit_attributions"),
            url(r'^proposals/$', learning_unit.learning_unit_proposals, name="learning_unit_proposals"),
            url(r'^specifications/$', learning_unit.learning_unit_specifications, name="learning_unit_specifications"),
            url(r'^specifications/edit/$', learning_unit.learning_unit_specifications_edit, name="learning_unit_specifications_edit"),
            url(r'^component/edit/$', learning_unit.learning_unit_component_edit, name="learning_unit_component_edit"),
            url(r'^class/edit/$', learning_unit.learning_class_year_edit, name="learning_class_year_edit"),
            url(r'^volumes/', include([
                url(u'^$', learning_unit.learning_unit_volumes_management, name="learning_unit_volumes_management"),
                url(u'^validation/$', learning_unit.volumes_validation, name="volumes_validation")])),
        ])),
        url(r'^check/$', learning_unit.check_acronym, name="check_acronym"),
    ])),

    url(r'^my_osis/', include([
        url(r'^$', my_osis.my_osis_index, name="my_osis"),
        url(r'^management_tasks/messages_templates', my_osis.messages_templates_index, name="messages_templates"),
        url(r'^my_messages/', include([
            url(r'^$', my_osis.my_messages_index, name="my_messages"),
            url(r'^action/$', my_osis.my_messages_action, name="my_messages_action"),
            url(r'^(?P<message_id>[0-9]+)/', include([
                url(r'^read/$', my_osis.read_message, name="read_my_message"),
                url(r'^delete/$', my_osis.delete_from_my_messages, name="delete_my_message"),
                url(r'^send_message_again/$', my_osis.send_message_again, name='send_message_again')
            ]))
        ])),
        url(r'^profile/', include([
            url(r'^$', my_osis.profile, name='profile'),
            url(r'^lang/$', my_osis.profile_lang, name='profile_lang'),
            url(r'^lang/edit/([A-Za-z-]+)/$', my_osis.profile_lang_edit, name='lang_edit')
        ]))
    ])),

    url(r'^noscript/$', common.noscript, name='noscript'),

    url(r'^offers/', include([
        url(r'^$', offer.offers, name='offers'),
        url(r'^search$', offer.offers_search, name='offers_search'),
        url(r'^(?P<offer_year_id>[0-9]+)/', include([
            url(r'^$', offer.offer_read, name='offer_read'),
            url(r'^academic_calendar/$', offer.offer_academic_calendar_tab, name='offer_academic_calendar_tab'),
            url(r'^program_managers/$', offer.offer_program_managers_tab, name='offer_program_managers_tab'),
        ]))
    ])),
    url(r'^educationgroups/', include([
        url(r'^$', education_group.education_groups, name='education_groups'),
        url(r'^(?P<education_group_year_id>[0-9]+)/', include([
            url(r'^$', education_group.education_group_read, name='education_group_read'),
        ]))
    ])),

    url(r'^offer_year_calendars/([0-9]+)/$', offer.offer_year_calendar_read, name='offer_year_calendar_read'),

    url(r'^organizations/', include([
        url(r'^$', organization.organizations, name='organizations'),
        url(r'^search$', organization.organizations_search, name='organizations_search'),
        url(r'^save/$', organization.organization_new, name='organization_save_new'),
        url(r'^create/$', organization.organization_create, name='organization_create'),
        url(r'^(?P<organization_id>[0-9]+)/', include([
            url(r'^$', organization.organization_read, name='organization_read'),
            url(r'^edit/$', organization.organization_edit, name='organization_edit'),
            url(r'^save/$', organization.organization_save, name='organization_save'),
        ])),
    ])),

    url(r'^organization_address/', include([
        url(r'^save/$', organization.organization_address_new, name='organization_address_save_new'),
        url(r'^(?P<organization_address_id>[0-9]+)/', include([
            url(r'^read/$', organization.organization_address_read,
                name='organization_address_read'),
            url(r'^edit/$', organization.organization_address_edit,
                name='organization_address_edit'),
            url(r'^save/$', organization.organization_address_save,
                name='organization_address_save'),
            url(r'^create/$', organization.organization_address_create,
                name='organization_address_create'),
            url(r'^delete/$', organization.organization_address_delete,
                name='organization_address_delete')
        ]))
    ])),

    url(r'^studies/$', common.studies, name='studies'),
    url(r'^students/', include([
        url(r'^$', student.students, name='students'),
        url(r'^search$', student.student_search, name='students_search'),
        url(r'^(?P<student_id>[0-9]+)/', include([
            url(r'^$', student.student_read, name='student_read'),
            url(r'^picture$', student.student_picture, name='student_picture'),
        ]))
    ])),
]
