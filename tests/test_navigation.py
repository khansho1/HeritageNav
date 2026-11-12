
import pytest

from navigation import (
    haversine_distance,
    calculate_bearing,
    compass_direction,
    walking_time
)


def test_same_location_distance():

    distance = haversine_distance(
        27.1751, 78.0421,
        27.1751, 78.0421
    )

    assert distance == pytest.approx(0)


def test_taj_mahal_to_red_fort_distance():
    distance = haversine_distance(
        27.1751, 78.0421,
        28.6562, 77.2410
    )
    assert 182 < distance < 183

def test_bearing_range():

    bearing = calculate_bearing(
        27.1751, 78.0421,
        28.6562, 77.2410
    )

    assert 0 <= bearing < 360


def test_compass_direction():

    assert compass_direction(0) == "North"
    assert compass_direction(90) == "East"
    assert compass_direction(180) == "South"
    assert compass_direction(270) == "West"


def test_walking_time():

    time = walking_time(10, speed=5)

    assert time == pytest.approx(120)
