from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from main.models import Website, Page


class PageCreate(CreateView):
    model = Page
    fields = ['name', 'title', 'heading']


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PageCreate, self).dispatch(*args, **kwargs)


    def form_valid(self, form):
        form.instance.site = Website.objects.get(pk=self.kwargs.get('site_id'))

        return super(PageCreate, self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super(PageCreate, self).get_context_data(**kwargs)
        context['title'] = 'Create new page'
        context['site_id'] = self.kwargs.get('site_id')

        return context


    def get_success_url(self, **kwargs):
        return reverse_lazy('main:website_details', kwargs={'pk':self.kwargs.get('site_id')})


class PageDetails(DetailView):
    model = Page
    context_object_name = 'page'
    template_name = 'main/page_details.html'


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PageDetails, self).dispatch(*args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(PageDetails, self).get_context_data(**kwargs)
        context['textblocks'] = self.object.textblock_set.all()
        context['pageimages'] = self.object.pageimage_set.all()
        context['videolinks'] = self.object.videolink_set.all()

        return context


class PageUpdate(UpdateView):
    model = Page
    fields = ['name', 'title', 'heading']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PageUpdate, self).dispatch(*args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(PageUpdate, self).get_context_data(**kwargs)
        context['title'] = 'Edit page'
        context['site_id'] = self.kwargs.get('site_id')

        return context


    def get_success_url(self, **kwargs):
        return reverse_lazy('main:website_details', kwargs={'pk':self.kwargs.get('site_id')})


class PageDelete(DeleteView):
    model = Page


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PageDelete, self).dispatch(*args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(PageDelete, self).get_context_data(**kwargs)
        context['site_id'] = self.kwargs.get('site_id')

        return context


    def get_success_url(self, **kwargs):
        return reverse_lazy('main:website_details', kwargs={'pk':self.kwargs.get('site_id')})
