from shuttle_search import earliest_departure_in, earliest_departure


def test_earliest_departure_time_for_one_line():
    earliest_timestamp = 939
    bus_id = 7
    assert (7, 6) == earliest_departure_in(bus_id, earliest_timestamp)


def test_earliest_departure_of_two_lines():
    earliest_timestamp = 939
    bus_ids = [7, 13]
    assert (7, 6) == earliest_departure(bus_ids, earliest_timestamp)


def test_earliest_departure_of_3_lines():
    earliest_timestamp = 939
    bus_ids = [7, 13, 59]
    assert (59, 5) == earliest_departure(bus_ids, earliest_timestamp)


def test_earliest_departure_of_5_lines():
    earliest_timestamp = 939
    bus_ids = [7, 13, 59, 31, 19]
    assert (59, 5) == earliest_departure(bus_ids, earliest_timestamp)
