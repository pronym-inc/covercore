from django.conf.urls import url

from covercore.apps.quote.views.general_liability_quote_request.collection import \
    GeneralLiabilityQuoteRequestCollectionApiView
from covercore.apps.quote.views.workers_compensation_quote_request.collection import \
    WorkersCompensationQuoteRequestCollectionApiView

urlpatterns = [
    url(
        r'workers_compensation/$',
        WorkersCompensationQuoteRequestCollectionApiView.as_view(),
        name="workers-compensation-quote-request-collection"
    ),
    url(
        r'general_liability/$',
        GeneralLiabilityQuoteRequestCollectionApiView.as_view(),
        name="general-liability-quote-request-collection"
    )
]

