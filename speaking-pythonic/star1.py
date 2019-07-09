def sum_numbers(numbers):
    sum = 0
    for num in numbers:
        if type(num) == int or type(num) == float:
            sum += num
    return sum
print(sum_numbers([1,2,"ds",321]))
