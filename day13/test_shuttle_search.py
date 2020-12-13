from shuttle_search import earliest_departure


def test_earliest_departure_time():
    earliest_timestamp = 939
    bus_id = 7
    assert 945 == earliest_departure(bus_id, earliest_timestamp)
