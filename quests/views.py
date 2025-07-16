from rest_framework import viewsets
from .models import Quest, QuestProgress
from .serializers import QuestSerializer, QuestProgressSerializer
from core.permissions import IsAdminOrReadOnly, IsOwnerOrAdmin
from drf_spectacular.utils import extend_schema

@extend_schema(
    description='Quests management API (Admin only).',
    tags=['Quests'],
)
class QuestViewSet(viewsets.ModelViewSet):

    queryset = Quest.objects.all()
    serializer_class = QuestSerializer
    permission_classes = [IsAdminOrReadOnly]

    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'title', 'required_level'] 

@extend_schema(
    description='Player quests progress API. Keep track of player\'s quests',
    tags=['Quest Progress'],
)
class QuestProgressViewSet(viewsets.ModelViewSet):
    queryset = QuestProgress.objects.all()
    serializer_class = QuestProgressSerializer
    permission_classes = [IsOwnerOrAdmin]

    ordering_fields = ['created_at',] 

    def get_queryset(self):
        if self.request.user.is_staff:
            return QuestProgress.objects.all()
        return QuestProgress.objects.filter(player__username=self.request.user)
