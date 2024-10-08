# ****** Python Strings
# NOTE: Strings are immutable, cannot change

# 1. Creating a String "" or ''

# 2. String Concatenation
first_name = "Allan"
last_name = "Ahmed"
full_name = first_name + " " + last_name
print(full_name)

# 3. String Formatting
print(f"My name is: {full_name}.")

# 4. String Slicing
my_string ="Hello, Class"
print(my_string[:5])
print(my_string[7:])

# 5. String Methods

# print string in upper case
upper_cased_string = my_string.upper()
print(f"the original string: {my_string}")
print(f"the upper cased string: {upper_cased_string}")

# print string in lower case
print(f"the upper cased string: {my_string.lower()}")

# split a string
sentence = "Python is a great language"
print(sentence.split())

dashed_word = "front-end-dev"
print(dashed_word.split("-"))

# Replace Python with JavaScript
print(sentence.replace('Python', 'JavaScript'))

# 6. String Length Function
print(len(sentence))

# 7. Check if substring exists
if 'Python' in sentence:
    print("Found language")
else:
     print("Language not found")



# ****** Python Exceptions

#1. Basic try-except Block
# NOTE: To except and handle all errors, replace specific error with "Exception"

try:
    user_choice = int(input("What number would you like to cube?\n"))
    print(type(user_choice))
    print(user_choice**3)
except Exception:
    print("That is not a valid choice! Try again")


# try:
#     user_choice = int(input("What number would you like to divide?\n"))
#     print(user_choice/0)
# except ZeroDivisionError:
#     print("Cannot divide number by zero")