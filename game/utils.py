import random

CELL_WEIGHTS = {
    1: 20,
    2: 100,
    3: 45,
    4: 70,
    5: 15,
    6: 140,
    7: 20,
    8: 20,
    9: 140,
    10: 45,
}


def get_random_number_using_weights(numbers: list[int]) -> int:
    weights = list(CELL_WEIGHTS.values())
    return random.choices(numbers, weights, k=1)[0]
