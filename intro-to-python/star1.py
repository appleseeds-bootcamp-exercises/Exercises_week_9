# Part 1
for i in range(1,41):
    print(i)

# Part 2
num = 1
while num <= 40 :
    print(num)
    num += 1 

# Part 3
for i in range(1,101):
    if(i%3 == 0 and i%5 == 0):
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)