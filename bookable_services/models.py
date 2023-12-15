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
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    max_participants = models.IntegerField(default=1)
    current_participants = models.IntegerField(default=0)

    def is_full(self):
        return self.current_participants >= self.max_participants

    def add_participant(self):
        if not self.is_full():
            self.current_participants += 1
            self.save()

    def remove_participant(self):
        if self.current_participants > 0:
            self.current_participants -= 1
            self.save()


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    booking_date = models.DateTimeField(default=timezone.now)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    
    def save(self, *args, **kwargs):
        creating = self._state.adding
        super().save(*args, **kwargs)
        if creating:
            self.slot.add_participant()
    
    def cancel(self):
        self.status = 'cancelled'
        self.slot.remove_participant()
        self.save()

    def __str__(self):
        return f"Booking {self.id} by {self.user} for {self.slot.service.name}"
