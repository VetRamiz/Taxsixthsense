# Generated by Django 5.1.3 on 2024-11-27 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sixthSense', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='preparer',
            name='ptin',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
