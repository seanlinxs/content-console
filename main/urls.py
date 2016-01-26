from django.conf.urls import url
from main.views.websites import WebsiteList, WebsiteDetails, WebsiteCreate, WebsiteUpdate, WebsiteDelete
from main.views.pages import PageCreate, PageDetails, PageUpdate, PageDelete
from main.views.textblocks import TextBlockCreate, TextBlockUpdate, TextBlockDelete
from main.views.pageimages import PageImageUpload, PageImageUpdate, PageImageDelete
from main.views.videolinks import VideoLinkCreate, VideoLinkUpdate, VideoLinkDelete
from main.views.news import NewsCreate, NewsUpdate, NewsDelete
from main.views.paragraphs import ParagraphCreate, ParagraphDetails, ParagraphUpdate, ParagraphDelete
from main.views.paragraphimages import ParagraphImageUpload, ParagraphImageUpdate, ParagraphImageDelete
from main.views.paragraphvideos import ParagraphVideoCreate, ParagraphVideoUpdate, ParagraphVideoDelete

urlpatterns = [
    # Website
    url(r'^websites/$', WebsiteList.as_view(), name='website_list'),
    url(r'^websites/add/$', WebsiteCreate.as_view(), name='website_create'),
    url(r'^websites/(?P<pk>\d+)/$', WebsiteDetails.as_view(), name='website_details'),
    url(r'^websites/(?P<pk>\d+)/update/$', WebsiteUpdate.as_view(), name='website_update'),
    url(r'^websites/(?P<pk>\d+)/delete/$', WebsiteDelete.as_view(), name='website_delete'),
    # Page
    url(r'^websites/(?P<site_id>\d+)/pages/add/$', PageCreate.as_view(), name='page_create'),
    url(r'^websites/(?P<site_id>\d+)/pages/(?P<pk>\d+)/$', PageDetails.as_view(), name='page_details'),
    url(r'^websites/(?P<site_id>\d+)/pages/(?P<pk>\d+)/update/$', PageUpdate.as_view(), name='page_update'),
    url(r'^websites/(?P<site_id>\d+)/pages/(?P<pk>\d+)/delete/$', PageDelete.as_view(), name='page_delete'),
    # TextBlock
    url(r'^websites/(?P<site_id>\d+)/pages/(?P<page_id>\d+)/textblocks/add/$', TextBlockCreate.as_view(), name='textblock_create'),
    url(r'^websites/(?P<site_id>\d+)/pages/(?P<page_id>\d+)/textblocks/(?P<pk>\d+)/update/$', TextBlockUpdate.as_view(), name='textblock_update'),
    url(r'^websites/(?P<site_id>\d+)/pages/(?P<page_id>\d+)/textblocks/(?P<pk>\d+)/delete/$', TextBlockDelete.as_view(), name='textblock_delete'),
    # PageImage
    url(r'^websites/(?P<site_id>\d+)/pages/(?P<page_id>\d+)/pageimages/upload/$', PageImageUpload.as_view(), name='pageimage_upload'),
    url(r'^websites/(?P<site_id>\d+)/pages/(?P<page_id>\d+)/pageimages/(?P<pk>\d+)/update/$', PageImageUpdate.as_view(), name='pageimage_update'),
    url(r'^websites/(?P<site_id>\d+)/pages/(?P<page_id>\d+)/pageimages/(?P<pk>\d+)/delete/$', PageImageDelete.as_view(), name='pageimage_delete'),
    # VideoLink
    url(r'^websites/(?P<site_id>\d+)/pages/(?P<page_id>\d+)/videolinks/add/$', VideoLinkCreate.as_view(), name='videolink_create'),
    url(r'^websites/(?P<site_id>\d+)/pages/(?P<page_id>\d+)/videolinks/(?P<pk>\d+)/update/$', VideoLinkUpdate.as_view(), name='videolink_update'),
    url(r'^websites/(?P<site_id>\d+)/pages/(?P<page_id>\d+)/videolinks/(?P<pk>\d+)/delete/$', VideoLinkDelete.as_view(), name='videolink_delete'),
    # News
    url(r'^websites/(?P<site_id>\d+)/news/add/$', NewsCreate.as_view(), name='news_create'),
    url(r'^websites/(?P<site_id>\d+)/news/(?P<pk>\d+)/update/$', NewsUpdate.as_view(), name='news_update'),
    url(r'^websites/(?P<site_id>\d+)/news/(?P<pk>\d+)/delete/$', NewsDelete.as_view(), name='news_delete'),
    # Paragraph
    url(r'^websites/(?P<site_id>\d+)/pages/(?P<page_id>\d+)/paragraphs/add/$', ParagraphCreate.as_view(), name='paragraph_create'),
    url(r'^websites/(?P<site_id>\d+)/pages/(?P<page_id>\d+)/paragraphs/(?P<pk>\d+)/details/$', ParagraphDetails.as_view(), name='paragraph_details'),
    url(r'^websites/(?P<site_id>\d+)/pages/(?P<page_id>\d+)/paragraphs/(?P<pk>\d+)/update/$', ParagraphUpdate.as_view(), name='paragraph_update'),
    url(r'^websites/(?P<site_id>\d+)/pages/(?P<page_id>\d+)/paragraphs/(?P<pk>\d+)/delete/$', ParagraphDelete.as_view(), name='paragraph_delete'),
    # ParagraphImage
    url(r'^websites/(?P<site_id>\d+)/pages/(?P<page_id>\d+)/paragraphs/(?P<paragraph_id>\d+)/paragraphimages/add/$', ParagraphImageUpload.as_view(), name='paragraphimage_upload'),
    url(r'^websites/(?P<site_id>\d+)/pages/(?P<page_id>\d+)/paragraphs/(?P<paragraph_id>\d+)/paragraphimages/(?P<pk>\d+)/update/$', ParagraphImageUpdate.as_view(), name='paragraphimage_update'),
    url(r'^websites/(?P<site_id>\d+)/pages/(?P<page_id>\d+)/paragraphs/(?P<paragraph_id>\d+)/paragraphimages/(?P<pk>\d+)/delete/$', ParagraphImageDelete.as_view(), name='paragraphimage_delete'),
    # ParagraphVideo
    url(r'^websites/(?P<site_id>\d+)/pages/(?P<page_id>\d+)/paragraphs/(?P<paragraph_id>\d+)/paragraphvideos/add/$', ParagraphVideoCreate.as_view(), name='paragraphvideo_create'),
    url(r'^websites/(?P<site_id>\d+)/pages/(?P<page_id>\d+)/paragraphs/(?P<paragraph_id>\d+)/paragraphvideos/(?P<pk>\d+)/update/$', ParagraphVideoUpdate.as_view(), name='paragraphvideo_update'),
    url(r'^websites/(?P<site_id>\d+)/pages/(?P<page_id>\d+)/paragraphs/(?P<paragraph_id>\d+)/paragraphvideos/(?P<pk>\d+)/delete/$', ParagraphVideoDelete.as_view(), name='paragraphvideo_delete'),
]
