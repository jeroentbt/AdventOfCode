import re


def read_rule(rule):
    r = re.match(r"^(\w+ \w+) bags contain (.*)", rule)
    container = r.group(1)
    contents = r.group(2)
    r = re.findall(r"(\d+) (\w+ \w+)", contents)
    contained_bags = [(bag[1], int(bag[0])) for bag in r]
    return {container: contained_bags}


def read_rules(rules):
    processed_rules = {}
    for rule in rules.splitlines():
        processed_rule = read_rule(rule)
        bag = list(processed_rule.keys())[0]
        processed_rules[bag] = processed_rule[bag]
    return processed_rules
