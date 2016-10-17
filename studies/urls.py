

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<slug>[-\w]*)/$', views.text, name='text'),
]
