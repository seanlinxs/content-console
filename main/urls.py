from django.conf.urls import url
from main.views.websites import WebsiteList, WebsiteDetails, WebsiteCreate, WebsiteUpdate, WebsiteDelete

urlpatterns = [
    url(r'^websites/$', WebsiteList.as_view(), name='website_list'),
    url(r'^websites/add/$', WebsiteCreate.as_view(), name='website_create'),
    url(r'^websites/(?P<pk>\d+)/$', WebsiteUpdate.as_view(), name='website_update'),
    url(r'^websites/(?P<pk>\d+)/delete/$', WebsiteDelete.as_view(), name='website_delete'),
]