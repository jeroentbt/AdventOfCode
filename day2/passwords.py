def read_min_and_max(policy_min_max_string):
    return tuple([int(i) for i in policy_min_max_string.split('-')])
