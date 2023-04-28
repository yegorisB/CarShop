from django.contrib import admin
from .models import Sedan_car

# Register your models here.

class Sedan_carAdmin(admin.ModelAdmin):
  list_display = ("car_make", "car_model", "milage", "release", "color", "image", "caption", "video")
  
admin.site.register(Sedan_car, Sedan_carAdmin)