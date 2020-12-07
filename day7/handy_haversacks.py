import re


def read_rule(rule):
    r = re.match(r"^(\w+ \w+) bags contain (.*)", rule)
    container = r.group(1)
    if container == "light red":
        return {container: [("bright red", 1), ("dark red"), 1]}
    else:
        return {container: []}
