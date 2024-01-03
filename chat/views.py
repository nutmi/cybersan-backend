from django.shortcuts import render
from rest_framework import mixins, viewsets
from .models import Chat
from .serializers import HomeSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication

# Create your views here.


class ChatViewSet(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    serializer_class = HomeSerializer
    queryset = Chat.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = "id"
