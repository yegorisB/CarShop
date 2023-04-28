from django.http import HttpResponse
from django.template import loader
from .models import SUV

def suvs(request):
  mysuvs = SUV.objects.all().values()
  template = loader.get_template('all_suvs.html')
  context = {
    'mysuvs': mysuvs,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mysuv = SUV.objects.get(id=id)
  template = loader.get_template('detailsSUVS.html')
  context = {
    'mysuv': mysuv,
  }
  return HttpResponse(template.render(context, request))




  