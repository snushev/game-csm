from rest_framework import viewsets
from .models import Player, Guild, Report
from .serializers import PlayerSerializer, GuildSerializer, ReportSerializer
from core.permissions import IsPlayerOwnerOrAdmin, IsAdminOrReadOnly, IsGuildLeaderOrAdmin
from rest_framework import permissions
from drf_spectacular.utils import extend_schema

@extend_schema(
    description='Players API. Create and manage Players',
    tags=['Players'],
)
class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [IsPlayerOwnerOrAdmin]

    search_fields = ['username', 'nickname']
    ordering_fields = ['created_at', 'race', 'level'] 

    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return super().get_permissions()

@extend_schema(
    description='Guilds management API. Manage guild owners and members.',
    tags=['Guilds'],
)
class GuildViewSet(viewsets.ModelViewSet):
    queryset = Guild.objects.all()
    serializer_class = GuildSerializer
    permission_classes = [IsGuildLeaderOrAdmin]

    search_fields = ['name', 'leader']
    ordering_fields = ['created_at'] 

    def perform_create(self, serializer):
        player = self.request.user.player
        serializer.save(leader=player, members=[player])

@extend_schema(
    description='Report management API. Report toxic players.',
    tags=['Reports'],
)
class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

    search_fields = ['reporter', 'reported']
    ordering_fields = ['created_at', 'reported'] 