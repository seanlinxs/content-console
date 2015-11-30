from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^owners/$', views.owners, name='owners'),
    url(r'^owners/create/$', views.create_owner, name="create_owner"),
    url(r'^owners/(?P<owner_id>[0-9]+)/$', views.owner, name='owner'),
    url(r'^owners/(?P<owner_id>[0-9]+)/sites/$', views.sites, name='sites'),
    url(r'^owners/(?P<owner_id>[0-9]+)/sites/(?P<site_id>[0-9]+)/pages/$', views.pages, name='pages'),
    url(r'^owners/(?P<owner_id>[0-9]+)/sites/(?P<site_id>[0-9]+)/pages/(?P<page_id>[0-9]+)/images/', views.images, name='images'),
]