def earliest_departure_in(bus_id, earliest_timestamp):
    bus_id = int(bus_id)
    if isinstance(bus_id, int):
        last_missed_run_number = earliest_timestamp // bus_id
        earliest_departure = bus_id * (last_missed_run_number + 1)
        return (bus_id, earliest_departure - earliest_timestamp)
    return None


def earliest_departure(bus_ids, earliest_timestamp):
    # print(bus_ids)
    next_departures = [earliest_departure_in(bus_id, earliest_timestamp)
                       for bus_id in bus_ids if bus_id != 'x']
    # print(next_departures)
    departures_sorted_by_time = sorted(next_departures, key=lambda tup: tup[1])
    return departures_sorted_by_time[0]


def solution_part_1(bus_ids, earliest_timestamp):
    bus_id, wait_time = earliest_departure(bus_ids, earliest_timestamp)
    return bus_id * wait_time


def earliest_schedule(bus_ids):
    # x * 7 = (y * 13) + 1
    x = bus_ids[0]
    y = bus_ids[1]
    biggest = max(bus_ids)

    while(True):
        if ((biggest % x == 0) and ((biggest + 1) % y == 0)):
            lcm = biggest
            break
        biggest += 1
    return lcm


if __name__ == "__main__":
    with open("input.txt") as schedule_file:
        schedule = schedule_file.readlines()
        earliest_timestamp = int(schedule[0])
        bus_ids = schedule[1].strip().split(',')
        print(solution_part_1(bus_ids, earliest_timestamp))
