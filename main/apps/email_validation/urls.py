from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^email$', views.create),
    url(r'^success$', views.success),
    url(r'^email/(?P<id>[0-9]*)/delete', views.destroy),
]
