from solution import count_known_digits, read_display, \
    determine_digits_with_6_segments


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
     'abcefg',   # 0 # found
     'cf',       # 1 # known
     'acdeg',    # 2
     'acdfg',    # 3
     'bcdf',     # 4 # known
     'abdfg',    # 5
     'abdefg',   # 6
     'acf',      # 7 # known
     'abcdefg',  # 8 # known
     'abcdfg']   # 9 # found


known = {
    0: set('abcefg'),
    1: set('cf'),
    2: set('acdeg'),
    3: set('acdfg'),
    4: set('bcdf'),
    5: set('abdfg'),
    6: set('abdefg'),
    7: set('acf'),
    8: set('abcdefg'),
    9: set('abcdfg')}


def test_find_9():
    assert set('abcdfg') == determine_digits_with_6_segments(digits, known)[9]


def test_find_0():
    assert set('abcefg') == determine_digits_with_6_segments(digits, known)[0]


def test_find_6():
    assert set('abdefg') == determine_digits_with_6_segments(digits, known)[6]
