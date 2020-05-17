from django.db import models
from django.contrib.auth.models import User

class Poll(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=140)
    description = models.TextField(max_length=300)
    asked = models.DateTimeField(auto_now=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=300)
    votes = models.IntegerField(default=0)

class Comment(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    comment_text = models.TextField(max_length=500)
    date_commented = models.DateTimeField(auto_now=True)


