from django.db import models


class GeneralLiabilityQuoteRequest(models.Model):
    api_account = models.ForeignKey(
        'pronym_api.ApiAccount',
        on_delete=models.CASCADE,
        related_name='general_liability_quote_requests',
        editable=False,
        null=True
    )
    commercial_name = models.CharField(max_length=255)
    communications_contact_name = models.CharField(max_length=255)
    communications_phone_number = models.CharField(max_length=255)
    communications_email = models.CharField(max_length=255)
    mailing_address1 = models.CharField(max_length=255)
    mailing_address2 = models.CharField(max_length=255, blank=True, null=True)
    mailing_city = models.CharField(max_length=255)
    mailing_state = models.CharField(max_length=255)
    mailing_zip = models.CharField(max_length=255)
    location_address1 = models.CharField(max_length=255)
    location_address2 = models.CharField(max_length=255, blank=True, null=True)
    location_city = models.CharField(max_length=255)
    location_state = models.CharField(max_length=255)
    location_zip = models.CharField(max_length=255)
    number_of_employees = models.PositiveIntegerField()
    total_employee_payroll = models.PositiveIntegerField()
    number_of_owners = models.PositiveIntegerField()
    legal_entity_code = models.CharField(max_length=255)
    spectrum_class_code = models.CharField(max_length=255)
    effective_date = models.DateField()
    business_start_year = models.PositiveIntegerField()
    bop_type_code = models.CharField(max_length=255)
    annual_sales = models.PositiveIntegerField()

    quote_received = models.BooleanField(default=False, editable=False)
    premium = models.PositiveIntegerField(null=True, blank=True)
