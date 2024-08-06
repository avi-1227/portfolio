from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    image =models.ImageField(upload_to ='portfolio/images/')
    url = models.URLField(blank=True)



