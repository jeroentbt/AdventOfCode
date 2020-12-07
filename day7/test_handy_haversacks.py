from handy_haversacks import read_rule, read_rules, can_hold_a, can_hold_a_shiny_gold_bag_eventually


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
    rule = "light red bags contain 1 bright orange bag."
    assert {"light red": [("bright orange", 1)]} == read_rule(rule)


def test_read_rule_contains_multiple_bags_of_1_color():
    rule = "light red bags contain 10 bright orange bags."
    assert {"light red": [("bright orange", 10)]} == read_rule(rule)


def test_read_multiple_rules():
    rules = ("light red bags contain 8 bright red bags, 1 dark red bag.\n"
             "light green bags contain 1 bright blue bag, 10 dark maroon bags.\n"
             "light maroon bags contain no other bags.")
    assert {"light red": [("bright red", 8),
                          ("dark red", 1)],
            "light green": [("bright blue", 1),
                            ("dark maroon", 10)],
            "light maroon": []} == read_rules(rules)


def test_can_hold_a_shiny_gold_bag_1():
    rules = ("light red bags contain 1 bright white bag, 2 muted yellow bags.\n"
             "dark orange bags contain 3 bright white bags, 4 muted yellow bags.\n"
             "bright white bags contain 1 shiny gold bag.\n"
             # "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.\n"
             "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.\n"
             "dark olive bags contain 3 faded blue bags, 4 dotted black bags.\n"
             "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.\n"
             "faded blue bags contain no other bags.\n"
             "dotted black bags contain no other bags.\n")
    assert ["bright white"] == can_hold_a("shiny gold", rules)


def test_can_hold_a_shiny_gold_bag_2():
    rules = ("light red bags contain 1 bright white bag, 2 muted yellow bags.\n"
             "dark orange bags contain 3 bright white bags, 4 muted yellow bags.\n"
             "bright white bags contain 1 shiny gold bag.\n"
             "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.\n"
             "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.\n"
             "dark olive bags contain 3 faded blue bags, 4 dotted black bags.\n"
             "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.\n"
             "faded blue bags contain no other bags.\n"
             "dotted black bags contain no other bags.\n")
    assert ["bright white", "muted yellow"] == can_hold_a("shiny gold", rules)


def test_can_hold_a_shiny_gold_bag_eventually():
    rules = ("light red bags contain 1 bright white bag, 2 muted yellow bags.\n"
             "dark orange bags contain 3 bright white bags, 4 muted yellow bags.\n"
             "bright white bags contain 1 shiny gold bag.\n"
             "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.\n"
             "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.\n"
             "dark olive bags contain 3 faded blue bags, 4 dotted black bags.\n"
             "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.\n"
             "faded blue bags contain no other bags.\n"
             "dotted black bags contain no other bags.\n")
    assert ["bright white", "muted yellow", "dark orange", "light red"] == can_hold_a_shiny_gold_bag_eventually(["shiny gold"], rules)
