from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User
User = settings.AUTH_USER_MODEL

class Message(models.Model):
    author = models.ForeignKey(User, related_name='author_name', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_30_mesages(self):
        return Message.objects.oredr_by('-timestamp').all()[:30]    