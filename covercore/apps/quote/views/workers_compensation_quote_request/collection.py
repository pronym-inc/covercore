from typing import Type, Dict, Any, Optional

from django.db.models import QuerySet
from pronym_api.models import ApiAccountMember
from pronym_api.views.actions import ResourceAction
from pronym_api.views.api_view import HttpMethod
from pronym_api.views.model_view.actions.create import CreateModelResourceAction
from pronym_api.views.model_view.modelform import LazyModelForm
from pronym_api.views.model_view.views import ModelCollectionApiView

from covercore.apps.quote.models import WorkersCompensationQuoteRequest
from covercore.apps.quote.service.hartford_client import CoverCoreHartfordClient


class CreateWorkersCompensationQuoteRequestResourceAction(CreateModelResourceAction[WorkersCompensationQuoteRequest]):

    def _save_form(self, form: LazyModelForm, request: Dict[str, Any], account_member: Optional[ApiAccountMember],
                   resource: WorkersCompensationQuoteRequest) -> WorkersCompensationQuoteRequest:
        obj = super()._save_form(form, request, account_member, resource)
        if account_member is not None:
            obj.api_account = account_member.api_account
        obj.save()
        service = CoverCoreHartfordClient()
        service.send_workers_compensation_quote_request(obj)
        return obj


class WorkersCompensationQuoteRequestCollectionApiView(ModelCollectionApiView[WorkersCompensationQuoteRequest]):
    require_authentication = True

    def _get_action_configuration(self) -> Dict[HttpMethod, ResourceAction]:
        config = super()._get_action_configuration()
        config[HttpMethod.POST] = CreateWorkersCompensationQuoteRequestResourceAction(self._get_model())
        return config

    def _get_model(self) -> Type[WorkersCompensationQuoteRequest]:
        return WorkersCompensationQuoteRequest

    def _get_queryset(self) -> 'QuerySet[WorkersCompensationQuoteRequest]':
        return self.authenticated_account_member.api_account.workers_compensation_quote_requests.all()
