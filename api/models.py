from django.db import models

# Create your models here.

class trips(models.Model):
    region=models.CharField(max_length=50)
    origin_coord=models.CharField(max_length=200)
    destination_coord=models.CharField(max_length=200)
    datetime=models.DateTimeField()
    datasource=models.CharField(max_length=50)


class load_trips(models.Model):
    region=models.CharField(max_length=50)
    origin_coord=models.CharField(max_length=200)
    destination_coord=models.CharField(max_length=200)
    datetime=models.DateTimeField()
    datasource=models.CharField(max_length=50)