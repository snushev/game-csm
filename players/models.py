from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Player(models.Model):
    RACE_CHOICES = (
        ("Human", "Human"),
        ("Orc", "Orc"),
        ("Elf", "Elf"),
        ("Dwarf", "Dwarf"),
        ("Troll", "Troll")
    )
    username = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    nickname = models.CharField(max_length=100, unique=True)
    race = models.CharField(max_length=10, choices=RACE_CHOICES)
    level = models.PositiveIntegerField(default=1)
    xp = models.PositiveIntegerField(default=0)
    gold = models.PositiveIntegerField(default=0)
    is_banned = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"The {self.race} {self.nickname} is lvl {self.level}. "

    
class Guild(models.Model):
    name = models.CharField(max_length=100)
    leader = models.ForeignKey(Player, on_delete=models.SET_NULL, null=True, related_name='leader')
    members = models.ManyToManyField(Player, related_name='guilds')
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Guild {self.name} with leader {self.leader}" if self.leader else f"Guild {self.name}"

class Report(models.Model):
    reporter = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='reported')
    reported = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='reporters')
    reason = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.reporter} - {self.reported}"