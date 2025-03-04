"""The two first Fibonacci numbers are 0 and 1, and the next Fibonacci number is always the sum of the two previous
numbers, so we get 0, 1, 1, 2, 3, 5, 8, 13, 21, ..."""

# Create the 20 first Fibonacci numbers

# 1. Implementation using a for loop
previous_number = 0
next_number = 1
print(previous_number)
print(next_number)
for x in range(18):
    new_number = previous_number + next_number
    print(new_number)
    previous_number = next_number
    next_number = new_number

# 2. Implementation using recursion
print(0)
print(1)
count = 2


def fibonacci(previous_number, next_number):
    global count
    if count <= 19:
        new_number = previous_number + next_number
        print(new_number)
        previous_number = next_number
        next_number = new_number
        count += 1
        fibonacci(previous_number, next_number)
    else:
        return


fibonacci(0, 1)
