from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.views import serve
from django.urls import re_path, include

admin.autodiscover()


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',
        include(
            ('covercore.apps.core.urls',
             'covercore.apps.core'),
            namespace='core')),
]

if settings.DEBUG_STATIC_FILES:
    urlpatterns += [re_path(r'^devstatic/(?P<path>.*)$', serve)]
