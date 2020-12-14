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
    iterable = iter(bus_ids)
    x = next(x for x in iterable if isinstance(x, int))
    print(x)
    y = next(x for x in iterable if isinstance(x, int))
    print(y)
    biggest = max([x, y])
    gap = bus_ids.index(y) - bus_ids.index(x)
    print(gap)

    while(True):
        if ((biggest % x == 0) and ((biggest + (1 * gap)) % y == 0)):
            lcm = biggest
            break
        biggest += 1
    print(lcm)
    return lcm






if __name__ == "__main__":
    with open("input.txt") as schedule_file:
        schedule = schedule_file.readlines()
        earliest_timestamp = int(schedule[0])
        bus_ids = schedule[1].strip().split(',')
        print(solution_part_1(bus_ids, earliest_timestamp))
    # stopen
    data = open('input.txt', 'r').read().split('\n')
    data = data[1].split(',')
    B = [(int(data[k]), k) for k in range(len(data)) if data[k] != 'x']

    lcm = 1
    time = 0
    for i in range(len(B)-1):
        bus_id = B[i+1][0]
        idx = B[i+1][1]
        lcm *= B[i][0]
        while (time + idx) % bus_id != 0:
            time += lcm
    print(time)
