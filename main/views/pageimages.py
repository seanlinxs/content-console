import uuid

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import redirect

from main.models import Page, PageImage
from main.forms import PageImageUploadForm


class PageImageUpload(FormView):
	template_name = 'main/page_image_upload_form.html'
	form_class = PageImageUploadForm


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


