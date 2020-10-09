from django.conf.urls import url
from pronym_api.api.get_token import GetTokenApiView

urlpatterns = [
    url(r'^get_token/$', GetTokenApiView.as_view(), name="get_token")
]