from django.db import models

# Create your models here.


class Chat(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    image = models.ImageField(null=True)

    def __str__(self) -> str:
        return self.name
