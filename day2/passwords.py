def get_policy(policystring):
    policy = policystring.split(' ')
    policylist = [int(i) for i in policy[0].split('-')]
    policylist.append(policy[1])
    return tuple(policylist)


def check_policy(listitem):
    policystring, password = tuple(listitem.split(': '))
    min_occurence, max_occurence, occurence_char = get_policy(policystring)
    if min_occurence <= password.count(occurence_char) <= max_occurence:
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
