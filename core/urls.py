from rest_framework.routers import DefaultRouter
from .views import NewPostViewSet

router = DefaultRouter()

router.register(r'post', NewPostViewSet, basename='posts')

urlpatterns = [
] + router.urls