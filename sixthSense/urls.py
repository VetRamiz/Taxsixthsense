# sixthSense/urls.py

from django.urls import path
from .views import (
    dashboard, company_report, edit_company, delete_company,
    register_preparer, preparer_report, edit_preparer, delete_preparer,company_details,preparer_details,
    register_company, register_client,client_list,edit_client,delete_client,
    client_details,create_audit, audit_list, audit_detail, delete_audit,edit_audit,
    create_loan_status, loan_status_report, edit_loan_status, delete_loan_status,loan_status_detail  # Ensure this is included
)

urlpatterns = [
    path('', dashboard, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('companies/', company_report, name='company_report'),
    path('companies/edit/<int:pk>/', edit_company, name='edit_company'),
    path('companies/delete/<int:pk>/', delete_company, name='delete_company'),
    path('companies/register/', register_company, name='register_company'),  # Ensure this line exists
    path('preparers/register/', register_preparer, name='register_preparer'),
    path('preparers/', preparer_report, name='preparer_report'),
    path('preparers/edit/<int:pk>/', edit_preparer, name='edit_preparer'),
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
    path('loan-status/<int:pk>/', loan_status_detail, name='loan_status_detail'),]