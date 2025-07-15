from rest_framework import serializers 
from .models import Quest, QuestProgress

class QuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = '__all__'
        read_only_fields = ['created_at', 'changed_at']

class QuestProgressSerializer(serializers.ModelSerializer):
    player = serializers.SlugRelatedField(
    slug_field='username',
    read_only=True,
    default=serializers.CurrentUserDefault()
)

    quest = serializers.SlugRelatedField(slug_field='title', queryset=Quest.objects.all())

    class Meta:
        model = QuestProgress
        fields = '__all__'
        read_only_fields = ['created_at', 'changed_at']