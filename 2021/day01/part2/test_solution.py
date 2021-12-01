from solution import count_increases


def test_flat_surface_has_no_increase():
    depth_measurement = [0, 0, 0, 0]
    assert 0 == count_increases(depth_measurement)


def test_curb_in_surface_has_1_increase():
    depth_measurement = (0, 1, 1, 1)
    assert 1 == count_increases(depth_measurement)


def test_uphil():
    depth_measurement = (0, 0, 0, 1, 2, 3, 4, 5)
    assert 5 == count_increases(depth_measurement)


def test_given_case():
    depth_measurement = (199,
                         200,
                         208,
                         210,
                         200,
                         207,
                         240,
                         269,
                         260,
                         263)
    assert 5 == count_increases(depth_measurement)
