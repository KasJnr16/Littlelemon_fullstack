from django.db import models

# Create your models here
class MenuAPI(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField() 
    table_number = models.IntegerField() 
    booking_date = models.DateTimeField()

class BookingAPI(models.Model):
    title = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    inventory = models.IntegerField()  