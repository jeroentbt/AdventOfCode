def position_after_navigation(course):
    position_x = 0
    position_y = 0
    aim = 0
    course = course.splitlines()
    for line in course:
        command, units = line.split(' ')
        if command == "forward":
            position_x += int(units)
            position_y = position_y + aim * int(units)
        if command == "down":
            aim += int(units)
        if command == "up":
            aim -= int(units)
    return {"x": position_x,
            "y": position_y}


if __name__ == "__main__":
    with open("../input.txt") as input:
        lines = input.read()
        position = position_after_navigation(lines)
        print(position['x'] * abs(position['y']))
