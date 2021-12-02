def position_after_navigation(course):
    position_x = 0
    position_y = 0
    course = course.splitlines()
    for line in course:
        command, units = line.split(' ')
        if command == "forward":
            position_x += int(units)
        if command == "down":
            position_y -= int(units)
        if command == "up":
            position_y += int(units)
    return {"x": position_x,
            "y": position_y}


if __name__ == "__main__":
    with open("../input.txt") as input:
        lines = input.read()
        position = position_after_navigation(lines)
        print(position['x'] * abs(position['y']))
