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


def can_hold_a(bag_to_hold, rules):
    can_hold = []
    processed_rules = read_rules(rules)
    for container_bag, container_rule in processed_rules.items():
        for contained_bag in container_rule:
            bag, amount_ = contained_bag
            if bag == bag_to_hold:
                can_hold.append(container_bag)
    return can_hold


def can_hold_a_shiny_gold_bag_eventually(rules):
    processed_rules = read_rules(rules)
    bags = find_container_for(["shiny gold"], [], processed_rules)
    print('BAGS', bags)
    return bags


def find_container_for(list_of_bags_to_find_container_for,
                       known_containers,
                       rules):
    found_containers = []
    # print('known containers: ', known_containers)
    # print('list_of_bags_to_find_container_for: ', list_of_bags_to_find_container_for)
    if list_of_bags_to_find_container_for != ["shiny gold"]:
        known_containers += list_of_bags_to_find_container_for
    # print('known_containers', known_containers)
    for container_bag, content_rule in rules.items():
        for contained_bag, amount_ in content_rule:
            # print(contained_bag)
            if contained_bag in list_of_bags_to_find_container_for:
                # print('found one!')
                found_containers.append(container_bag)
    # print('found_containers: ', found_containers)
    if found_containers != []:
        find_container_for(set(found_containers), known_containers, rules)
    # print('known_containers: ', known_containers)
    return set(known_containers)


if __name__ == "__main__":
    with open("input.txt") as rulefile:
        bags_that_contaon_shiny_gold = can_hold_a_shiny_gold_bag_eventually(rulefile.read())
        print('number of bags that can contain  shiny gold:')
        print(len(bags_that_contaon_shiny_gold))
