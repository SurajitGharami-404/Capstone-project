from django.db import models

# Create your models here.

class Menu(models.Model):
    menu_id = models.AutoField
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self) -> str:
        return self.title


class Booking(models.Model):
    booking_id = models.AutoField
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.name