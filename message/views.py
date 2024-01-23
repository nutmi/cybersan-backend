from django.shortcuts import render
from rest_framework import mixins, viewsets, pagination
from rest_framework.authentication import TokenAuthentication
from .models import Message
from .serializers import MessageSerializer
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    AllowAny,
    IsAuthenticated,
)
from rest_framework.pagination import LimitOffsetPagination


class CustomPagination(pagination.PageNumberPagination):
    page_size = 15  # Set your desired page size here
    page_size_query_param = "page_size"
    max_page_size = 100


class MessageViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
    serializer_class = MessageSerializer
    lookup_field = "id"

    def get_permissions(self):
        if self.action == "list":
            return [AllowAny()]
        elif self.action == "create":
            return [IsAuthenticated()]
        return super().get_permissions()

    def get_queryset(self):
        self.pagination_class = CustomPagination
        chatid = self.request.query_params.get("chatid")
        return Message.objects.filter(chat=chatid).order_by("-date")
