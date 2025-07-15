from django.db import models
from items.models import Item
from players.models import Player

# Create your models here.

class Quest(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=200)
    required_level = models.PositiveIntegerField(default=1)
    reward_gold = models.PositiveIntegerField()
    is_active = models.BooleanField(default=False)
    reward_items = models.ManyToManyField(Item, related_name='reward_items')
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
     
class QuestProgress(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='quest_players')
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='quests_progress')
    is_completed = models.BooleanField(default=False)
    notes = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.player.nickname}'s {self.quest.title}"

    