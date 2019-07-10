def sum(list_to_sum, index):
    if index >= len(list_to_sum):
        return 0
    return list_to_sum[index]+ sum(list_to_sum, index+1)



assert(sum([1, 2, 3, 4, 5], 0) == 15)
assert(sum([], 0) == 0)
assert(sum([11], 0) == 11)
assert(sum([11, 0], 0) == 11)
assert(sum([11, -1], 0) == 10)