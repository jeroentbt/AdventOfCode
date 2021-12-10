from solution import count_known_digits, read_display, find_9


full_example = \
    "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb |"\
    " fdgacbe cefdb cefbgd gcbe\n" \
    "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec |"\
    " fcgedb cgb dgebacf gc\n" \
    "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef |"\
    " cg cg fdcagb cbg\n" \
    "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega |"\
    " efabcd cedba gadfec cb\n" \
    "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga |"\
    " gecf egdcabf bgf bfgea\n" \
    "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf |"\
    " gebdcfa ecba ca fadegcb\n" \
    "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf |"\
    " cefg dcbef fcge gbcadfe\n" \
    "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd |"\
    " ed bcgafe cdgba cbgef\n" \
    "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg |"\
    " gbdfcae bgc cg cgb\n" \
    "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc |"\
    " fgae cfgab fg bagce\n"

example_one_line = \
    "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |" \
    "cdfeb fcadb cdfeb cdbaf"


def test_part1_example():
    assert 26 == count_known_digits(full_example)


def test_part1_solution():
    with open("input.txt") as input:
        input = input.read()
    assert 488 == count_known_digits(input)


def test_reading_1_display():
    assert 5353 == read_display(example_one_line)


digits = [
     'abcefg'    # 0
     'cf',       # 1
     'acdeg',    # 2
     'acdfg',    # 3
     'bcdf',     # 4
     'abdfg',    # 5
     'abdefg',   # 6
     'acf',      # 7
     'abcdefg',  # 8
     'abcdfg']   # 9


known = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg'}


def test_find_9():
    assert 'abcdfg' == find_9(digits, known)
