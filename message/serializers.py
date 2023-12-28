from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="user.username", read_only=True)
    whos_message = serializers.SerializerMethodField()
    class Meta:
        model = Message
        fields = ["user", "chat", "text", "name", "id", "whos_message"]
        read_only_fields = ["id"]

    def get_whos_message(self, obj):
        request = self.context.get("request")
        if request:
            user_message = obj.user
            user_current = request.user
            if user_message == user_current:
                return True
            return False