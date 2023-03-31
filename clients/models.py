from django.db import models
from datetime import datetime

class Clients(models.Model):
   
    property_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    clients_date = models.DateTimeField(default=datetime.now)
    user_id = models.IntegerField(blank=True)
    property = models.CharField(max_length=200)
    def __str__ (self):
        return self.name

# Create your models here.
