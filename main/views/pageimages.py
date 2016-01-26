import uuid

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect

from main.models import Page, PageImage


class PageImageUpload(CreateView):
    model = PageImage
    fields = ['name', 'image']


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PageImageUpload, self).dispatch(*args, **kwargs)
    

    def form_valid(self, form):
        page_image = PageImage(image=form.cleaned_data.get('image'))
        page_image.page = Page.objects.get(pk=self.kwargs.get('page_id'))
        page_image.name = form.cleaned_data.get('name')
        page_image.save()

        return redirect(self.get_success_url())


    def get_context_data(self, **kwargs):
        context = super(PageImageUpload, self).get_context_data(**kwargs)
        context['title'] = 'Upload page image'
        context['site_id'] = self.kwargs.get('site_id')
        context['page_id'] = self.kwargs.get('page_id')
        
        return context


    def get_success_url(self, **kwargs):
        return reverse_lazy('main:page_details', kwargs={'site_id':self.kwargs.get('site_id'), 'pk':self.kwargs.get('page_id')})


class PageImageUpdate(UpdateView):
    model = PageImage
    fields = ['name', 'image']

    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PageImageUpdate, self).dispatch(*args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(PageImageUpdate, self).get_context_data(**kwargs)
        context['title'] = 'Edit page image'
        context['site_id'] = self.kwargs.get('site_id')
        context['page_id'] = self.kwargs.get('page_id')

        return context


    def get_success_url(self, **kwargs):
        return reverse_lazy('main:page_details', kwargs={'site_id':self.kwargs.get('site_id'), 'pk':self.kwargs.get('page_id')})


class PageImageDelete(DeleteView):
    model = PageImage


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(PageImageDelete, self).dispatch(*args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(PageImageDelete, self).get_context_data(**kwargs)
        context['title'] = 'Confirm delete page image'
        context['site_id'] = self.kwargs.get('site_id')
        context['page_id'] = self.kwargs.get('page_id')

        return context


    def get_success_url(self, **kwargs):
        return reverse_lazy('main:page_details', kwargs={'site_id':self.kwargs.get('site_id'), 'pk':self.kwargs.get('page_id')})
