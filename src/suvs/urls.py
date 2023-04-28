from django.urls import path
from . import views

urlpatterns = [
    path('suvs/', views.suvs, name='suvs'),
    path('suvs/details/<int:id>', views.details, name='details'),

]