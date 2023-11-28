from django.db import transaction
from drf_spectacular.utils import extend_schema
from rest_framework import views
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from game.models.game_round import GameRound
from game.serializers import SpinRouletteResponseSerializer


class SpinRouletteView(views.APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        responses=SpinRouletteResponseSerializer,
    )
    def post(self, request, *args, **kwargs):
        user = request.user
        game_round, _ = GameRound.objects.get_or_create(is_closed=False)

        with transaction.atomic():
            cell = game_round.do_spin()
            game_round.gameroundlog_set.create(
                player=user,
                given_number=cell,
            )
            serializer = SpinRouletteResponseSerializer(
                data={"cell": cell, "jackpot_reached": game_round.is_closed}
            )
            serializer.is_valid(raise_exception=True)

            return Response(serializer.data)
