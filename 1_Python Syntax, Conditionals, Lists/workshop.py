# Python Syntax
# camelCase, snake_case, PascalCase, UPPER_CASE
firstName = "Allan"
myLastName = "Allan"

first_name = "Allan"

FirstName = "Allan" # used only for classes

FIRST_NAME = "Allan" # used only for constants (value never changes)

# Python Conditionals (if, elif, else)
# falsy values
# empty sequences and collections (lists, tuples, strings, dictionaries, sets), zero in every numeric type, None, and False

# temp is 10        this is a statement
temp = 50

# if temp is equal 0?        This is a question to check the value of temp
if(temp == 0):
    print("The temp is zero")



if(temp):
    print("temp defined")
else:
    print("temp undefined")



# comparison operators
# <, <=, >, >=, ==, !=
# if temp is larger or equal to 90
if (temp >= 90):
    print("Its pretty steamy outside, do not wear black!")
elif( temp >=75 ):
    print("Its a nice day!")
elif temp == 50:
    print("The temp is 50 degrees exact!")
else:
    print("It's cold outside!")

# if temp is not equal to 0 ?
if( temp != 0):
    print("Temp is not 0 degrees")




# logical AND & OR
# user_name = "allana"
# password = "golakers"
# first_name = "Allan"

# if (user_name == "allana1" or first_name == "Allan"):
#     print("Hello user Allan")


# if(user_name == "allana" and password == "golakers"):
#     print("Welcome Lead Instructor!")
# else:
#     print("Welcome, student!")




# nested if & input function
user_name = "allana"
first_name = "Allan"

if (user_name == "allana" or first_name == "Allan"):
    user = input("Are you the Lead Instructor, Allan Ahmed? (yes or no)").upper()
    print("The user responded with: "+user)
    if(user == "YES"):
        print("Access Granted: Hello " + user_name)
    elif(user == "NO"):
        print("Go away, please.")
    else:
        print("You entered a wrong answer")
else:
    print("Welcome, Student!")



# Python Lists: Stores multiple values in a single variable
#Index          0           1           2       3
students = ["Victoria", "Michael", "Emanuel", "Adam"]
# indexing
print("The first student is " + students[0])
print("The third student is " +students[2])
print("The second student is " +students[1])
print("The fourth student is " +students[3])

# slicing (start(includes): stop(excludes): step)
print(students[1:3])

print(students[::2])


# add to list
students.append("Rahil")
students.append("Silas")
print(students)


# remove from list using .pop(0), .remove('student 1'), del, .clear()

students.pop(2) # .pop(2) removes index value

students.remove("Michael") # .remove("Michael") removes item by the value

del students[0]

students.clear()

print(students)

# membership checks with "in" & "not in"
curriculum = ["python", "javascript", "html/css"]

# if "python" is in languages
# if("c++" in curriculum):
#     print('Language is apart of the curriculum')
# else:
#     print('Language is NOT apart of the curriculum')

if("c++" not in curriculum):
    print('Language is NOT apart of the curriculum')
else:
    print('Language is apart of the curriculum')