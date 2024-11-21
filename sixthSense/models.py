# sixthSense/models.py
from django.db import models

class Company(models.Model):
    COMPANY_STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    company_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos/')
    email_id = models.EmailField()
    password = models.CharField(max_length=128)
    status = models.CharField(max_length=8, choices=COMPANY_STATUS_CHOICES)
    office_contact = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    address = models.TextField()
    registered_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.company_name


class Preparer(models.Model):
    ACCOUNT_STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

   
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    data_entry = models.DateTimeField(auto_now_add=True)
    office_name = models.CharField(max_length=255)
    office_contact = models.BooleanField(default=False)
    self_employed = models.BooleanField(default=False)
    view_own_returns = models.BooleanField(default=False)
    guide_required = models.BooleanField(default=False)
    prepares_ny = models.BooleanField(default=False)
    prepares_or_returns = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255)
    office_code = models.CharField(max_length=50)
    agree_date = models.DateField()
    email = models.EmailField()
    password = models.CharField(max_length=128)
    phone = models.CharField(max_length=15)
    account_active = models.CharField(max_length=8, choices=ACCOUNT_STATUS_CHOICES)
    registered_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Client(models.Model):
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='clients')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    dob = models.DateField()
    entered_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name


class ClientAuditList(models.Model):
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='audit_lists')
    preparer = models.ForeignKey(Preparer, on_delete=models.CASCADE, related_name='audit_lists')
    additional_preparer = models.TextField(blank=True, null=True)
    date = models.DateField()
    year = models.IntegerField()  # You could derive this from the date if needed
    missing_documents = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    taxpayer_name = models.CharField(max_length=255)
    identification_drivers_license = models.BooleanField(default=False)
    social_security_card = models.BooleanField(default=False)
    healthcare1095_form = models.BooleanField(default=False)
    spouse_name = models.CharField(max_length=255, blank=True, null=True)
    identification_drivers_license1 = models.BooleanField(default=False)
    social_security_card1 = models.BooleanField(default=False)
    healthcare1095_form1 = models.BooleanField(default=False)
    a_of_dependents = models.BooleanField(default=False)
    dependent_ssc = models.BooleanField(default=False)
    healthcare_card = models.BooleanField(default=False)
    birth_certificate = models.BooleanField(default=False)
    application_w_signature = models.BooleanField(default=False)
    signed_documents = models.BooleanField(default=False)
    w2 = models.BooleanField(default=False)
    self_employment_log = models.BooleanField(default=False)
    a1099 = models.BooleanField(default=False)
    ssa = models.BooleanField(default=False)
    a1098t = models.BooleanField(default=False)

    @property
    def total_missing(self):
        return sum([
            not self.identification_drivers_license,
            not self.social_security_card,
            not self.healthcare1095_form,
            not self.identification_drivers_license1,
            not self.social_security_card1,
            not self.healthcare1095_form1,
            not self.a_of_dependents,
            not self.dependent_ssc,
            not self.healthcare_card,
            not self.birth_certificate,
            not self.application_w_signature,
            not self.signed_documents,
            not self.w2,
            not self.self_employment_log,
            not self.a1099,
            not self.ssa,
            not self.a1098t,
        ])

    def __str__(self):
        return f"Audit for {self.taxpayer_name} - {self.date}"


class PayoutBreakdown(models.Model):
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='payouts_by_name')
    preparer = models.ForeignKey(Preparer, on_delete=models.CASCADE, related_name='payouts')
    additional_preparer = models.TextField(blank=True, null=True)
    taxpayer_first_name = models.CharField(max_length=100)
    taxpayer_last_name = models.CharField(max_length=100)
    total_prep_fee_charged = models.DecimalField(max_digits=10, decimal_places=2)
    fees_intercepted = models.DecimalField(max_digits=10, decimal_places=2)
    total_prep_fee_deposited = models.DecimalField(max_digits=10, decimal_places=2)
    funding_date = models.DateField()
    year = models.IntegerField()  # You could derive this from the funding_date if needed
    partnership_remaining_balance = models.DecimalField(max_digits=10, decimal_places=2)
    advance_loan_fees = models.DecimalField(max_digits=10, decimal_places=2)
    sum_total_preparer = models.DecimalField(max_digits=10, decimal_places=2)
    split = models.DecimalField(max_digits=5, decimal_places=2)
    payout = models.DecimalField(max_digits=10, decimal_places=2)
    prior_week_hold = models.DecimalField(max_digits=10, decimal_places=2)
    current_week_hold = models.DecimalField(max_digits=10, decimal_places=2)
    total_hold = models.DecimalField(max_digits=10, decimal_places=2)
    release_hold_amt = models.DecimalField(max_digits=10, decimal_places=2)
    dd_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"Payout Breakdown for {self.taxpayer_first_name} {self.taxpayer_last_name} - {self.funding_date}"


class TaxpayerLoanStatus(models.Model):
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='loan_statuses')
    preparer = models.ForeignKey(Preparer, on_delete=models.CASCADE, related_name='loan_statuses')
    additional_preparer = models.TextField(blank=True, null=True)
    application_date = models.DateField()
    year = models.IntegerField()  # You could derive this from application_date if needed
    decision_date = models.DateField(blank=True, null=True)
    loan_type = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    ssn = models.CharField(max_length=11)  # Format: XXX-XX-XXXX
    disb_type = models.CharField(max_length=100)
    advance_amount = models.DecimalField(max_digits=10, decimal_places=2)
    outstanding_loan_balance = models.DecimalField(max_digits=10, decimal_places=2)
    marketing_fee = models.DecimalField(max_digits=10, decimal_places=2)
    repayment_status = models.CharField(max_length=100)
    group_efin = models.CharField(max_length=50)
    parent_efin = models.CharField(max_length=50)
    office_efin = models.CharField(max_length=50)
    ptin = models.CharField(max_length=50)
    loan_disb_type = models.CharField(max_length=100)
    irs_ack_date = models.CharField(max_length=100)  # Can change to DateField if appropriate

    def __str__(self):
        return f"Loan Status for {self.first_name} {self.last_name} - {self.application_date}"
class WebReportTaxesToGo(models.Model):
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='web_reports_by_name')
    
    preparer = models.ForeignKey(Preparer, on_delete=models.CASCADE, related_name='web_reports')
    additional_preparer = models.TextField(blank=True, null=True)
    group_name = models.IntegerField()
    efin = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    cell_phone = models.CharField(max_length=15)
    referral_code = models.CharField(max_length=100)
    app_submit_date = models.DateField()
    referrer = models.DateField(blank=True, null=True)
    validation_code = models.IntegerField()

    def __str__(self):
        return f"Web Report for {self.first_name} {self.last_name} - {self.app_submit_date}"
class WebReports(models.Model):
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='web_reports')
    file_title = models.CharField(max_length=255)
    file = models.FileField(upload_to='web_reports/')
    uploaded_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.file_title} - {self.company_id.company_name}"