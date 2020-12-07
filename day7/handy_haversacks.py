import re


def read_rule(rule):
    r = re.match(r"^(\w+ \w+) bags contain (.*)", rule)
    container = r.group(1)
    contents = r.group(2)
    if contents == "no other bags.":
        return {container: []}
    else:
        r = re.findall(r"(\d) (\w+ \w+)", contents)
        return {container: [(r[0][1], 1), (r[1][1], 1)]}
