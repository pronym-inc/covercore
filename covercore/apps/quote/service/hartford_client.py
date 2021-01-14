from typing import Optional

from django.conf import settings
from hartford_client.client import HartfordClient, HartfordConfiguration, HartfordWorkersCompensationResponse, \
    HartfordWorkersCompensationQuoteRequest
from hartford_client.models.general_liability import (
    HartfordGeneralLiabilityResponse, HartfordGeneralLiabilityRequest, HartfordGeneralLiabilityLocation)
from hartford_client.models.workers_compensation import HartfordWorkersCompensationLocation

from covercore.apps.quote.models import WorkersCompensationQuoteRequest, GeneralLiabilityQuoteRequest


class CoverCoreHartfordClient:
    def __init__(self):
        self._configuration = HartfordConfiguration(
            use_qa=True,
            api_username=settings.HARTFORD_API_USERNAME,
            api_password=settings.HARTFORD_API_PASSWORD,
            client_id=settings.HARTFORD_CLIENT_ID,
            producer_code=settings.HARTFORD_PRODUCER_CODE,
            client_secret=settings.HARTFORD_CLIENT_SECRET
        )
        self._client = HartfordClient(self._configuration)

    def send_general_liability_quote_request(
            self,
            quote_request: GeneralLiabilityQuoteRequest
    ) -> Optional[HartfordGeneralLiabilityResponse]:
        request = HartfordGeneralLiabilityRequest(
            commercial_name=quote_request.commercial_name,
            communications_contact_name=quote_request.communications_contact_name,
            communications_phone_number=quote_request.communications_phone_number,
            communications_email=quote_request.communications_email,
            mailing_address1=quote_request.mailing_address1,
            mailing_address2=quote_request.mailing_address2,
            mailing_city=quote_request.mailing_city,
            mailing_state=quote_request.mailing_state,
            mailing_zip=quote_request.mailing_zip,
            locations=[
                HartfordGeneralLiabilityLocation(
                    address1=quote_request.location_address1,
                    address2=quote_request.location_address2,
                    city=quote_request.location_city,
                    state=quote_request.location_state,
                    zip=quote_request.location_zip
                )
            ],
            legal_entity_code=quote_request.legal_entity_code,
            spectrum_class_code=quote_request.spectrum_class_code,
            effective_date=quote_request.effective_date,
            business_start_year=quote_request.business_start_year,
            number_of_employees=quote_request.number_of_employees,
            number_of_owners=quote_request.number_of_owners,
            total_employee_payroll=quote_request.total_employee_payroll,
            bop_type_code=quote_request.bop_type_code,
            annual_sales=quote_request.annual_sales
        )
        response = self._client.make_general_liability_quote(request)

        if response is not None:
            quote_request.quote_received = True
            quote_request.premium = response.total_premium
            quote_request.save()

        return response

    def send_workers_compensation_quote_request(
            self,
            quote_request: WorkersCompensationQuoteRequest
    ) -> Optional[HartfordWorkersCompensationResponse]:
        request = HartfordWorkersCompensationQuoteRequest(
            commercial_name=quote_request.commercial_name,
            communications_contact_name=quote_request.communications_contact_name,
            communications_phone_number=quote_request.communications_phone_number,
            communications_email=quote_request.communications_email,
            mailing_address1=quote_request.mailing_address1,
            mailing_address2=quote_request.mailing_address2,
            mailing_city=quote_request.mailing_city,
            mailing_state=quote_request.mailing_state,
            mailing_zip=quote_request.mailing_zip,
            locations=[
                HartfordWorkersCompensationLocation(
                    address1=quote_request.location_address1,
                    address2=quote_request.location_address2,
                    city=quote_request.location_city,
                    state=quote_request.location_state,
                    zip=quote_request.location_zip,
                    number_of_employees=quote_request.number_of_employees,
                    number_of_owners=quote_request.number_of_owners,
                    annual_employee_payroll=quote_request.annual_employee_payroll,
                    annual_owners_payroll=quote_request.annual_owners_payroll
                )
            ],
            legal_entity_code=quote_request.legal_entity_code,
            spectrum_class_code=quote_request.spectrum_class_code,
            effective_date=quote_request.effective_date,
            business_start_year=quote_request.business_start_year
        )
        response = self._client.make_workers_compensation_quote(request)

        if response is not None:
            quote_request.quote_received = True
            quote_request.premium = response.total_premium
            quote_request.save()

        return response
