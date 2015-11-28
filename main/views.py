from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import SiteOwner, Website

# Create your views here.

def owners(request):
    owners = SiteOwner.objects.all()
    context = {'owners': owners}

    return render(request, "main/owners.html", context)


def owner(request, owner_id):
    owner = get_object_or_404(SiteOwner, pk=owner_id)
    context = {'owner': owner}

    return render(request, "main/owner.html", context)


def sites(request, owner_id):
    mysites = SiteOwner.objects.get(id=owner_id).website_set.all()
    resp = ', '.join(s.name for s in mysites)

    return HttpResponse(resp)


def pages(request, site_id):
    return HttpResponse("Pages of site #{0}".format(site_id))


def images(request, site_id, page_id):
    return HttpResponse("Images of site #{0}, page #{1}".format(site_id, page_id))


def create_owner(request):
    owner = SiteOwner(name=request.POST['name'], email=request.POST['email'], phone=request.POST['phone'])
    owner.save()

    return HttpResponseRedirect(reverse('main:owners'))