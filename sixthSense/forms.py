# sixthSense/forms.py

from django import forms
from .models import Company, Preparer, Client

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'company_name', 'logo', 'email_id', 'password',
            'status', 'office_contact', 'phone_number',
            'city', 'state', 'zip_code', 'address', 'role'
        ]
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
        labels = {
            'company_name': 'Company Name',
            'logo': 'Company Logo',
            'email_id': 'Email Address',
            'password': 'Password',
            'status': 'Company Status',
            'office_contact': 'Office Contact',
            'phone_number': 'Phone Number',
            'city': 'City',
            'state': 'State',
            'zip_code': 'Zip Code',
            'address': 'Address',
            'role': 'Role',
        }

class PreparerForm(forms.ModelForm):
    class Meta:
        model = Preparer
        fields = [
            'first_name', 'last_name', 'office_name', 'office_contact',
            'self_employed', 'view_own_returns', 'guide_required', 
            'prepares_ny', 'prepares_or_returns', 'title', 
            'company_name', 'office_code', 'agree_date', 
            'email', 'password', 'phone', 'account_active'
        ]
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'agree_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'office_name': 'Office Name',
            'office_contact': 'Office Contact',
            'self_employed': 'Self Employed',
            'view_own_returns': 'View Own Returns',
            'guide_required': 'Guide Required',
            'prepares_ny': 'Prepares NY Returns',
            'prepares_or_returns': 'Prepares OR Returns',
            'title': 'Title',
            'company_name': 'Company Name',
            'office_code': 'Office Code',
            'agree_date': 'Agreement Date',
            'email': 'Email Address',
            'password': 'Password',
            'phone': 'Phone Number',
            'account_active': 'Account Active',
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'company_name', 'first_name', 'last_name', 
            'email', 'password', 'phone', 
            'address', 'dob'
        ]
        widgets = {
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {
            'company_name': 'Company Name',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'password': 'Password',
            'phone': 'Phone Number',
            'address': 'Address',
            'dob': 'DOB',
        }
# forms.py

from django import forms
from .models import ClientAuditList

class ClientAuditListForm(forms.ModelForm):
    class Meta:
        model = ClientAuditList
        fields = [
            'company_name', 'preparer', 'additional_preparer', 
            'date', 'year', 'missing_documents', 'notes', 
            'taxpayer_name', 'identification_drivers_license', 
            'social_security_card', 'healthcare1095_form', 
            'spouse_name', 'identification_drivers_license1', 
            'social_security_card1', 'healthcare1095_form1', 
            'a_of_dependents', 'dependent_ssc', 
            'healthcare_card', 'birth_certificate', 
            'application_w_signature', 'signed_documents', 
            'w2', 'self_employment_log', 'a1099', 
            'ssa', 'a1098t',
        ]
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            # You can add other widgets as needed
        }
        from django import forms
from .models import TaxpayerLoanStatus

class TaxpayerLoanStatusForm(forms.ModelForm):
    class Meta:
        model = TaxpayerLoanStatus
        fields = [
            'company_name', 'preparer', 'additional_preparer', 'application_date',
            'year', 'decision_date', 'loan_type', 'status', 'last_name',
            'first_name', 'ssn', 'disb_type', 'advance_amount',
            'outstanding_loan_balance', 'marketing_fee', 'repayment_status',
            'group_efin', 'parent_efin', 'office_efin', 'ptin',
            'loan_disb_type', 'irs_ack_date'
        ]

from django import forms

class CompanyLoginForm(forms.Form):
    email = forms.EmailField(label="Company Email", max_length=255)
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

    def __init__(self, *args, **kwargs):
        super(CompanyLoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
from django import forms

class PreparerLoginForm(forms.Form):
    email = forms.EmailField(label="Preparer Email", max_length=255)
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

    def __init__(self, *args, **kwargs):
        super(PreparerLoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})

