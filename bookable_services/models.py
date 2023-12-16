# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone

# class Service(models.Model):
#     name = models.CharField(max_length=200)
#     image1 = models.ImageField(upload_to='service_images/', blank=True, null=True)
#     image2 = models.ImageField(upload_to='service_images/', blank=True, null=True)
#     description = models.TextField()
#     key_features = models.TextField(help_text="Enter key features separated by commas")
#     price = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return self.name

#     def get_key_features_list(self):
#         return self.key_features.split(',')


# class ServiceSlot(models.Model):
#     service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
#     max_participants = models.IntegerField(default=1)
#     current_participants = models.IntegerField(default=0)

#     def is_full(self):
#         return self.current_participants >= self.max_participants

#     def __str__(self):
#         return f"{self.service.name} ({self.start_time} - {self.end_time})"


# class Booking(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     service_slot = models.ForeignKey(ServiceSlot, on_delete=models.CASCADE, null=True)
#     booking_date = models.DateTimeField(default=timezone.now)
#     STATUS_CHOICES = [
#         ('pending', 'Pending'),
#         ('confirmed', 'Confirmed'),
#         ('cancelled', 'Cancelled'),
#     ]
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

#     def __str__(self):
#         return f"{self.user.username}'s booking for {self.service.name}"

#     def save(self, *args, **kwargs):
#         # Add any custom save logic here
#         super().save(*args, **kwargs)

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

    def __str__(self):
        return f"{self.service.name} at { self.place.name } ({self.start_time} - {self.end_time})"



class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE, null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    booking_date = models.DateTimeField(default=timezone.now)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    
    def __str__(self):
        return f"Booking {self.id} by {self.user}"