from django.contrib import admin
from .models import SUV

# Register your models here.

class SUVAdmin(admin.ModelAdmin):
  list_display = ("suv_make", "suv_model", "milage", "release", "color", "image", "caption", "video")
admin.site.register(SUV, SUVAdmin)
