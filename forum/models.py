from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class ForumPost(models.Model):
    UserId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=False)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    image = CloudinaryField('image', default='placeholder')
    published_status = models.IntegerField(choice=STATUS, default=1)
    reported_status = models.IntegerField(choice=STATUS, default=0)
    reported_by = models.Manager(User, related_name='reported_posts', blank=True)
    likes = models.ManyToManyField(User, related_name="likes", blank=True)

    class Meta:
        ordering=['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def number_of_comments(self):
        return self.comments.count()


class Comment(models.Model):
    post = models.ForeignKey(ForumPost, on_delete=models.CASCADE, related_name='comments')
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
    
    def __str__(self):
        return f"Comment {self.body} by {self.name}"

