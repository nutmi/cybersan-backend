from rest_framework import routers
from .views import ChatViewSet

router = routers.SimpleRouter()
router.register(r"chat", ChatViewSet, basename="chat")
urlpatterns = router.urls
urlpatterns += []