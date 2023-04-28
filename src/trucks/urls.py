from django.urls import path
from . import views

urlpatterns = [
    path('trucks/', views.trucks, name='trucks'),
    path('trucks/details/<int:id>', views.details, name='details'),

]