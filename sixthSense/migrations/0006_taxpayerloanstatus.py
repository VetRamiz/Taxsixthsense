# Generated by Django 5.1 on 2024-11-15 18:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sixthSense', '0005_payoutbreakdown'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaxpayerLoanStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional_preparer', models.TextField(blank=True, null=True)),
                ('application_date', models.DateField()),
                ('year', models.IntegerField()),
                ('decision_date', models.DateField(blank=True, null=True)),
                ('loan_type', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('ssn', models.CharField(max_length=11)),
                ('disb_type', models.CharField(max_length=100)),
                ('advance_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('outstanding_loan_balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('marketing_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('repayment_status', models.CharField(max_length=100)),
                ('group_efin', models.CharField(max_length=50)),
                ('parent_efin', models.CharField(max_length=50)),
                ('office_efin', models.CharField(max_length=50)),
                ('ptin', models.CharField(max_length=50)),
                ('loan_disb_type', models.CharField(max_length=100)),
                ('irs_ack_date', models.CharField(max_length=100)),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_statuses', to='sixthSense.company')),
                ('preparer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_statuses', to='sixthSense.preparer')),
            ],
        ),
    ]