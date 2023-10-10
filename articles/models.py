from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone 

# Create your models here.


class Article(models.Model):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published")
    )

    title = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    body = models.TextField(max_length=5000)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField (get_user_model(), related_name="articles")

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="Draft")

    def total_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title[:35]
