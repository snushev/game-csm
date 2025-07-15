from rest_framework import serializers 
from .models import Player, Guild, Report

class PlayerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Player
        fields = '__all__'
        read_only_fields = ['level', 'xp', 'gold', 'created_at', 'changed_at']

class GuildSerializer(serializers.ModelSerializer):
    leader = serializers.SlugRelatedField(slug_field='nickname', queryset=Player.objects.all())
    members = serializers.SlugRelatedField(slug_field='nickname', queryset=Player.objects.all(), many=True)

    class Meta:
        model = Guild
        fields = '__all__'
        read_only_fields = ['created_at', 'changed_at']

    def validate(self, data):
        instance = getattr(self, 'instance', None)
        current_members = instance.members.count() if instance else 0
        new_members = len(data.get('members', []))
        
        if current_members + new_members > 100:
            raise serializers.ValidationError("Guild cannot be more than 100 members!")
        return data
    
class ReportSerializer(serializers.ModelSerializer):
    reporter = serializers.SlugRelatedField(
    slug_field='username',
    read_only=True,
    default=serializers.CurrentUserDefault()
)

    reported = serializers.SlugRelatedField(slug_field='nickname', queryset=Player.objects.all())
    class Meta:
        model = Report
        fields = '__all__'
        read_only_fields = ['created_at', 'changed_at']
