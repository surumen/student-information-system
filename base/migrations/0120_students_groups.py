from __future__ import unicode_literals
from django.db import migrations


def remove_groups(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    db_alias = schema_editor.connection.alias
    Group.objects.using(db_alias).filter(name="internship_students").delete()
    Group.objects.using(db_alias).filter(name="students").delete()


def rollback_groups(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    db_alias = schema_editor.connection.alias
    Group.objects.using(db_alias).bulk_create([
        Group(name="internship_students"),
        Group(name="students")
    ])


class Migration(migrations.Migration):
    dependencies = [
        ('base', '0119_auto_20170516_1326'),
    ]

    operations = [
        migrations.RunPython(remove_groups, rollback_groups),
    ]
