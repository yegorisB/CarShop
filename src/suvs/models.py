from django.db import models

class SUV(models.Model):
  suv_make = models.CharField(max_length=255)
  suv_model = models.CharField(max_length=255)
  milage = models.IntegerField(null=True)
  release = models.IntegerField(null=True)
  color = models.CharField(max_length=30, default='white')
  image = models.ImageField(null=True, blank=True, upload_to="imagesSUV/")
  caption = models.CharField(max_length=255, default='No video')
  video = models.FileField(null=True, blank=True, upload_to="videoSUV/")
  def __str__(self):
    return f"{self.suv_make} {self.suv_model}"