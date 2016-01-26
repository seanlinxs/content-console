from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from main.models import Page, Paragraph


class ParagraphCreate(CreateView):
    model = Paragraph
    fields = ['name', 'markdown', 'display_order']


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ParagraphCreate, self).dispatch(*args, **kwargs)


    def form_valid(self, form):
        form.instance.page = Page.objects.get(pk=self.kwargs.get('page_id'))

        return super(ParagraphCreate, self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super(ParagraphCreate, self).get_context_data(**kwargs)
        context['title'] = 'Create new paragraph'
        context['site_id'] = self.kwargs.get('site_id')
        context['page_id'] = self.kwargs.get('page_id')

        return context


    def get_success_url(self, **kwargs):
        return reverse_lazy('main:page_details', kwargs={'site_id':self.kwargs.get('site_id'), 'pk':self.kwargs.get('page_id')})


class ParagraphDetails(DetailView):
    model = Paragraph
    template_name = 'main/paragraph_details.html'


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ParagraphDetails, self).dispatch(*args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(ParagraphDetails, self).get_context_data(**kwargs)
        context['paragraphimages'] = self.object.paragraphimage_set.all()
        context['paragraphvideos'] = self.object.paragraphvideo_set.all()

        return context


class ParagraphUpdate(UpdateView):
    model = Paragraph
    fields = ['name', 'markdown', 'display_order']


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ParagraphUpdate, self).dispatch(*args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(ParagraphUpdate, self).get_context_data(**kwargs)
        context['title'] = 'Edit paragraph'
        context['site_id'] = self.kwargs.get('site_id')
        context['page_id'] = self.kwargs.get('page_id')

        return context


    def get_success_url(self, **kwargs):
        return reverse_lazy('main:page_details', kwargs={'site_id':self.kwargs.get('site_id'), 'pk':self.kwargs.get('page_id')})


class ParagraphDelete(DeleteView):
    model = Paragraph


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ParagraphDelete, self).dispatch(*args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(ParagraphDelete, self).get_context_data(**kwargs)
        context['site_id'] = self.kwargs.get('site_id')
        context['page_id'] = self.kwargs.get('page_id')
        
        return context


    def get_success_url(self, **kwargs):
        return reverse_lazy('main:page_details', kwargs={'site_id':self.kwargs.get('site_id'), 'pk':self.kwargs.get('page_id')})
