
from django.urls import path
from . import views

urlpatterns = [   
    path('sedan_cars/', views.sedan_cars, name='sedan_cars'),
    path('sedan_cars/details/<int:id>', views.details, name='details'),
   
]