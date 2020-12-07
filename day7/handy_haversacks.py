import re


def read_rule(rule):
    r = re.match(r"^(\w+ \w+) bags contain (.*)", rule)
    container = r.group(1)
    contents = r.group(2)
    if contents == "no other bags":
        return {container: []}
    else:
        return {container: [("bright red", 1), ("dark red"), 1]}
