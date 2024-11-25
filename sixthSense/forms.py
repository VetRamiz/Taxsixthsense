# sixthSense/forms.py

from django import forms
from .models import Company, Preparer, Client

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'company_name', 'logo',
            'status', 'office_contact', 'phone_number',
            'city', 'state', 'zip_code', 'address','role'
        ]
        widgets = {
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
        labels = {
            'company_name': 'Company Name',
            'logo': 'Company Logo',
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
             'phone', 'account_active'
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

from django import forms

class CompanyLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}))

class PreparerLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}))


from django import forms
from .models import  Company, Preparer


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ['user']


class PreparerForm(forms.ModelForm):
    class Meta:
        model = Preparer
        exclude = ['user']
from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match')
        return cleaned_data

from django import forms
from django.contrib.auth.models import User
from .models import Company, Preparer


from django import forms
from django.contrib.auth.models import User, Group
from .models import Company

from django.core.exceptions import ValidationError
class CompanyRegistrationForm(forms.ModelForm):
    # Fields for the User model
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    email = forms.EmailField(required=True)

    # Fields for the Company model
    class Meta:
        model = Company
        fields = [
            'company_name', 'logo', 'status', 'office_contact', 'phone_number','email',
            'city', 'state', 'zip_code', 'role', 'address',
        ]

    def save(self, commit=True):
        # Check if the username already exists
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists. Please choose a different username.")


    def save(self, commit=True):
        # Create the User instance
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email']
        )

        # Populate the Company profile
        company = super().save(commit=False)
        company.user = user
        company.email = self.cleaned_data['email']  # Sync email with User

        if commit:
            company.save()

            # Assign to the Company group after the user is saved
            company_group, created = Group.objects.get_or_create(name='Company')
            user.groups.add(company_group)  # Add user to the Company group

        return user  # Return the User instance for further use


from django import forms
from django.contrib.auth.models import User, Group
from .models import Preparer


class PreparerRegistrationForm(forms.ModelForm):
    # Fields for the User model
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    email = forms.EmailField(required=True)

    # Fields for the Preparer model
    class Meta:
        model = Preparer
        fields = [
            'first_name', 'last_name', 'office_name', 'office_contact', 'self_employed',
            'view_own_returns', 'guide_required', 'prepares_ny', 'prepares_or_returns',
            'title', 'company_name', 'office_code', 'agree_date', 'phone', 'account_active',
        ]

    def save(self, commit=True):
        # Create the User instance
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email']
        )

        # Populate the Preparer profile
        preparer = super().save(commit=False)
        preparer.user = user
        preparer.preparer_email = self.cleaned_data['email']  # Sync email with User

        if commit:
            preparer.save()

            # Assign to the Preparer group after the user is saved
            preparer_group, created = Group.objects.get_or_create(name='Preparer')
            user.groups.add(preparer_group)  # Add user to the Preparer group

        return user  # Return the User instance for further use

from django import forms
from .models import Preparer

class PreparerProfileForm(forms.ModelForm):
    class Meta:
        model = Preparer
        fields = [
            "first_name",
            "last_name",
            "preparer_email",
            "office_name",
            "office_contact",
            "self_employed",
            "view_own_returns",
            "guide_required",
            "prepares_ny",
            "prepares_or_returns",
            "title",
            "company_name",
            "agree_date",
            "phone",
        ]
        widgets = {
            "agree_date": forms.DateInput(attrs={"type": "date"}),
        }
