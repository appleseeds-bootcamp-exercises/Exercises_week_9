import operator

OPERATORS = {
    '-': operator.sub,
    '+': operator.add,
    '*': operator.mul,
    '/': operator.truediv
}


def is_a_no(s):
    return True if s in ['n', 'N', 'no', 'No'] else False


def is_a_yes(s):
    return True if s in ['yes', 'Yes', 'y', 'Y'] else False
