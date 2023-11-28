from rest_framework import serializers


class SpinRouletteResponseSerializer(serializers.Serializer):
    cell = serializers.IntegerField()
    jackpot_reached = serializers.BooleanField()
