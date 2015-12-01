from django.conf.urls import url
from main.views.websites import WebsiteList, WebsiteDetails

urlpatterns = [
    url(r'^websites/$', WebsiteList.as_view(), name='website_list'),
    url(r'^websites/(?P<pk>\d+)/$', WebsiteDetails.as_view(), name='website_details'),
]