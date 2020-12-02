def get_policy(policystring):
    return tuple([int(i) for i in policystring.split('-')])
