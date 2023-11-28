from drf_spectacular.utils import extend_schema
from rest_framework import views
from rest_framework.response import Response

from game.models import GameRoundLog
from game.serializers import (
    GetStatsResponseSerializer,
)


class GetStatsView(views.APIView):
    @extend_schema(
        responses=GetStatsResponseSerializer,
    )
    def get(self, request):
        participants_per_round = GameRoundLog.objects.get_participants_per_round()
        participants_data = [
            {"round_id": round_id, "num_participants": num_participants}
            for round_id, num_participants in participants_per_round
        ]

        most_active_users = GameRoundLog.objects.get_most_active_users()
        active_users_data = [
            {
                "user_id": user["player_id"],
                "rounds_count": user["rounds_count"],
                "avg_spins": user["avg_spins"],
            }
            for user in most_active_users
        ]
        serializer = GetStatsResponseSerializer(
            data={
                "participants_per_round": participants_data,
                "most_active_users": active_users_data,
            }
        )
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data)
