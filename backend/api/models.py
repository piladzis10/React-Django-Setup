from django.db import models

class RentForm(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    date = models.DateField()
    
