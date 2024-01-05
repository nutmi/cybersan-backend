from rest_framework import serializers
from .models import Message
from core.serializers import CustomUserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class MessageSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="user.username", read_only=True)
    whos_message = serializers.SerializerMethodField()
    user_display = CustomUserSerializer(source="user", read_only=True)

    class Meta:
        model = Message
        fields = ["user", "chat", "text", "name", "id", "whos_message", "user_display"]
        read_only_fields = ["id", "user_display"]

    def create(self, validated_data):
        # Extract the user from the validated data
        user = validated_data.get("user")
        print(user)

        # Create the message

        message = Message.objects.create(**validated_data)

        # Increment the amountOfMessages for the user
        if user:
            if user.amountOfMessages >= 100:
                user.achievements.create(achivment_id=1)
            elif user.amountOfMessages >= 500:
                user.achievements.create(achivment_id=2)

            print("yes")
            user.amountOfMessages += 1  # Adjust the field name
            user.save()

        return message

    def get_whos_message(self, obj):
        request = self.context.get("request")
        if request:
            user_message = obj.user
            user_current = request.user
            if user_message == user_current:
                return True
            return
