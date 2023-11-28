from django.urls import path

from game.views.spin_roulette_view import SpinRouletteView
from game.views.get_stats_view import GetStatsView

urlpatterns = [
    path("spin", SpinRouletteView.as_view()),
    path("stats", GetStatsView.as_view()),
]
