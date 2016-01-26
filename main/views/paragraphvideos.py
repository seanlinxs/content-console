from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from main.models import Paragraph, ParagraphVideo


class ParagraphVideoCreate(CreateView):
    model = ParagraphVideo
    fields = ['name', 'link', 'layout']


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ParagraphVideoCreate, self).dispatch(*args, **kwargs)


    def form_valid(self, form):
        form.instance.paragraph = Paragraph.objects.get(pk=self.kwargs.get('paragraph_id'))

        return super(ParagraphVideoCreate, self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super(ParagraphVideoCreate, self).get_context_data(**kwargs)
        context['title'] = 'Create paragraph video'
        context['site_id'] = self.kwargs.get('site_id')
        context['page_id'] = self.kwargs.get('page_id')
        context['paragraph_id'] = self.kwargs.get('paragraph_id')

        return context


    def get_success_url(self, **kwargs):
        return reverse_lazy('main:paragraph_details', kwargs={'site_id':self.kwargs.get('site_id'), 'page_id':self.kwargs.get('page_id'), 'pk':self.kwargs.get('paragraph_id')})


class ParagraphVideoUpdate(UpdateView):
    model = ParagraphVideo
    fields = ['name', 'link', 'layout']


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ParagraphVideoUpdate, self).dispatch(*args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(ParagraphVideoUpdate, self).get_context_data(**kwargs)
        context['title'] = 'Edit video link'
        context['site_id'] = self.kwargs.get('site_id')
        context['page_id'] = self.kwargs.get('page_id')
        context['paragraph_id'] = self.kwargs.get('paragraph_id')

        return context


    def get_success_url(self, **kwargs):
        return reverse_lazy('main:paragraph_details', kwargs={'site_id':self.kwargs.get('site_id'), 'page_id':self.kwargs.get('page_id'), 'pk':self.kwargs.get('paragraph_id')})


class ParagraphVideoDelete(DeleteView):
    model = ParagraphVideo


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ParagraphVideoDelete, self).dispatch(*args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(ParagraphVideoDelete, self).get_context_data(**kwargs)
        context['site_id'] = self.kwargs.get('site_id')
        context['page_id'] = self.kwargs.get('page_id')
        context['paragraph_id'] = self.kwargs.get('paragraph_id')
        
        return context


    def get_success_url(self, **kwargs):
        return reverse_lazy('main:paragraph_details', kwargs={'site_id':self.kwargs.get('site_id'), 'page_id':self.kwargs.get('page_id'), 'pk':self.kwargs.get('paragraph_id')})
