from django.http import HttpResponse
from django.template import loader
from .models import TRUCK

def trucks(request):
  mytrucks = TRUCK.objects.all().values()
  template = loader.get_template('all_trucks.html')
  context = {
    'mytrucks': mytrucks,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mytruck = TRUCK.objects.get(id=id)
  template = loader.get_template('detailsTRUCKS.html')
  context = {
    'mytruck': mytruck,
  }
  return HttpResponse(template.render(context, request))




  