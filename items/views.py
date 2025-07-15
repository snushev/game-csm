from rest_framework import viewsets
from .models import Item, InventoryItem, Transaction
from .serializers import ItemSerializer, InventoryItemSerializer, TransactionSerializer
from core.permissions import IsOwnerOrAdmin, IsAdminOrReadOnly
from drf_spectacular.utils import extend_schema

@extend_schema(
    description='Items API (Admin only). Manages game items.',
    tags=['Items'],
)
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAdminOrReadOnly]

    search_fields = ['name', 'description']
    ordering_fields = ['created_at', 'name'] 

@extend_schema(
    description='User Inventory API. Players can manage their items.',
    tags=['Inventory'],
)
class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [IsOwnerOrAdmin]

    ordering_fields = ['created_at', 'quantity'] 

    def get_queryset(self):
        if self.request.user.is_staff:
            return InventoryItem.objects.all()
        return InventoryItem.objects.filter(player__username=self.request.user)

@extend_schema(
    description='Player transactions API. Tracks item exchanges.',
    tags=['Transactions'],
)
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsOwnerOrAdmin]

    ordering_fields = ['created_at', ] 

    def get_queryset(self):
        if self.request.user.is_staff:
            return Transaction.objects.all()
        return Transaction.objects.filter(from_player__username=self.request.user)
