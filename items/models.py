from django.db import models
from players.models import Player

# Create your models here.

class Item(models.Model):
    CHOICES = (
        ('common', 'Common'),
        ('rare', 'Rare'),
        ('epic', 'Epic'),
        ('legendary', 'Legendary')
    )
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=200)
    rarity = models.CharField(max_length=15, choices=CHOICES)
    price = models.PositiveIntegerField()
    image = models.ImageField(
        upload_to='items/',
        null=True,
        blank=True,
        )
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.get_rarity_display()} {self.name}"

class InventoryItem(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='inventory_items')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='inventory_instances')
    quantity = models.PositiveIntegerField()
    equipped = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.player.nickname}'s {self.item.name} (x{self.quantity})"

class Transaction(models.Model):
    from_player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='outgoing_transactions')
    to_player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='incoming_transactions')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='transactions')
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Transaction #{self.id}: {self.item.name} (x{self.quantity})"