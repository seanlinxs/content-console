from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from main.models import Website, Page


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


    def get_context_data(self, **kwargs):
        context = super(WebsiteDetails, self).get_context_data(**kwargs)
        context['pages'] = Page.objects.filter(site=self.object)
        return context


class WebsiteCreate(CreateView):
    model = Website
    fields = ['name']
    success_url = reverse_lazy('main:website_list')


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WebsiteCreate, self).dispatch(*args, **kwargs)


    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(WebsiteCreate, self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super(WebsiteCreate, self).get_context_data(**kwargs)
        context['title'] = 'Create new website'
        return context


class WebsiteUpdate(UpdateView):
    model = Website
    fields = ['name']
    success_url = reverse_lazy('main:website_list')


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WebsiteUpdate, self).dispatch(*args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(WebsiteUpdate, self).get_context_data(**kwargs)
        context['title'] = 'Edit website'
        return context


class WebsiteDelete(DeleteView):
    model = Website
    success_url = reverse_lazy('main:website_list')


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(WebsiteDelete, self).dispatch(*args, **kwargs)