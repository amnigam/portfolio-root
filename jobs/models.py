from django.db import models

# Create your models here.
#models is imported. But to allow the use of python objects we need to import Model from models.
class Jobs(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
