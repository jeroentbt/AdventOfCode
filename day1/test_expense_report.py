def test_get_rest_of_2019():
    assert get_rest(2019) == 1

def test_get_rest_of_1721():
    assert get_rest(1721) == 299

def test_find_entries_that_add_up_t0_2020():
    list = [1721, 979, 366, 299, 675, 1456]
    assert [1721, 299] == find_entries_that_add_up_to_2020(list)

def test_find_entries_that_add_up_t0_2020_2():
    list = [1722, 979, 366, 298, 675, 1456]
    assert [1722, 298] == find_entries_that_add_up_to_2020(list)

    
def get_rest(given_number):
    return 2020 - given_number

def find_entries_that_add_up_to_2020(list):
    for number in list:
        other_number = get_rest(number)
        if other_number in list:
            return [number, other_number]

    
