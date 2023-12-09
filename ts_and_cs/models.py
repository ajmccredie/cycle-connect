from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserVerified(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_verified')
    agreed_to_terms = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username