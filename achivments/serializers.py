from rest_framework import serializers
from .models import UserAchievement, Achievement


class AchievementSerializers(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = "__all__"


class UserAchievementSerializer(serializers.ModelSerializer):
    achivment = AchievementSerializers(read_only=True)

    class Meta:
        model = UserAchievement
        fields = ["achivment"]
