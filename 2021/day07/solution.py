def deltas_to(positions, to):
    return [abs(x-to) for x in positions]


def fuel_to(deltas):
    fuel_for_deltas = []
    for d in deltas:
        fuel = 0
        for s in range(0, d+1):
            fuel += s
        fuel_for_deltas.append(fuel)
    return fuel_for_deltas


def combined_deltas_to(positions, to):
    return sum(deltas_to(positions, to))


def combined_fuel_to(positions, to):
    return sum(fuel_to(deltas_to(positions, to)))


def smallest_combined_delta(positions):
    deltas = []
    for p in range(0, max(positions)):
        deltas.append(combined_deltas_to(positions, p))
    return min(deltas)


def smallest_combined_fuel(positions):
    fuel_consumptions = []
    for p in range(0, max(positions)):
        fuel_consumptions.append(combined_fuel_to(positions, p))
    return min(fuel_consumptions)


if __name__ == "__main__":
    with open("input.txt") as input:
        input = input.read().rstrip()
        print("part 1:", smallest_combined_delta([int(x) for x in input.split(',')]))
        print("part 2:", smallest_combined_fuel([int(x) for x in input.split(',')]))
