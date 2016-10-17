

from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^studies/', include('studies.urls')),
]


admin.site.site_header = 'Field Poetics'
