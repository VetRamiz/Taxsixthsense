# sixthSense/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Preparer, Company
from .forms import PreparerForm, CompanyForm

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
from django.shortcuts import render, get_object_or_404
from .models import Company

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

# Preparer views
from django.shortcuts import render, redirect
from .forms import PreparerForm

def register_preparer(request):
    if request.method == 'POST':
        form = PreparerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('preparer_report')  # Change to your success URL
    else:
        form = PreparerForm()
    
    return render(request, 'sixthSense/register_preparer.html', {'form': form})

def preparer_report(request):
    preparers = Preparer.objects.all()
    return render(request, 'sixthSense/preparer_report.html', {'preparers': preparers})

def edit_preparer(request, pk):
    preparer = get_object_or_404(Preparer, pk=pk)
    if request.method == 'POST':
        form = PreparerForm(request.POST, instance=preparer)
        if form.is_valid():
            form.save()
            return redirect('preparer_report')
    else:
        form = PreparerForm(instance=preparer)

    return render(request, 'sixthSense/edit_preparer.html', {'form': form, 'preparer': preparer})

def delete_preparer(request, pk):
    preparer = get_object_or_404(Preparer, pk=pk)
    preparer.delete()
    return redirect('preparer_report')
# sixthSense/views.py

from django.shortcuts import render, redirect
from .models import Company
from .forms import CompanyForm

def register_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('company_report')  # Adjust as needed
    else:
        form = CompanyForm()
    
    return render(request, 'sixthSense/register_company.html', {'form': form})

# sixthSense/views.py

from django.shortcuts import render, get_object_or_404
from .models import Preparer

def preparer_details(request, preparer_id):
    preparer = get_object_or_404(Preparer, id=preparer_id)
    return render(request, 'sixthSense/preparer_details.html', {'preparer': preparer})

# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Client
from .forms import ClientForm  # Ensure you have a form for the Client model

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
from django.shortcuts import render, redirect, get_object_or_404
from .models import ClientAuditList
from .forms import ClientAuditListForm

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

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Company, Preparer
from .forms import CompanyLoginForm, PreparerLoginForm

def login_view(request):
    if request.method == 'POST':
        login_type = request.POST.get('login_type')  # 'company' or 'preparer'
        
        if login_type == 'company':
            form = CompanyLoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                try:
                    company = Company.objects.get(email=email, password=password)
                    # Perform company login actions
                    request.session['user_type'] = 'company'
                    request.session['user_id'] = company.id
                    return redirect('company_dashboard')
                except Company.DoesNotExist:
                    messages.error(request, "Invalid company login credentials.")
        elif login_type == 'preparer':
            form = PreparerLoginForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                try:
                    preparer = Preparer.objects.get(email=email, password=password)
                    # Perform preparer login actions
                    request.session['user_type'] = 'preparer'
                    request.session['user_id'] = preparer.id
                    return redirect('preparer_dashboard')
                except Preparer.DoesNotExist:
                    messages.error(request, "Invalid preparer login credentials.")
    else:
        company_form = CompanyLoginForm()
        preparer_form = PreparerLoginForm()
        return render(request, 'sixthSense/login.html', {
            'company_form': company_form,
            'preparer_form': preparer_form
        })
