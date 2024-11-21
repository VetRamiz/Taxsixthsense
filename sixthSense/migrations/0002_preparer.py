# Generated by Django 5.1 on 2024-11-14 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sixthSense', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preparer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptin_sidn', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('data_entry', models.DateTimeField(auto_now_add=True)),
                ('office_name', models.CharField(max_length=255)),
                ('office_contact', models.BooleanField(default=False)),
                ('self_employed', models.BooleanField(default=False)),
                ('view_own_returns', models.BooleanField(default=False)),
                ('guide_required', models.BooleanField(default=False)),
                ('prepares_ny', models.BooleanField(default=False)),
                ('prepares_or_returns', models.BooleanField(default=False)),
                ('agt_title', models.CharField(max_length=100)),
                ('agt_company_name', models.CharField(max_length=255)),
                ('agt_office_code', models.CharField(max_length=50)),
                ('agt_irs_agree_date', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=128)),
                ('agt_phone', models.CharField(max_length=15)),
                ('account_active', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], max_length=8)),
                ('registered_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
