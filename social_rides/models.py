from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Ride(models.Model):
    organiser = models.ForeignKey(User, on_delete=models.CASCADE, related_name='organised_rides')
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='ride_images/', blank=True, null=True)
    route_description = models.TextField()
    date = models.DateField(default=datetime.date.today)
    start_time = models.TimeField(default=datetime.time(11, 0))
    start_place = models.CharField(max_length=200)
    end_place = models.CharField(max_length=200)
    distance = models.DecimalField(max_digits=5, decimal_places=2)
    BEGINNER = 'BF'
    INTERMEDIATE = 'IN'
    CHALLENGING = 'CH'
    EXPERT = 'EX'
    DIFFICULTY_CHOICES = [
        (BEGINNER, 'Beginner Friendly'),
        (INTERMEDIATE, 'Intermediate'),
        (CHALLENGING, 'Challenging'),
        (EXPERT, 'Seasoned Experts Advised'),
    ]
    difficulty = models.CharField(max_length=2, choices=DIFFICULTY_CHOICES, default=BEGINNER,)
    max_participants = models.PositiveIntegerField(default=10)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class RideOrganiser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    trusted_organiser = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class RideAttendance(models.Model):
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name='attendees')
    participant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='participated_rides')
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.ride.title} - {self.participant.username}"
