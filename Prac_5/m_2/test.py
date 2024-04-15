import pytest
from z_1 import distance


@pytest.fixture
def coordinates():
    return [(0, 0, 3, 4), (1, 2, 1, 2), (-1, -1, 1, 1)]


def test_distance_correct(coordinates):
    x1, y1, x2, y2 = coordinates[0]
    assert distance(x1, y1, x2, y2) == 5.0


def test_distance_zero(coordinates):
    x1, y1, x2, y2 = coordinates[1]
    assert distance(x1, y1, x2, y2) == 0.0


def test_distance_negative(coordinates):
    x1, y1, x2, y2 = coordinates[2]
    assert distance(x1, y1, x2, y2) == pytest.approx(2.8284271247461903)
