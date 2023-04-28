from django.db import models

class TRUCK(models.Model):
  truck_make = models.CharField(max_length=255)
  truck_model = models.CharField(max_length=255)
  milage = models.IntegerField(null=True)
  release = models.IntegerField(null=True)
  color = models.CharField(max_length=30, default='white')
  image = models.ImageField(null=True, blank=True, upload_to="imagesTRUCK/")
  caption = models.CharField(max_length=255, default='No video')
  video = models.FileField(null=True, blank=True, upload_to="videoTRUCK/")
  def __str__(self):
    return f"{self.truck_make} {self.truck_model}"