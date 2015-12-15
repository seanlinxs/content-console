import uuid

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, FormView
from django.core.urlresolvers import reverse_lazy

from main.models import Website, News
from main.forms import NewsForm


class NewsCreate(FormView):
    template_name = 'main/news_form.html'
    form_class = NewsForm


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NewsCreate, self).dispatch(*args, **kwargs)


    def form_valid(self, form):
        news = News(title=form.cleaned_data.get('title'), content=form.cleaned_data.get('content'), image=form.cleaned_data.get('image'))
        news.site = Website.objects.get(pk=self.kwargs.get('site_id'))
        news.save()

        return super(NewsCreate, self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super(NewsCreate, self).get_context_data(**kwargs)
        context['title'] = 'Create news'
        context['site_id'] = self.kwargs.get('site_id')

        return context


    def get_success_url(self, **kwargs):
        return reverse_lazy('main:website_details', kwargs={'pk':self.kwargs.get('site_id')})


class NewsUpdate(UpdateView):
    model = News
    fields = ['title', 'content', 'image']

    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NewsUpdate, self).dispatch(*args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(NewsUpdate, self).get_context_data(**kwargs)
        context['title'] = 'Edit news'
        context['site_id'] = self.kwargs.get('site_id')

        return context


    def get_success_url(self, **kwargs):
        return reverse_lazy('main:website_details', kwargs={'pk':self.kwargs.get('site_id')})


class NewsDelete(DeleteView):
    model = News


    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NewsDelete, self).dispatch(*args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(NewsDelete, self).get_context_data(**kwargs)
        context['site_id'] = self.kwargs.get('site_id')

        return context


    def get_success_url(self, **kwargs):
        return reverse_lazy('main:website_details', kwargs={'pk':self.kwargs.get('site_id')})