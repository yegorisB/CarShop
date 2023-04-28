from django.db import models

class Sedan_car(models.Model):
  car_make = models.CharField(max_length=255)
  car_model = models.CharField(max_length=255)
  milage = models.IntegerField(null=True)
  release = models.IntegerField(null=True)
  color = models.CharField(max_length=30, default='white')
  image = models.ImageField(null=True, blank=True, upload_to="imagesSEDAN/")
  caption = models.CharField(max_length=255, default='No video')
  video = models.FileField(null=True, blank=True, upload_to="videoSEDAN/")
  def __str__(self):
    return f"{self.car_make} {self.car_model}"