from .models import User
from rest_framework import serializers
from achivments.serializers import UserAchievementSerializer


class CustomUserSerializer(serializers.ModelSerializer):
    achievements = UserAchievementSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "email",
            "description",
            "amountOfMessages",
            "id",
            "achievements",
            "terminalName",
        ]
