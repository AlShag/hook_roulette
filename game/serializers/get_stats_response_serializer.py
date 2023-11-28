from rest_framework import serializers


class ParticipantsSerializer(serializers.Serializer):
    round_id = serializers.IntegerField()
    num_participants = serializers.IntegerField()


class ActiveUserSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    rounds_count = serializers.IntegerField()
    avg_spins = serializers.FloatField()


class GetStatsResponseSerializer(serializers.Serializer):
    participants_per_round = ParticipantsSerializer(many=True)
    most_active_users = ActiveUserSerializer(many=True)

