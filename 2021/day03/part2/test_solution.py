from solution import calc_life_support_rating


def test_example():
    input = "00100\n" \
        "11110\n" \
        "10110\n" \
        "10111\n" \
        "10101\n" \
        "01111\n" \
        "00111\n" \
        "11100\n" \
        "10000\n" \
        "11001\n" \
        "00010\n" \
        "01010\n"
    assert 230 == calc_life_support_rating(input)
