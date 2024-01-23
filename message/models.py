from django.db import models
from django.contrib.auth import get_user_model
from chat.models import Chat
from django.utils import timezone

# Create your models here.

User = get_user_model()


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    text = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"message by {self.user} - {self.date}"
