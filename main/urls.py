from django.conf.urls import url
from main.views.websites import WebsiteList, WebsiteDetails, WebsiteCreate, WebsiteUpdate, WebsiteDelete
from main.views.pages import PageCreate, PageDetails, PageUpdate, PageDelete
from main.views.textblocks import TextBlockCreate, TextBlockUpdate, TextBlockDelete
from main.views.pageimages import PageImageUpload, PageImageUpdate, PageImageDelete
from main.views.news import NewsCreate, NewsUpdate, NewsDelete

urlpatterns = [
    url(r'^websites/$', WebsiteList.as_view(), name='website_list'),
    url(r'^websites/add/$', WebsiteCreate.as_view(), name='website_create'),
    url(r'^websites/(?P<pk>\d+)/$', WebsiteDetails.as_view(), name='website_details'),
    url(r'^websites/(?P<pk>\d+)/update/$', WebsiteUpdate.as_view(), name='website_update'),
    url(r'^websites/(?P<pk>\d+)/delete/$', WebsiteDelete.as_view(), name='website_delete'),
    url(r'^websites/(?P<site_id>\d+)/pages/add/$', PageCreate.as_view(), name='page_create'),
    url(r'^websites/(?P<site_id>\d+)/pages/(?P<pk>\d+)/$', PageDetails.as_view(), name='page_details'),
    url(r'^websites/(?P<site_id>\d+)/pages/(?P<pk>\d+)/update/$', PageUpdate.as_view(), name='page_update'),
    url(r'^websites/(?P<site_id>\d+)/pages/(?P<pk>\d+)/delete/$', PageDelete.as_view(), name='page_delete'),
    url(r'^websites/(?P<site_id>\d+)/pages/(?P<page_id>\d+)/textblocks/add/$', TextBlockCreate.as_view(), name='textblock_create'),
    url(r'^websites/(?P<site_id>\d+)/pages/(?P<page_id>\d+)/textblocks/(?P<pk>\d+)/update/$', TextBlockUpdate.as_view(), name='textblock_update'),
    url(r'^websites/(?P<site_id>\d+)/pages/(?P<page_id>\d+)/textblocks/(?P<pk>\d+)/delete/$', TextBlockDelete.as_view(), name='textblock_delete'),
    url(r'^websites/(?P<site_id>\d+)/pages/(?P<page_id>\d+)/pageimages/upload/$', PageImageUpload.as_view(), name='pageimage_upload'),
    url(r'^websites/(?P<site_id>\d+)/pages/(?P<page_id>\d+)/pageimages/(?P<pk>\d+)/update/$', PageImageUpdate.as_view(), name='pageimage_update'),
    url(r'^websites/(?P<site_id>\d+)/pages/(?P<page_id>\d+)/pageimages/(?P<pk>\d+)/delete/$', PageImageDelete.as_view(), name='pageimage_delete'),
    url(r'^websites/(?P<site_id>\d+)/news/add/$', NewsCreate.as_view(), name='news_create'),
    url(r'^websites/(?P<site_id>\d+)/news/(?P<pk>\d+)/update/$', NewsUpdate.as_view(), name='news_update'),
    url(r'^websites/(?P<site_id>\d+)/news/(?P<pk>\d+)/delete/$', NewsDelete.as_view(), name='news_delete'),
]