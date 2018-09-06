from django.db import models

# Create your models here.
class Data(models.Model):
    first_field = models.CharField(max_length=200)
    second_field = models.CharField(max_length=200)
    third_field = models.CharField(max_length=200)
    fourth_field = models.CharField(max_length=200)
