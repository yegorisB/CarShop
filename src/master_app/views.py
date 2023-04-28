from django.http import HttpResponse
from django.template import loader

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  template = loader.get_template('template.html')
  context = {
    'sedan_cars': ['Ford', 'Toyota', 'Honda'],   
  }
  return HttpResponse(template.render(context, request))