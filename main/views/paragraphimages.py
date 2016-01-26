import uuid

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect

from main.models import Paragraph, ParagraphImage


class ParagraphImageUpload(CreateView):
    model = ParagraphImage
    fields = ['name', 'image', 'layout']


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ParagraphImageUpload, self).dispatch(*args, **kwargs)
    

    def form_valid(self, form):
        form.instance.paragraph = Paragraph.objects.get(pk=self.kwargs.get('paragraph_id'))

        return super(ParagraphImageUpload, self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super(ParagraphImageUpload, self).get_context_data(**kwargs)
        context['title'] = 'Upload paragraph image'
        context['site_id'] = self.kwargs.get('site_id')
        context['page_id'] = self.kwargs.get('page_id')
        context['paragraph_id'] = self.kwargs.get('paragraph_id')
        
        return context


    def get_success_url(self, **kwargs):
        return reverse_lazy('main:paragraph_details', kwargs={'site_id':self.kwargs.get('site_id'), 'page_id':self.kwargs.get('page_id'), 'pk':self.kwargs.get('paragraph_id')})


class ParagraphImageUpdate(UpdateView):
    model = ParagraphImage
    fields = ['name', 'image', 'layout']

    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ParagraphImageUpdate, self).dispatch(*args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(ParagraphImageUpdate, self).get_context_data(**kwargs)
        context['title'] = 'Edit page image'
        context['site_id'] = self.kwargs.get('site_id')
        context['page_id'] = self.kwargs.get('page_id')
        context['paragraph_id'] = self.kwargs.get('paragraph_id')

        return context


    def get_success_url(self, **kwargs):
        return reverse_lazy('main:paragraph_details', kwargs={'site_id':self.kwargs.get('site_id'), 'page_id':self.kwargs.get('page_id'), 'pk':self.kwargs.get('paragraph_id')})


class ParagraphImageDelete(DeleteView):
    model = ParagraphImage


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ParagraphImageDelete, self).dispatch(*args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(ParagraphImageDelete, self).get_context_data(**kwargs)
        context['title'] = "Confirm delete paragraph image"
        context['site_id'] = self.kwargs.get('site_id')
        context['page_id'] = self.kwargs.get('page_id')
        context['paragraph_id'] = self.kwargs.get('paragraph_id')

        return context


    def get_success_url(self, **kwargs):
        return reverse_lazy('main:paragraph_details', kwargs={'site_id':self.kwargs.get('site_id'), 'page_id':self.kwargs.get('page_id'), 'pk':self.kwargs.get('paragraph_id')})
