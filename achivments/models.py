from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Achievement(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name


class UserAchievement(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="achievements"
    )
    achivment = models.ForeignKey(Achievement, on_delete=models.CASCADE)
