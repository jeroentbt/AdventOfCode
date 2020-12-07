from handy_haversacks import read_rule


def test_read_rule_only_single_bags():
    rule = "light red bags contain 1 bright red bag, 1 dark red bag."
    assert {"light red": [("bright red", 1), ("dark red", 1)]} == read_rule(rule)


def test_read_rule_no_bags():
    rule = "light green bags contain no other bags."
    assert {"light green": []} == read_rule(rule)


def test_read_rule_only_single_bags_but_other_colors():
    rule = "light red bags contain 1 bright orange bag, 1 dark orange bag."
    assert {"light red": [("bright orange", 1), ("dark orange", 1)]} == read_rule(rule)


def test_read_rule_only_1_bag():
    rule = "light red bags contain 1 bright orange bag"
    assert {"light red": [("bright orange", 1)]} == read_rule(rule)


def test_read_rule_contains_multiple_bags_of_1_color():
    rule = "light red bags contain 10 bright orange bag"
    assert {"light red": [("bright orange", 10)]} == read_rule(rule)
