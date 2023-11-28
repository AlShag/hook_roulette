from django.db import transaction
from rest_framework import views
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from game.models.game_round import GameRound
from game.utils import get_participants_stats, get_active_users_stats


class SpinRouletteView(views.APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        game_round, _ = GameRound.objects.get_or_create(is_closed=False)

        with transaction.atomic():
            cell = game_round.do_spin()
            game_round.gameroundlog_set.create(
                player=user,
                given_number=cell,
            )
            return Response({"cell": cell, "jackpot_reached": game_round.is_closed})


class GetStatsView(views.APIView):
    def get(self):
        participants_data = get_participants_stats()
        active_users_data = get_active_users_stats()
        return Response(
            {
                "participants_per_round": participants_data,
                "most_active_users": active_users_data,
            }
        )
