import operator

OPERATORS = {
    '-': operator.sub,
    '+': operator.add,
    '*': operator.mul,
    '/': operator.truediv
}


def is_a_no(s):
    if s in ['n', 'N', 'no', 'No']:
        return True
    return False


def is_a_yes(s):
    if s in ['yes', 'Yes', 'y', 'Y']:
        return True
    return False
