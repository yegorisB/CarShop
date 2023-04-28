from django.http import HttpResponse
from django.template import loader
from .models import Sedan_car

def sedan_cars(request):
  mysedan_cars = Sedan_car.objects.all().values()
  template = loader.get_template('all_sedan_cars.html')
  context = {
    'mysedan_cars': mysedan_cars,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mysedan_car = Sedan_car.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mysedan_car': mysedan_car,
  }
  return HttpResponse(template.render(context, request))
