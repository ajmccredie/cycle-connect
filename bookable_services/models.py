from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

#Geographical placement for the bookings matters
class Place(models.Model):
    name = models.CharField(max_length=25)
    further_description = models.TextField()

    def __str__(self):
        return self.name


#Set up and management of the bookable timeslots
class Slot(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    max_people = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.place.name} {self.start_time} - {self.end_time}"


#Set up the admin side to add the details to the services available
class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10)
    regions = models.ManyToManyFields(Place)
    description = models.TextField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    booking_date = models.DateTimeField
    status = models.CharField(max_length=10)

    class Meta:
        full_booking = ('user', 'slot')
    
    def __str__(self):
        return f"Booking {self.id} by {self.user}"
