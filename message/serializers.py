from rest_framework import serializers
from .models import Message
from core.serializers import CustomUserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class MessageSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(source="user.username", read_only=True)
    whos_message = serializers.SerializerMethodField()
    user_display = CustomUserSerializer(source="user", read_only=True)

    class Meta:
        model = Message
        fields = ["user", "chat", "text", "censured_text", "id", "whos_message", "user_display"]
        read_only_fields = ["id", "user_display"]


    def create(self, validated_data):

        user = validated_data.get("user")
        forbidden_words = ['cherry', 'naruto', 'jjk']

        text = validated_data['text']
        censured_text = validated_data["censured_text"]

        new_message = [
            '*' * len(word) if word in forbidden_words else word
            for word in text.split()
        ]
        
        validated_data['censured_text'] = ' '.join(new_message)

        if user:
            if user.amountOfMessages >= 100:
                user.achievements.create(achivment_id=1)
            elif user.amountOfMessages >= 500:
                user.achievements.create(achivment_id=2)
            user.amountOfMessages += 1  # Adjust the field name
            user.save()

        message = Message.objects.create(**validated_data)

        return message

    def get_whos_message(self, obj):
        request = self.context.get("request")
        if request:
            user_message = obj.user
            user_current = request.user
            if user_message == user_current:
                return True
            return
