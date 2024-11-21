# sixthSense/templatetags/form_tags.py

from django import template
from django import template, forms
from sixthSense.models import Company  # Use absolute import

register = template.Library()

@register.filter
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class}
                           )
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            'company_name', 
            'logo', 
            'email_id', 
            'status', 
            'office_contact', 
            'phone_number', 
            'city', 
            'state', 
            'zip_code', 
            'address'
        ]