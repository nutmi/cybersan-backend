from rest_framework import routers
from .views import MessageViewSet

router = routers.SimpleRouter()
router.register(r"message", MessageViewSet, basename="message")
urlpatterns = router.urls
urlpatterns += []