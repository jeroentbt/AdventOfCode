def earliest_departure_in(bus_id, earliest_timestamp):
    last_missed_run_number = earliest_timestamp // bus_id
    earliest_departure = bus_id * (last_missed_run_number + 1)
    return (bus_id, earliest_departure - earliest_timestamp)


def earliest_departure(bus_ids, earliest_timestamp):
    next_departures = [earliest_departure_in(bus_id, earliest_timestamp) for bus_id in bus_ids]
    return next_departures[0]
