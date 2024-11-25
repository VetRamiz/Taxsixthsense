# sixthSense/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Preparer, Company
from .forms import PreparerForm, CompanyForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CompanyLoginForm, PreparerLoginForm
from .models import Company, Preparer
from .models import Client
from .forms import ClientForm
from .models import ClientAuditList, PayoutBreakdown
from .forms import ClientAuditListForm
from .models import Company
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import CompanyForm

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from django.contrib import messages


def index(request):
    return render(request, 'sixthSense/index.html')
# Dashboard view to register a new company
def dashboard(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES)  # Handle file uploads for logos
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to the dashboard
    else:
        form = CompanyForm()

    return render(request, 'sixthSense/dashboard.html', {'form': form})

# Company report view with search and filter options
def company_report(request):
    query = request.GET.get('q', '')
    status_filter = request.GET.get('status', '')

    companies = Company.objects.all()

    if query:
        companies = companies.filter(company_name__icontains=query)

    if status_filter:
        companies = companies.filter(status=status_filter)

    return render(request, 'sixthSense/company_report.html', {
        'companies': companies,
        'query': query,
        'status_filter': status_filter,
    })

from django.shortcuts import render, redirect
from .forms import CompanyRegistrationForm, PreparerRegistrationForm


def register_company(request):
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST, request.FILES)  # Include FILES for logo upload
        if form.is_valid():
            form.save()
            return redirect('login_company')  # Redirect to Company login
    else:
        form = CompanyRegistrationForm()
    return render(request, 'sixthSense/register_company.html', {'form': form})


def register_preparer(request):
    if request.method == 'POST':
        form = PreparerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_preparer')  # Redirect to Preparer login
    else:
        form = PreparerRegistrationForm()
    return render(request, 'sixthSense/register_preparer.html', {'form': form})



def company_details(request, pk):
    company = get_object_or_404(Company, pk=pk)
    return render(request, 'sixthSense/company_details.html', {
        'company': company,
    })
# View to edit a specific company
def edit_company(request, pk):
    company = get_object_or_404(Company, pk=pk)
    
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_report')  # Redirect to the company report view
    else:
        form = CompanyForm(instance=company)

    return render(request, 'sixthSense/edit_company.html', {'form': form, 'company': company})

# View to delete a specific company
def delete_company(request, pk):
    company = get_object_or_404(Company, pk=pk)
    company.delete()
    return redirect('company_report')


def preparer_report(request):
    preparers = Preparer.objects.all()
    return render(request, 'sixthSense/preparer_report.html', {'preparers': preparers})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PreparerProfileForm

from django.shortcuts import render, get_object_or_404

from django.shortcuts import get_object_or_404

@login_required
def edit_preparer_inline(request, pk):
    preparer = get_object_or_404(Preparer, pk=pk)  # Fetch preparer by primary key

    if request.method == "POST":
        form = PreparerProfileForm(request.POST, instance=preparer)
        if form.is_valid():
            form.save()
            messages.success(request, "Preparer updated successfully.")
            return redirect("preparer_report")  # Redirect back to the report view
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = PreparerProfileForm(instance=preparer)

    context = {
        "form": form,
        "preparer": preparer,
    }
    return render(request, "sixthSense/edit_preparer_inline.html", context)



@login_required
def edit_preparer(request):
    preparer = request.user.preparer_profile  # Get the preparer profile of the logged-in user

    if request.method == "POST":
        form = PreparerProfileForm(request.POST, instance=preparer)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully.")
            return redirect("preparer_profile")  # Assuming 'preparer_profile' is the name of the profile view
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = PreparerProfileForm(instance=preparer)

    context = {
        "form": form,
    }
    return render(request, "sixthSense/edit_preparer.html", context)

def delete_preparer(request, pk):
    preparer = get_object_or_404(Preparer, pk=pk)
    preparer.delete()
    return redirect('preparer_report')


from django.shortcuts import render, get_object_or_404
from .models import Preparer

def preparer_details(request, preparer_id):
    preparer = get_object_or_404(Preparer, id=preparer_id)
    return render(request, 'sixthSense/preparer_details.html', {'preparer': preparer})

# views.py

def register_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')  # Redirect to the client list after registration
    else:
        form = ClientForm()
    
    return render(request, 'sixthSense/client_registration.html', {'form': form})

def client_list(request):
    search_last_name = request.GET.get('last_name', '')
    clients = Client.objects.filter(last_name__icontains=search_last_name)

    return render(request, 'sixthSense/client_list.html', {
        'clients': clients,
        'search_last_name': search_last_name,
    })

