def find_max(a_list, index):
    if(len(a_list) == 0):
        return 0
    if index >= len(a_list) - 1:
        return a_list[index]
    next_max = find_max(a_list, index + 1)
    if next_max > a_list[index]:
        return next_max
    else:
        return a_list[index]


assert (find_max([1, 2, 3], 0) == 3)
assert (find_max([100, 2, 100], 0) == 100)
assert (find_max([], 0) == 0
        )  # what is your return value for empty list? Decided it will be 0
assert (find_max([11], 0) == 11)
assert (find_max([11, 0], 0) == 11)
assert (find_max([11, -19], 0) == 11)
