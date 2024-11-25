# sixthSense/urls.py
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView

from .views import import_data_from_excel
from django.urls import path
from .views import (
    dashboard, company_report, edit_company, delete_company, export_data_to_excel, edit_preparer_inline,
    preparer_report, edit_preparer, delete_preparer,company_details,preparer_details, preparer_profile,
     register_client,client_list,edit_client,delete_client,partnership_payroll_report,taxpayer_audit_report,taxpayer_loan_report,
    client_details,create_audit, audit_list, audit_detail, delete_audit,edit_audit,index, register_preparer,login_company,login_preparer,
    create_loan_status, loan_status_report, edit_loan_status, delete_loan_status,loan_status_detail,register_company,
    preparer_dashboard,company_dashboard,logout_view # Ensure this is included
)

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', company_dashboard, name='company_dashboard'),  # Use specific name
    path('companies/', company_report, name='company_report'),
    path('companies/edit/<int:pk>/', edit_company, name='edit_company'),
    path('companies/delete/<int:pk>/', delete_company, name='delete_company'),
    path('preparers/', preparer_report, name='preparer_report'),
    path('profile/edit/', edit_preparer, name='edit_preparer'),
    path('preparers/delete/<int:pk>/', delete_preparer, name='delete_preparer'),
    path('companies/<int:pk>/', company_details, name='company_details'),
    path('preparers/<int:preparer_id>/', preparer_details, name='preparer_details'),
    path('clients/register/', register_client, name='register_client'),
    path('clients/', client_list, name='client_list'),
    path('clients/edit/<int:client_id>/', edit_client, name='edit_client'),
    path('clients/delete/<int:client_id>/', delete_client, name='delete_client'),
    path('clients/<int:client_id>/', client_details, name='client_details'),
    path('audits/create/', create_audit, name='create_audit'),
    path('audits/', audit_list, name='audit_list'),
    path('audits/<int:pk>/', audit_detail, name='audit_detail'),
    path('audits/delete/<int:pk>/', delete_audit, name='delete_audit'),
    path('audits/edit/<int:pk>/', edit_audit, name='edit_audit'),
    path('loan-status/create/', create_loan_status, name='create_loan_status'),
    path('loan-status/', loan_status_report, name='loan_status_report'),
    path('loan-status/edit/<int:pk>/', edit_loan_status, name='edit_loan_status'),
    path('loan-status/delete/<int:pk>/', delete_loan_status, name='delete_loan_status'),
    path('loan-status/<int:pk>/', loan_status_detail, name='loan_status_detail'),
    path('preparer-dashboard/', preparer_dashboard, name='preparer_dashboard'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),  # Dashboard redirect
    path('company-dashboard/', company_dashboard, name='company_dashboard'),  # Company Dashboard
    path('preparer_dashboard/', preparer_dashboard, name='preparer_dashboard'),  # Preparer Dashboard
    path('logout/', logout_view, name='logout'),
    path('register/company/', register_company, name='register_company'),  # Company Register
    path( 'register/preparer/', register_preparer, name='register_preparer'),  # Preparer Register
    path('login/company/', login_company, name='login_company'),  # Company Login
    path('login/preparer/', login_preparer, name='login_preparer'),  # Preparer Login
    path('preparer/partnership_payroll/', partnership_payroll_report, name ='partnership_payroll_report'),
    path('preparer/taxpayer_audit_report/', taxpayer_audit_report, name='taxpayer_audit_report'),
    path ('preparer/taxpayer_loan_report', taxpayer_loan_report, name= 'taxpayer_loan_report'),
    path ('prepare/profile', preparer_profile, name= 'preparer_profile'),path('password/change/', PasswordChangeView.as_view(
        template_name='sixthSense/password_change.html',
        success_url='/password/change/done/'  # Redirect after success
    ), name='password_change'),

    path('password/change/done/', PasswordChangeDoneView.as_view(
        template_name='sixthSense/password_change_done.html'
    ), name='password_change_done'),
    path('export/excel/', export_data_to_excel, name='export_data_to_excel'),
    path('import/excel/', import_data_from_excel, name='import_data_to_excel'),
    path('preparer/edit/<int:pk>/', edit_preparer_inline, name='edit_preparer_inline'),




]

