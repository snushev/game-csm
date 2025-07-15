from rest_framework.routers import DefaultRouter
from .views import  QuestViewSet, QuestProgressViewSet

router = DefaultRouter()

router.register(r'quest', QuestViewSet, basename='quests')
router.register(r'progress', QuestProgressViewSet, basename='progress')

urlpatterns = [
] + router.urls