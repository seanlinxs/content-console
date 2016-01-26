from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from main.models import Page, VideoLink


class VideoLinkCreate(CreateView):
    model = VideoLink
    fields = ['name', 'link']


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(VideoLinkCreate, self).dispatch(*args, **kwargs)


    def form_valid(self, form):
        form.instance.page = Page.objects.get(pk=self.kwargs.get('page_id'))

        return super(VideoLinkCreate, self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super(VideoLinkCreate, self).get_context_data(**kwargs)
        context['title'] = 'Create new video link'
        context['site_id'] = self.kwargs.get('site_id')
        context['page_id'] = self.kwargs.get('page_id')

        return context


    def get_success_url(self, **kwargs):
        return reverse_lazy('main:page_details', kwargs={'site_id':self.kwargs.get('site_id'), 'pk':self.kwargs.get('page_id')})


class VideoLinkUpdate(UpdateView):
    model = VideoLink
    fields = ['name', 'link']


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(VideoLinkUpdate, self).dispatch(*args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(VideoLinkUpdate, self).get_context_data(**kwargs)
        context['title'] = 'Edit video link'
        context['site_id'] = self.kwargs.get('site_id')
        context['page_id'] = self.kwargs.get('page_id')

        return context


    def get_success_url(self, **kwargs):
        return reverse_lazy('main:page_details', kwargs={'site_id':self.kwargs.get('site_id'), 'pk':self.kwargs.get('page_id')})


class VideoLinkDelete(DeleteView):
    model = VideoLink


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(VideoLinkDelete, self).dispatch(*args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(VideoLinkDelete, self).get_context_data(**kwargs)
        context['title'] = 'Confirm delete video link'
        context['site_id'] = self.kwargs.get('site_id')
        context['page_id'] = self.kwargs.get('page_id')
        
        return context


    def get_success_url(self, **kwargs):
        return reverse_lazy('main:page_details', kwargs={'site_id':self.kwargs.get('site_id'), 'pk':self.kwargs.get('page_id')})
