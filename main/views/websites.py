from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from main.models import Website

class WebsiteList(ListView):
    model = Website
    context_object_name = 'websites'
    template_name = 'main/website_list.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WebsiteList, self).dispatch(*args, **kwargs)


    def get_queryset(self):
        return Website.objects.filter(owner=self.request.user)


class WebsiteDetails(DetailView):
    model = Website
    context_object_name = 'website'
    template_name = 'main/website_details.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WebsiteDetails, self).dispatch(*args, **kwargs)
