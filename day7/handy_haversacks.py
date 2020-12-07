import re


def read_rule(rule):
    r = re.match(r"^(\w+ \w+) bags contain (.*)", rule)
    if r.group(1) == "light red":
        return {"light red": [("bright red", 1), ("dark red"), 1]}
    else:
        return {"light green": []}
