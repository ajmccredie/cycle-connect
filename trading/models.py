from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

APPROVED = ((0, "Draft"), (1, "Published"))

# Data model of trading posts
class TradingPost(models.Model):
    CATEGORY_CHOICES = [
        ("clothing", "Clothing"),
        ("bike_part", "Bike Part"),
        ("bike_accessory", "Bike Accessory"),
        ("other", "Other"),
    ]

    CONDITION_CHOICES = [
    ("new", "New"),
    ("tired", "Tired"),
    ("like_new", "Like New"),
    ("used", "Used"),
    ]

    STATUS_CHOICES = [
    ("available", "Available"),
    ("sold", "Sold"),
    ]

    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=False, null=False)
    description = models.TextField(max_length=750, null=False)
    created_on = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image', default='trading_placeholder', blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    condition = models.CharField(max_length=50, choices=CONDITION_CHOICES, default='other')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='available')
    approved = models.IntegerField(choices=APPROVED, default=0)

    class Meta:
        ordering=['-created_on']

    def __str__(self):
        return self.title


# Data model of conversation
class TradingConversation(models.Model):
    post = models.ForeignKey(TradingPost, on_delete=models.CASCADE, related_name='conversations')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='selling_conversations')
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='buying_conversations')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Conversation about {self.post.title} between {self.seller} and {self.buyer}'


# Data model of message
class Message(models.Model):
    conversation = models.ForeignKey(TradingConversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    text = models.TextField(max_length=500, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.sender.username} at {self.created_at}'

