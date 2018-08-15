# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-24 14:01
from __future__ import unicode_literals

from django.db import migrations, connection


origin_year = 2015
destination_year = 2016


def copy_score_sheet_address(apps, schema_editor):

    old_offer_years = _find_offer_years(origin_year)
    new_offer_years = _find_offer_years(destination_year)
    for new_offer in new_offer_years:
        _update_address(new_offer, old_offer_years)


def _offer_years_by_acronym(year):
    offer_years = _find_offer_years(year)
    offers = {}
    for offer_year in offer_years:
        offers.update({offer_year['acronym']: offer_year['id']})
    return offers


def _find_offer_years(year):
    with connection.cursor() as cursor:
        sql = " SELECT id FROM base_academicyear where year= %s "
        cursor.execute(sql, [year])
        ac_year = cursor.fetchone()

        with connection.cursor() as cursor:
            sql = " SELECT * FROM base_offeryear where academic_year_id= %s "
            cursor.execute(sql, [ac_year])
            return dictfetchall(cursor)
    return None


def _update_address(new_offer, old_offer_years):
    old_offer = get_old_offer_year(new_offer['acronym'], old_offer_years)

    if old_offer:
        _copy_address_fields_from_old_to_new_offer(old_offer, new_offer)


def _copy_address_fields_from_old_to_new_offer(old_offer, new_offer):

    with connection.cursor() as cursor:
        sql = "update base_offeryear set recipient=%s, location=%s, postal_code=%s, city=%s,country_id=%s,phone=%s, fax=%s, email=%s where id = %s"
        cursor.execute(sql, [old_offer['recipient'],
                             old_offer['location'],
                             old_offer['postal_code'],
                             old_offer['city'],
                             old_offer['country_id'],
                             old_offer['phone'],
                             old_offer['fax'],
                             old_offer['email'],
                             new_offer['id']])


def copy_program_managers(apps, schema_editor):
    pgm_managers = _find_program_managers()
    new_offer_years = _offer_years_by_acronym(destination_year)
    for manager in pgm_managers:
        _create_new_manager(manager, new_offer_years)


def _find_program_managers():
    with connection.cursor() as cursor:
        sql = " SELECT base_programmanager.id as programmanager_id, base_programmanager.person_id, base_offeryear.id as offeryear_id, base_offeryear.acronym FROM base_programmanager, base_offeryear, base_academicyear where base_offeryear.id = base_programmanager.offer_year_id and base_offeryear.academic_year_id = base_academicyear.id and base_academicyear.year= %s "
        cursor.execute(sql, [origin_year])
        return dictfetchall(cursor)

    return None


def _create_new_manager(manager, new_offer_years):
    manager_offer_year_acronym = manager['acronym']
    new_offer_year = get_offer_year(manager_offer_year_acronym, new_offer_years)

    if new_offer_year and not _program_manager_exists(new_offer_year, manager['person_id']):
        with connection.cursor() as cursor:
            sql = "INSERT INTO base_programmanager (person_id, offer_year_id) VALUES (%s, %s)"
            cursor.execute(sql, [manager['person_id'], new_offer_year])


def get_offer_year(manager_offer_year_acronym, new_offer_years):
    new_offer_year = None
    for key, value in new_offer_years.items():
        if key == manager_offer_year_acronym:
            new_offer_year = new_offer_years[key]
            break
    return new_offer_year


def get_old_offer_year(manager_offer_year_acronym, new_offer_years):
    for row in new_offer_years:
        if row['acronym'] == manager_offer_year_acronym:
            return row

    return None


def _program_manager_exists(new_offer_year, person):
    with connection.cursor() as cursor:
        sql = " SELECT * FROM base_programmanager where offer_year_id=%s and person_id=%s "
        cursor.execute(sql, [new_offer_year, person])
        rows = cursor.fetchall()

        if rows:
            return True

    return False


def dictfetchall(cursor):
    """Returns all rows from a cursor as a dict"""
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
        ]


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0078_offeryear_mail'),
    ]

    operations = [
        migrations.RunPython(copy_program_managers),
        migrations.RunPython(copy_score_sheet_address)
    ]