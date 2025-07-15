from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, InventoryItemViewSet, TransactionViewSet

router = DefaultRouter()

router.register(r'item', ItemViewSet, basename='items')
router.register(r'inventory', InventoryItemViewSet, basename='inventories')
router.register(r'transaction', TransactionViewSet, basename='transactions')

urlpatterns = [
] + router.urls