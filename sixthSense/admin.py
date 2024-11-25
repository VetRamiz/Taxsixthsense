# sixthSense/admin.py

from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Company,Preparer, Client, ClientAuditList, PayoutBreakdown, TaxpayerLoanStatus, WebReportTaxesToGo, WebReports

admin.site.register(Company)
admin.site.register(Preparer)
admin.site.register(Client)
admin.site.register(ClientAuditList)
admin.site.register(PayoutBreakdown)
admin.site.register(TaxpayerLoanStatus)
admin.site.register(WebReportTaxesToGo)
admin.site.register(WebReports)

company_group, _ = Group.objects.get_or_create(name='Company')
preparer_group, _ = Group.objects.get_or_create(name='Preparer')




