# ***** PYTHON LOOPS *****

# 1. Basic For Loop
# A loop iterates over a sequence and performs the same operation on each element, such as a list.
# EX: Iterate over and print each number in a list

numbers = [1,2,3,4,5]
# for each num in the list numbers, do the following:
for num in numbers:
    print(num)

print(f"The length of the numbers list is {len(numbers)}")


# 2. For Loop with Range
# EX: Using Range, print numbers from 10 to 15 and step by 2
for num in range(10, 15, 2):
    print(num)



# 3. For Loop over a String
# EX: print each letter in string

print("Looping over a String")
team = "lakers"
for letter in team:
    print(letter)


name = "Allan"
age = 29
print(f'Hi! my name is {name} and I am {age} years old')

print("Hi! my name is "+ name +" and I am ",age," years old")

# 4. While Loop
# A while loop keeps executing as long as its condition evaluates to True
# EX: print numbers from 1 to 5 using a while loop
count = 1
while count <= 5:
    print(count)
    count += 1

# answer = input("Would you like to continue?")
# while(answer == "yes"):
#     print("Welcome back!")
#     answer = input("Would you like to continue?")


# 5. Break Statement
# the break statement breaks out of the loop when a certain condition is met
# EX: Stop the loop when the number 3 is found
print("-----")
count = 1
while count <= 5:
    print(count)
    count += 1
    if count == 3:
        break


    
# 6. Continue Statement
# the continue statement skips the current iteration and continues with the next
# EX: Skip printing number 3
print("-----")

for num in range(5):
    if(num == 3):
        continue
    print(num)



# 7. Nested Loops
# EX: print a multiplication table (1-3)
for x in range(1,4):
    for y in range(1,4):
        print(f"{x}*{y} = {x*y}")




# ***** PYTHON FUNCTIONS *****
# 1. Basic Function
# A function is defined using the def keyword, followed by the function name and parentheses. Inside the parentheses, you can include parameters that the function can accept.
# EX: Define a function to greet a user

def greet():
    print("Hello, Allan!")
    print("Welcome to the class!")
    print("Hope you enjoy learning!")

greet()
greet()


# 2. Function with Parameters
# NOTE: The term "parameters" & "arguments" are used interchangeably
# EX: Define a function with one parameter

def greet_with_params(name="Tony"):
    print(f"Hello, {name}!")
    print("Welcome to the class!")
    print("Hope you enjoy learning!")
print("-----")
greet_with_params("Adam")
greet_with_params("Michael")

# 3. Function with Return Value
# NOTE: In most cases, functions will always return a value
# EX: Define a function that adds two numbers

def add_numbers(num1, num2):
    return num1 + num2

result = add_numbers(2,3)

print(result)


# 4. Function with Default Parameters
# You can specify default values for parameters. If an argument is not provided, the default value is used.
# EX: Define a function with a default parameter

def add_numbers(num1 = 7, num2 = 3):
    return num1 + num2

result = add_numbers(num2 = 10)

print(result)

greet_with_params()

# 5. Anonymous Function(lambda)
# a small function that can have any number of parameters but only one expression
# NOTE: Its not ever needed, its mainly used to clean up code.
# EX: Define a lambda function to cube a number

def add_numbers(num1, num2):
    return num1 + num2

result = lambda num1, num2: num1 + num2
print(f"result of the lambda function is {result(5,8)}")

cubed = lambda num: num**3
print(cubed(2))

# 6. Functions with Arbitrary Arguments (*args)
# pass any number of arguments to a function
# EX: Define a function that accepts any number of arguments

def add_nums(*args):
    return sum(args)

print(add_nums(1,2))
print(add_nums(1,2,3,4,5))
print(add_nums(1,2, 100, 22,12, 200, 5,8,96))



# 7. Functions with Keyword Arguments (**kwargs)
# pass any number of keyword arguments to a function
# EX: Define a function that accepts any number of keyword arguments

def nba_teams(**kwargs):
    print(kwargs)

nba_teams(la="lakers", denver="nuggets", toronto="raptors")