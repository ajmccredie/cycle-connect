from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

APPROVED = ((0, "Draft"), (1, "Published"))
choice = 0

class TradingPost(models.Model):
    CATEGORY_CHOICES = [
        ("clothing", "Clothing"),
        ("bike_part", "Bike Part"),
        ("bike_accessory", "Bike Accessory"),
        ("other", "Other"),
        ("all", "All"),
    ]

    CONDITION_CHOICES = [
    ("new", "New"),
    ("tired", "Tired"),
    ("like_new", "Like New"),
    ("used", "Used"),
    ("all", "All"),
    ]

    STATUS_CHOICES = [
    ("available", "Available"),
    ("sold", "Sold"),
    ]

    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=False)
    description = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image', default='placeholder')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    condition = models.CharField(max_length=50, choices=CONDITION_CHOICES, default='other')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='available')
    approved = models.IntegerField(choice=STATUS, default=0)

    class Meta:
        ordering=['-created_on']

    def __str__(self):
        return self.title

    def number_of_interests(self):
        return self.likes.count()

