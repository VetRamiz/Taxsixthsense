from django.db.models import Case, When, IntegerField, Sum, Count

from .models import ClientAuditList, PayoutBreakdown , TaxpayerLoanStatus

def get_audit_data(company_id, selected_year=None):
    audit_queryset = ClientAuditList.objects.filter(company_name_id=company_id)

    if selected_year:
        audit_queryset = audit_queryset.filter(year=selected_year)

    audit_queryset = audit_queryset.annotate(
        total_missing=(
            Case(When(identification_drivers_license=False, then=1), default=0, output_field=IntegerField()) +
            Case(When(social_security_card=False, then=1), default=0, output_field=IntegerField()) +
            Case(When(healthcare1095_form=False, then=1), default=0, output_field=IntegerField()) +
            Case(When(w2=False, then=1), default=0, output_field=IntegerField()) +
            Case(When(self_employment_log=False, then=1), default=0, output_field=IntegerField())
            # Add all other fields similarly...
        )
    )

    return {
        "total_clients": audit_queryset.count(),
        "total_missing_docs": audit_queryset.filter(total_missing__gt=0).count(),
        "percentage_missing": (audit_queryset.filter(total_missing__gt=0).count() / audit_queryset.count() * 100) if audit_queryset.count() else 0,
    }

def get_payout_data(company_id, selected_year=None):
    payout_queryset = PayoutBreakdown.objects.filter(company_name_id=company_id)

    if selected_year:
        payout_queryset = payout_queryset.filter(year=selected_year)

    return {
        "total_customers": payout_queryset.aggregate(total_customers=Count("taxpayer_first_name"))["total_customers"],
        "total_prep_fee": payout_queryset.aggregate(total_fee=Sum("total_prep_fee_charged"))["total_fee"] or 0,
        "total_payout": payout_queryset.aggregate(total_payout=Sum("payout"))["total_payout"] or 0,
    }

def get_loan_data(company_id, selected_year=None):
    loan_queryset = TaxpayerLoanStatus.objects.filter(company_name_id=company_id)

    if selected_year:
        loan_queryset = loan_queryset.filter(year=selected_year)

    return {
        "clients_with_loans": loan_queryset.aggregate(total_loans=Count("advance_amount"))["total_loans"] or 0,
        "total_loan_amount": loan_queryset.aggregate(total_loan=Sum("advance_amount"))["total_loan"] or 0,
        "total_marketing_fee": loan_queryset.aggregate(total_marketing_fee=Sum("marketing_fee"))["total_marketing_fee"] or 0,
    }

from django.db.models import Sum

def get_partnership_payroll_data(preparer_id, selected_year=None):
    # Filter based on the preparer
    queryset = PayoutBreakdown.objects.filter(preparer_id=preparer_id)

    # Filter by year if provided
    if selected_year:
        queryset = queryset.filter(year=selected_year)

    # Aggregate the necessary fields
    payroll_data = queryset.aggregate(
        total_prep_fee_charged=Sum("total_prep_fee_charged"),
        fees_intercepted=Sum("fees_intercepted"),
        total_prep_fee_deposited=Sum("total_prep_fee_deposited"),
        partnership_remaining_balance=Sum("partnership_remaining_balance"),
        advance_loan_fees=Sum("advance_loan_fees"),
        sum_total_preparer=Sum("sum_total_preparer"),
        split=Sum("split"),
        payout=Sum("payout"),
        prior_week_hold=Sum("prior_week_hold"),
        current_week_hold=Sum("current_week_hold"),
        total_hold=Sum("total_hold"),
        release_hold_amt=Sum("release_hold_amt"),
    )

    return payroll_data
