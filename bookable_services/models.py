from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

#Geographical placement for the bookings matters
class Place(models.Model):
    name = models.CharField(max_length=25)
    further_description = models.TextField()

    def __str__(self):
        return self.name


#Set up the admin side to add the details to the services available
class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0.0)
    regions = models.ManyToManyField(Place)
    description_summary = models.TextField(default='No summary available.')
    description_detail_bullets = models.TextField(default='Details not provided.')

    def __str__(self):
        return self.name


#Set up and management of the bookable timeslots
class Slot(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    max_people = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            for _ in range(self.max_people):
                new_individual_slot = IndividualSlot.objects.create(slot=self)

    def __str__(self):
        return f"{self.service.name} at { self.place.name } ({self.start_time} - {self.end_time})"


class IndividualSlot(models.Model):
    slot = models.ForeignKey(Slot, related_name='individual_slots', on_delete=models.CASCADE)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"Place in {self.slot} - {'Booked' if self.is_booked else 'Available'}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    individual_slot = models.ForeignKey(IndividualSlot, on_delete=models.CASCADE, null=True)
    booking_date = models.DateTimeField(default=timezone.now)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    
    def __str__(self):
        return f"Booking {self.id} by {self.user} for {self.slot.service.name}"
