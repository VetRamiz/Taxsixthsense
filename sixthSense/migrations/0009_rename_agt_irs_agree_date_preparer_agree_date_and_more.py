# Generated by Django 5.1 on 2024-11-19 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sixthSense', '0008_webreports'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preparer',
            old_name='agt_irs_agree_date',
            new_name='agree_date',
        ),
        migrations.RenameField(
            model_name='preparer',
            old_name='agt_company_name',
            new_name='company_name',
        ),
        migrations.RenameField(
            model_name='preparer',
            old_name='agt_office_code',
            new_name='office_code',
        ),
        migrations.RenameField(
            model_name='preparer',
            old_name='agt_phone',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='preparer',
            old_name='agt_title',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='preparer',
            name='ptin_sidn',
        ),
    ]