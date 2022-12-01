def calories_of_most_loaded_elf(list):
    max_calories = 0
    for elves_bag in list.split("\n\n"):
        total = 0
        for i in elves_bag.splitlines():
            total += int(i)
        if total > max_calories:
            max_calories = total
    return max_calories



if __name__ == "__main__":
    with open("input.txt") as elves_list:
        lines = elves_list.read()
        print(calories_of_most_loaded_elf(lines))
