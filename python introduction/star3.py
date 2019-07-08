num = input("Please insert a 5 digit number:")
num_as_str = str(num)
sum_of_digits = 0
print("You entered the number: "+ str(num))
print("The digits of this number are:", end=" ")
for i in range(len(num_as_str)):
    print(num_as_str[i], end=", ")
    sum_of_digits += int(num_as_str[i])
print(f'\nThe sum of the digits is: {sum_of_digits}')