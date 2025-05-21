from rest_framework import serializers
from .models import Character, Weapon

class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = [
            'id', 'name', 'range', 'A', 'WS', 'S', 'AP', 'D', 'keywords', 'character'
        ]

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = [
            'id', 'name', 'cost', 'M', 'T', 'SV', 'W', 'LD', 'OC'
        ]

# Nested serializer for Character including its weapons
class CharacterDetailSerializer(serializers.ModelSerializer):
    weapons = WeaponSerializer(many=True, read_only=True)

    class Meta:
        model = Character
        fields = [
            'id', 'name', 'cost', 'M', 'T', 'SV', 'W', 'LD', 'OC', 'weapons'
        ]