import json

from django.db import models

from game.utils import CELL_WEIGHTS, get_random_number_using_weights


class GameRound(models.Model):
    cell_weights = models.JSONField(default=CELL_WEIGHTS)
    is_closed = models.BooleanField(default=False)
    cells_remaining = models.JSONField(default=json.dumps(list(range(1, 11))))

    def get_cells_remaining(self) -> list:
        return json.loads(self.cells_remaining)

    def do_spin(self) -> int:
        cells = self.get_cells_remaining()
        number = get_random_number_using_weights(cells)

        cells.pop(number)
        self.cells_remaining = json.dumps(cells)

        if not cells:
            self.is_closed = True

        self.save()

        return number