def edit_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    
    return render(request, 'sixthSense/client_registration.html', {'form': form})

def delete_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'sixthSense/client_confirm_delete.html', {'client': client})

def client_details(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    return render(request, 'sixthSense/client_details.html', {'client': client})

# views.py


def create_audit(request):
    if request.method == 'POST':
        form = ClientAuditListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('audit_list')  # Redirect to the audit list after creation
    else:
        form = ClientAuditListForm()
    
    return render(request, 'sixthSense/create_audit.html', {'form': form})

def audit_list(request):
    audits = ClientAuditList.objects.all()
    return render(request, 'sixthSense/audit_list.html', {'audits': audits})

def audit_detail(request, pk):
    audit = get_object_or_404(ClientAuditList, pk=pk)
    return render(request, 'sixthSense/audit_detail.html', {'audit': audit})

def edit_audit(request, pk):
    audit = get_object_or_404(ClientAuditList, pk=pk)
    if request.method == 'POST':
        form = ClientAuditListForm(request.POST, instance=audit)
        if form.is_valid():
            form.save()
            return redirect('audit_list')  # Redirect to the audit list after editing
    else:
        form = ClientAuditListForm(instance=audit)
    
    return render(request, 'sixthSense/create_audit.html', {'form': form})

def delete_audit(request, pk):
    audit = get_object_or_404(ClientAuditList, pk=pk)
    if request.method == 'POST':
        audit.delete()
        return redirect('audit_list')  # Redirect to the audit list after deletion
    return render(request, 'sixthSense/delete_audit.html', {'audit': audit})
from django.shortcuts import render, redirect, get_object_or_404
from .models import TaxpayerLoanStatus
from .forms import TaxpayerLoanStatusForm

def create_loan_status(request):
    if request.method == 'POST':
        form = TaxpayerLoanStatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('loan_status_report')  # Redirect to the report page
    else:
        form = TaxpayerLoanStatusForm()
    return render(request, 'sixthSense/create_loan_status.html', {'form': form})

def loan_status_report(request):
    loan_statuses = TaxpayerLoanStatus.objects.all()
    return render(request, 'sixthSense/loan_status_report.html', {'loan_statuses': loan_statuses})

def edit_loan_status(request, pk):
    loan_status = get_object_or_404(TaxpayerLoanStatus, pk=pk)
    if request.method == 'POST':
        form = TaxpayerLoanStatusForm(request.POST, instance=loan_status)
        if form.is_valid():
            form.save()
            return redirect('loan_status_report')
    else:
        form = TaxpayerLoanStatusForm(instance=loan_status)
    return render(request, 'sixthSense/create_loan_status.html', {'form': form})

def delete_loan_status(request, pk):
    loan_status = get_object_or_404(TaxpayerLoanStatus, pk=pk)
    if request.method == 'POST':
        loan_status.delete()
        return redirect('loan_status_report')
    return render(request, 'sixthSense/delete_loan_status.html', {'loan_status': loan_status})
def loan_status_detail(request, pk):
    loan_status = get_object_or_404(TaxpayerLoanStatus, pk=pk)
    return render(request, 'sixthSense/loan_status_detail.html', {'loan_status': loan_status})


from django.shortcuts import render
from django.http import HttpResponse
from .services import get_audit_data, get_payout_data, get_loan_data

def company_dashboard(request):
    # Access the company using the correct related_name
    try:
        company = request.user.company_profile
    except AttributeError:
        return HttpResponse("User is not associated with any company.", status=400)

    company_id = company.id  # Get the company ID
    selected_year = request.GET.get("year")  # Retrieve the selected year from the dropdown

    # Fetch data from services
    audit_data = get_audit_data(company_id, selected_year)
    payout_data = get_payout_data(company_id, selected_year)
    loan_data = get_loan_data(company_id, selected_year)

    # Prepare context for the template
    context = {
        "company": company,
        "audit_data": audit_data,
        "payout_data": payout_data,
        "loan_data": loan_data,
        "selected_year": selected_year,
        "years": list(range(2016, 2035)),  # Example range for the dropdown
    }

    return render(request, "sixthSense/company_dashboard.html", context)









from django.shortcuts import render
from django.db.models import Sum, Count


def preparer_dashboard(request):
    # Get the current preparer from the logged-in user
    preparer = request.user.preparer_profile

    # Filter ClientAuditList and PayoutBreakdown for this preparer
    audit_list = ClientAuditList.objects.filter(preparer=preparer)
    payout_list = PayoutBreakdown.objects.filter(preparer=preparer)

    # Extract year filter from the GET request
    selected_year = request.GET.get('year', '')

    # Filter by year if selected
    if selected_year:
        audit_list = audit_list.filter(year=selected_year)
        payout_list = payout_list.filter(year=selected_year)

    # Dashboard Calculations
    total_clients = audit_list.count()
    total_prep_fee_charged = payout_list.aggregate(Sum('total_prep_fee_charged'))['total_prep_fee_charged__sum'] or 0
    total_payout = payout_list.aggregate(Sum('payout'))['payout__sum'] or 0

    # Calculate total_missing dynamically
    total_missing_docs = sum(audit.total_missing for audit in audit_list)

    # Percentage of Missing Documents
    missing_docs_percentage = (total_missing_docs / total_clients * 100) if total_clients > 0 else 0

    # Company names associated with this preparer
    companies = list(audit_list.values_list('company_name__company_name', flat=True).distinct())

    # Get distinct years from ClientAuditList
    distinct_years = audit_list.values_list('year', flat=True).distinct()

    context = {
        'preparer': preparer,
        'total_clients': total_clients,
        'total_prep_fee_charged': total_prep_fee_charged,
        'total_payout': total_payout,
        'total_missing_docs': total_missing_docs,
        'missing_docs_percentage': missing_docs_percentage,
        'companies': companies,
        'distinct_years': distinct_years,
        'selected_year': selected_year,
    }
    return render(request, 'sixthSense/preparer_dashboard.html', context)




from django.shortcuts import redirect

def logout_view(request):
    # Clear the session
    request.session.flush()
    # Redirect to login page
    return redirect('index')


def login_company(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.groups.filter(name='Company').exists():  # Check if the user belongs to the 'Company' group
                login(request, user)
                return redirect('company_report')  # Redirect to the company dashboard
            else:
                messages.error(request, "You are not authorized to log in as a company.")
                return redirect('login_company')
    else:
        form = AuthenticationForm()
    return render(request, 'sixthSense/login_company.html', {'form': form})

def login_preparer(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.groups.filter(name='Preparer').exists():  # Check if the user belongs to the 'Preparer' group
                login(request, user)
                return redirect('preparer_dashboard')  # Redirect to the preparer dashboard
            else:
                messages.error(request, "You are not authorized to log in as a preparer.")
                return redirect('login_preparer')
    else:
        form = AuthenticationForm()
    return render(request, 'sixthSense/login_preparer.html', {'form': form})

from django.shortcuts import render
from django.db.models import Sum, F
from .models import PayoutBreakdown
from .services import get_partnership_payroll_data  # Optional: If needed for complex aggregations

def partnership_payroll_report(request):
    # Correctly reference the related Preparer object
    preparer = request.user.preparer_profile  # Adjusted for related_name='preparer_profile'
    selected_year = request.GET.get("year")  # Year selected from the dropdown (if any)
    
    # Fetch partnership payroll data
    payroll_data = get_partnership_payroll_data(preparer.id, selected_year)

    # Prepare context for template
    context = {
        "payroll_data": payroll_data,
        "selected_year": selected_year,
        "years": list(range(2020, 2025)),  # Example range for the year dropdown
    }

    return render(request, "sixthSense/partnership_payroll_report.html", context)

from django.shortcuts import render
from .models import ClientAuditList
from django.db.models import Q, Case, When, IntegerField

def taxpayer_audit_report(request):
    # Get the logged-in preparer's profile
    preparer = request.user.preparer_profile  # Use related_name 'preparer_profile'
    selected_year = request.GET.get("year")  # Optional year filter

    # Fetch audits related to the preparer, filtered by year if provided
    audits = ClientAuditList.objects.filter(preparer=preparer)
    if selected_year:
        audits = audits.filter(year=selected_year)

    # Annotate total missing documents using the SQL logic translated into Django ORM
    audits = audits.annotate(
        total_missing=(
            Case(When(identification_drivers_license=False, then=1), default=0, output_field=IntegerField()) +
            Case(When(social_security_card=False, then=1), default=0, output_field=IntegerField()) +
            Case(When(healthcare1095_form=False, then=1), default=0, output_field=IntegerField()) +
            Case(When(identification_drivers_license1=False, then=1), default=0, output_field=IntegerField()) +
            Case(When(social_security_card1=False, then=1), default=0, output_field=IntegerField()) +
            Case(When(healthcare1095_form1=False, then=1), default=0, output_field=IntegerField()) +
            Case(When(healthcare_card=False, then=1), default=0, output_field=IntegerField()) +
            Case(When(birth_certificate=False, then=1), default=0, output_field=IntegerField()) +
            Case(When(application_w_signature=False, then=1), default=0, output_field=IntegerField()) +
            Case(When(signed_documents=False, then=1), default=0, output_field=IntegerField()) +
            Case(When(w2=False, then=1), default=0, output_field=IntegerField()) +
            Case(When(self_employment_log=False, then=1), default=0, output_field=IntegerField()) +
            Case(When(a1099=False, then=1), default=0, output_field=IntegerField()) +
            Case(When(ssa=False, then=1), default=0, output_field=IntegerField()) +
            Case(When(a1098t=False, then=1), default=0, output_field=IntegerField())
        )
    )

    # Prepare context for the template
    context = {
        "audits": audits,
        "selected_year": selected_year,
        "years": list(range(2019, 2036)),  # Example range for dropdown
    }

    return render(request, "sixthSense/taxpayer_audit_report.html", context)
from django.shortcuts import render
from .models import TaxpayerLoanStatus

def taxpayer_loan_report(request):
    # Get the logged-in preparer's profile
    preparer = request.user.preparer_profile  # Use related_name 'preparer_profile'
    selected_year = request.GET.get("year")  # Optional year filter

    # Filter loan statuses specific to the preparer and optionally by year
    loans = TaxpayerLoanStatus.objects.filter(preparer=preparer)
    if selected_year:
        loans = loans.filter(year=selected_year)

    # Prepare context for the template
    context = {
        "loans": loans,
        "selected_year": selected_year,
        "years": list(range(2020, 2025)),  # Example range for dropdown
    }

    return render(request, "sixthSense/taxpayer_loan_report.html", context)
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def preparer_profile(request):
    # Get the logged-in user's preparer profile
    preparer = request.user.preparer_profile

    # Prepare context for the template
    context = {
        "preparer": preparer,
    }

    return render(request, "sixthSense/preparer_profile.html", context)

import pandas as pd
from django.http import HttpResponse
from .models import Company, PayoutBreakdown, ClientAuditList, TaxpayerLoanStatus

def export_data_to_excel(request):
    # Ensure the user is associated with a company
    if not hasattr(request.user, 'company_profile'):
        return HttpResponse("You are not authorized to export data.", status=403)

    company = request.user.company_profile

    # Collect data for all models related to the company
    data = {
        "PayoutBreakdown": list(PayoutBreakdown.objects.filter(company_name=company).values()),
        "ClientAuditList": list(ClientAuditList.objects.filter(company_name=company).values()),
        "TaxpayerLoanStatus": list(TaxpayerLoanStatus.objects.filter(company_name=company).values()),
    }

    # Create an Excel file with each model as a separate sheet
    with pd.ExcelWriter('exported_data.xlsx', engine='openpyxl') as writer:
        for sheet_name, rows in data.items():
            df = pd.DataFrame(rows)
            df.to_excel(writer, sheet_name=sheet_name, index=False)

    # Send the file as a response
    with open('exported_data.xlsx', 'rb') as excel_file:
        response = HttpResponse(excel_file.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename={company.company_name}_exported_data.xlsx'
    return response


import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render
from .models import Company, PayoutBreakdown, ClientAuditList, TaxpayerLoanStatus

def import_data_from_excel(request):
    if request.method == 'POST' and request.FILES.get('excel_file'):
        # Ensure the user is associated with a company
        if not hasattr(request.user, 'company_profile'):
            return HttpResponse("You are not authorized to import data.", status=403)

        company = request.user.company_profile

        # Read the uploaded Excel file
        excel_file = request.FILES['excel_file']
        data = pd.read_excel(excel_file, sheet_name=None)

        # Process each sheet and import data
        for sheet_name, df in data.items():
            rows = df.to_dict('records')

            # Map sheets to models
            if sheet_name == "PayoutBreakdown":
                PayoutBreakdown.objects.bulk_create(
                    [PayoutBreakdown(**row, company_name=company) for row in rows]
                )
            elif sheet_name == "ClientAuditList":
                ClientAuditList.objects.bulk_create(
                    [ClientAuditList(**row, company_name=company) for row in rows]
                )
            elif sheet_name == "TaxpayerLoanStatus":
                TaxpayerLoanStatus.objects.bulk_create(
                    [TaxpayerLoanStatus(**row, company_name=company) for row in rows]
                )

        return HttpResponse("Data imported successfully!")

    return render(request, "sixthSense/import_export.html")
