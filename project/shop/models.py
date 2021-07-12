from django.db import models


# Create your models here.
class Bd(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(blank=True)
