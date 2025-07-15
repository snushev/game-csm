from rest_framework import serializers
from .models import Item, InventoryItem, Transaction
from players.models import Player

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'  
        read_only_fields = ['created_at', 'changed_at']

class InventoryItemSerializer(serializers.ModelSerializer):
    player = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    item = serializers.SlugRelatedField(slug_field='name', queryset=Item.objects.all())

    class Meta:
        model = InventoryItem
        fields = '__all__'
        read_only_fields = ['created_at', 'changed_at']

class TransactionSerializer(serializers.ModelSerializer):
    from_player = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    to_player = serializers.SlugRelatedField(slug_field='username', queryset=Player.objects.all())
    item = serializers.SlugRelatedField(slug_field='name', queryset=Item.objects.all())

    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ['created_at', 'changed_at']