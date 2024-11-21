# Generated by Django 5.1 on 2024-11-14 17:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sixthSense', '0002_preparer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('dob', models.DateField()),
                ('entered_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_ids', to='sixthSense.company')),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='sixthSense.company')),
            ],
        ),
    ]
