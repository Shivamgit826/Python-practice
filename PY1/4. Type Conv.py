# Type Conversion
# a = "2"
# b = 4.25
# sum = a + b     # Integer + Float value cannot be added
# print(sum)

# from ctypes import ARRAY


a = int("10") # Type Conversion / U can convert string to integer
b = 20
sum = a + b
print(sum)
print(type(a))

# Also like this -- a = str(a)

name = input("Enter your name: ")
print("Welcome", name)

val1 = (input("Enter some value: "))
print(type(val1), val1)
print(val1)

val2 = (int(input("Enter some value: ")))
print(type(val2), val2)

val3 = (float(input("Enter some value: ")))
print(type(val3), val3)

# ------------------------------------------------------------------------------------------------

Name = (input("Enter your name: "))
Age = int(input("Enter your age: "))
Marks = float(input("Enter your marks: "))

print(type(Name), Name)
print(type(Age), Age)
print(type(Marks), Marks)

# Practice Ques 1
first = input("Enter First: ")
second = input("Enter Second: ")
print("sum: ", first + second)      # Error

# Practice Ques 2
first = int(input("Enter First: "))
second = int(input("Enter Second: "))
print("sum: ", first + second)

# Practice Ques 3
side = int(input("Enter the side of the square: "))
print("Area of the square is: ", side * side)
print("Area of the square is: ", side ** 2)

# Practice Ques 4
a = float(input("Enter First: "))
b = float(input("Enter Second: "))
print("avg: ", (a + b) / 2)

# Practice Ques 5
a = int(input("Enter First: "))
b = int(input("Enter Second: "))
print(a>=b)