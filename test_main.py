import pytest

from main import *


@pytest.mark.parametrize(
    'weight, distance, expected_output',
    [
        (25, 15, 160000),
        (25, 0, 25000),
        (25, 30, 310000),
        (25, 1, 32000),
        (25, 29, 300000),
        (25, -1, -1),
        (25, 31, -1),
        (0, 15, 150000),
        (50, 15, 160000),
        (1, 15, 150000),
        (49, 15, 160000),
        (-1, 15, -1),
        (51, 15, -1),
    ]
)
def test_calculate_ship_cost_weak_boundary_technique(weight, distance, expected_output):
    assert calculate_ship_cost(weight, distance) == expected_output


@pytest.mark.parametrize(
    'weight, distance, expected_output',
    [
        (-4, 50, -1),
        (55, -3, -1),
        (4, 20, 200000),
        (16, 3, 46000),

    ]
)
def test_calculate_ship_cost_equivalent_class_partitioning_technique(weight, distance, expected_output):
    assert calculate_ship_cost(weight, distance) == expected_output

