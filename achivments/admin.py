from django.contrib import admin
from .models import Achievement, UserAchievement

# Register your models here.
admin.site.register(Achievement)
admin.site.register(UserAchievement)
