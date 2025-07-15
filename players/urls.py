from rest_framework.routers import DefaultRouter
from .views import PlayerViewSet, GuildViewSet, ReportViewSet

router = DefaultRouter()

router.register(r'player', PlayerViewSet, basename='players')
router.register(r'guild', GuildViewSet, basename='guilds')
router.register(r'report', ReportViewSet, basename='reports')

urlpatterns = [
] + router.urls