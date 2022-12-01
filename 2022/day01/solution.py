def calories_per_elf(list):
    total_calories_list = []
    for elf_bag in list.split("\n\n"):
        total = 0
        for i in elf_bag.splitlines():
            total += int(i)
        total_calories_list.append(total)
    return total_calories_list

def calories_of_most_loaded_elf(list):
    return max(calories_per_elf(list))


def calories_of_3_most_loaded_elves(list):
    s = sorted(calories_per_elf(list), reverse=True)
    return s[0] + s[1] + s[2]



if __name__ == "__main__":
    with open("input.txt") as elves_list:
        lines = elves_list.read()
        print("Part 1: Most loaded elf carries:")
        print(calories_of_most_loaded_elf(lines))
        print("Part 2: 3 most loaded elves carry:")
        print(calories_of_3_most_loaded_elves(lines))
