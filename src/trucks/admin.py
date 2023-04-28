from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import TRUCK

# Register your models here.

class TRUCKAdmin(admin.ModelAdmin):
  list_display = ("truck_make", "truck_model", "milage", "release", "color", "image", "caption", "video")
admin.site.register(TRUCK, TRUCKAdmin)
