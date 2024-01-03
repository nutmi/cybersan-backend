from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from .models import Message
from .serializers import MessageSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class MessageViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
    serializer_class = MessageSerializer
    lookup_field = "id"
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        chatid = self.request.query_params.get("chatid")
        return Message.objects.filter(chat=chatid)
