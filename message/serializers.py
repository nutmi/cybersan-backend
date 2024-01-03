from rest_framework import serializers
from .models import Message
from core.serializers import CustomUserSerializer


class MessageSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="user.username", read_only=True)
    whos_message = serializers.SerializerMethodField()
    user_display = CustomUserSerializer(source="user", read_only=True)

    class Meta:
        model = Message
        fields = ["user", "chat", "text", "name", "id", "whos_message", "user_display"]
        read_only_fields = ["id", "user_display"]

    def get_whos_message(self, obj):
        request = self.context.get("request")
        if request:
            user_message = obj.user
            user_current = request.user
            if user_message == user_current:
                return True
            return False
