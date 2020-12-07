import re


def read_rule(rule):
    r = re.match(r"^(\w+ \w+) bags contain (.*)", rule)
    container = r.group(1)
    contents = r.group(2)
    if contents == "no other bags.":
        return {container: []}
    else:
        r = re.findall(r"(\d+) (\w+ \w+)", contents)
        print(r)
        contained_bags = [(bag[1], int(bag[0])) for bag in r]
        return {container: contained_bags}


def read_rules(rules):
    processed_rules = []
    for rule in rules.splitlines():
        processed_rules.append(read_rule(rule))
    print(processed_rules)
    print([{"light red": [("bright red", 8),
                           ("dark red", 1)]},
            {"light green": [("bright blue", 1),
                             ("dark maroon"), 10]},
            {"light maroon": []}])
    return processed_rules
