from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Count, Avg

from game.models import GameRound


class GameRoundLogManager(models.Manager):
    def get_participants_per_round(self):
        return (
            self.values("round_id")
            .annotate(num_participants=Count("player", distinct=True))
            .values_list("round_id", "num_participants")
        )

    def get_most_active_users(self):
        return (
            self.values("player_id")
            .annotate(
                rounds_count=Count("round_id", distinct=True),
                total_spins=Count("id"),
            )
            .filter(rounds_count__gt=0)
            .annotate(
                avg_spins=models.ExpressionWrapper(
                    models.F("total_spins") / models.F("rounds_count"),
                    output_field=models.FloatField(),
                )
            )
            .order_by("-rounds_count")[:10]
        )


class GameRoundLog(models.Model):
    round = models.ForeignKey(GameRound, on_delete=models.CASCADE, editable=False)
    player = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    given_number = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        editable=False,
    )

    objects = GameRoundLogManager()
