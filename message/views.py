from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from .models import Message
from .serializers import MessageSerializer

class MessageViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = MessageSerializer
    lookup_field = "id"

    def get_queryset(self):
        chat_id = self.request.query_params.get("chat_id")
        return Message.objects.filter(chat=chat_id)