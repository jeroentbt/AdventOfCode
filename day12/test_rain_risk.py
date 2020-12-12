from rain_risk import Boat


def test_boat_starts_facing_east():
    b = Boat()
    assert "east" == b.facing
