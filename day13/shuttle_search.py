def earliest_departure_in(bus_id, earliest_timestamp):
    if isinstance(bus_id, int):
        last_missed_run_number = earliest_timestamp // bus_id
        earliest_departure = bus_id * (last_missed_run_number + 1)
        return (bus_id, earliest_departure - earliest_timestamp)
    return None


def earliest_departure(bus_ids, earliest_timestamp):
    next_departures = [earliest_departure_in(bus_id, earliest_timestamp)
                       for bus_id in bus_ids if bus_id != 'x']
    print(next_departures)
    departures_sorted_by_time = sorted(next_departures, key=lambda tup: tup[1])
    return departures_sorted_by_time[0]


def solution_part_1(bus_ids, earliest_timestamp):
    bus_id, wait_time = earliest_departure(bus_ids, earliest_timestamp)
    return bus_id * wait_time
