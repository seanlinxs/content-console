from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from main.models import Website, Page, TextBlock


class TextBlockCreate(CreateView):
	model = TextBlock
	fields = ['name', 'content']


	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(TextBlockCreate, self).dispatch(*args, **kwargs)


	def form_valid(self, form):
		form.instance.page = Page.objects.get(pk=self.kwargs.get('page_id'))
		return super(TextBlockCreate, self).form_valid(form)


	def get_context_data(self, **kwargs):
		context = super(TextBlockCreate, self).get_context_data(**kwargs)
		context['title'] = 'Create new text block'
		context['site_id'] = self.kwargs.get('site_id')
		context['page_id'] = self.kwargs.get('page_id')
		return context


	def get_success_url(self, **kwargs):
		return reverse_lazy('main:page_details', kwargs={'site_id':self.kwargs.get('site_id'), 'pk':self.kwargs.get('page_id')})


class TextBlockUpdate(UpdateView):
	model = TextBlock
	fields = ['name', 'content']


	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super(TextBlockUpdate, self).dispatch(*args, **kwargs)


	def get_context_data(self, **kwargs):
		context = super(TextBlockUpdate, self).get_context_data(**kwargs)
		context['title'] = 'Edit text block'
		context['site_id'] = self.kwargs.get('site_id')
		context['page_id'] = self.kwargs.get('page_id')
		return context


	def get_success_url(self, **kwargs):
		return reverse_lazy('main:page_details', kwargs={'site_id':self.kwargs.get('site_id'), 'pk':self.kwargs.get('page_id')})
