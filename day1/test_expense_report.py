def test_get_rest_of_2019():
    assert get_rest(2019) == 1

def test_get_rest_of_1721():
    assert get_rest(1721) == 299

    
def get_rest(given_number):
    return 2020 - given_number
