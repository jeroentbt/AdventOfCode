def get_policy(policystring):
    positions, char = tuple(policystring.split(' '))
    policy = [(int(i) - 1) for i in positions.split('-')]
    policy.append(char)
    return tuple(policy)


def check_policy(listitem):
    policystring, password = tuple(listitem.split(': '))
    position_one, position_two, occurence_char = get_policy(policystring)
    char_found_times = 0

    if password[position_one] == occurence_char:
        char_found_times += 1
    if password[position_two] == occurence_char:
        char_found_times += 1

    if char_found_times == 1:
        return True
    else:
        return False


if __name__ == "__main__":
    valid_password_count = 0
    with open("input.txt") as passwordlist:
        lines = passwordlist.readlines()
    for line in lines:
        if check_policy(line):
            valid_password_count += 1
    print(valid_password_count)
