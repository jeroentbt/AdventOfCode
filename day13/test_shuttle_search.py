from shuttle_search import earliest_departure_in, earliest_departure, \
    solution_part_1, earliest_schedule


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


def test_earliest_departure_of_5_lines_among_xs():
    earliest_timestamp = 939
    bus_ids = [7, 13, 'x', 'x', 59, 'x', 31, 19]
    assert (59, 5) == earliest_departure(bus_ids, earliest_timestamp)


def test_solution_part_1():
    earliest_timestamp = 939
    bus_ids = [7, 13, 'x', 'x', 59, 'x', 31, 19]
    assert 295 == solution_part_1(bus_ids, earliest_timestamp)


def test_earliest_schedule():
    bus_ids = [7, 13]
    assert 77 == earliest_schedule(bus_ids)


def test_earliest_schedule_2_busses_gap():
    bus_ids = [7, 'x', 13]
    assert 63 == earliest_schedule(bus_ids)


def test_earliest_schedule_3_busses_gap():
    bus_ids = [17, 'x', 13, 19]
    # bus_ids = [102, 19]
    assert 3417 == earliest_schedule(bus_ids)
