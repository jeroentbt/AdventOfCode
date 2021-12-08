from solution import part1


def test_part1_example():
    input = \
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
    assert 26 == part1(input)
