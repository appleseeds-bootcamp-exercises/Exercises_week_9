def fact_helper(num_to_check, index, prev_factorial):
    if prev_factorial == num_to_check:
        return True
    if prev_factorial > num_to_check:
        return False
    return fact_helper(num_to_check, index+1, prev_factorial*index)
def is_factorial_result(num):
    return fact_helper(num,1,1)

print(is_factorial_result(1))
print(is_factorial_result(6))
print(is_factorial_result(14))
print(is_factorial_result(24))
