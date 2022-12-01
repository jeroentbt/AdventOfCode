from solution import *


def test_total_calories_of_one_elf():
    elves_list = "1\n" \
        "1"
    assert 2 == calories_of_most_loaded_elf(elves_list)


def test_most_calories_of_two_elves():
    elves_list = "1\n" \
        "\n" \
        "2"
    assert 2 == calories_of_most_loaded_elf(elves_list)


def test_example_part1():
    elves_list = "1000\n" \
    "2000\n" \
    "3000\n" \
    "\n"\
    "4000\n" \
    "\n"\
    "5000\n" \
    "6000\n" \
    "\n"\
    "7000\n" \
    "8000\n" \
    "9000\n" \
    "\n"\
    "10000"
    assert 24000 == calories_of_most_loaded_elf(elves_list)


def test_example_part2():
    elves_list = "1000\n" \
    "2000\n" \
    "3000\n" \
    "\n"\
    "4000\n" \
    "\n"\
    "5000\n" \
    "6000\n" \
    "\n"\
    "7000\n" \
    "8000\n" \
    "9000\n" \
    "\n"\
    "10000"
    assert 45000 == calories_of_3_most_loaded_elves(elves_list)
