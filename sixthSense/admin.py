# sixthSense/admin.py

from django.contrib import admin
from .models import Company, Preparer, Client, ClientAuditList, PayoutBreakdown, TaxpayerLoanStatus, WebReportTaxesToGo, WebReports

admin.site.register(Company)
admin.site.register(Preparer)
admin.site.register(Client)
admin.site.register(ClientAuditList)
admin.site.register(PayoutBreakdown)
admin.site.register(TaxpayerLoanStatus)
admin.site.register(WebReportTaxesToGo)
admin.site.register(WebReports)