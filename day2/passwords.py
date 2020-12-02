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
