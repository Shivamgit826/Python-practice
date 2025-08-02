# Input in Python

#Input() statement is used to accept values (using keyboard) from user
#String input

name = input("Enter your name: ")
print(name)

#Integer input
age = int(input("Enter your age: "))
print(age)

#Float input
price = float(input("Enter the price: "))
print(price)

print("My name is", name, "and i am", age, "years old")

print('''*Operator Precedence
 not > and > or

 not(true)=false
 not(false)=true

 in and = false
 in or = true''')

# Conditional Statements (if, elif, else)
# (we can't use if, elif, else in variables)

if(age>=18):
    print("You are an adult & you can vote")        #if condition is true

elif(age<=18):
    print("You are not an adult & you can't vote")   #elif condition is true

else:
    print("You are a minor & you can't vote")        #else condition is true


#Example of Conditional Statements
light = input("light: ")
if(light == "red"):
    print("Stop")
elif(light == "yellow"):
    print("Look out")
elif(light == "green"):
    print("Go")
else:
    print("light is broken")

#Example 2 of Conditional Statements
Marks = int(input("Enter your marks: "))
if(Marks>=90):
    print("You got A grade")
elif(Marks>=80):
    print("You got B grade")
elif(Marks>=70):
    print("You got C grade")
else:
    print("You got D grade")


#Practice Question of Conditional Statements
# Print Output 

A = int(input("A: "))
G = input("M/F: ")

if((A ==1 or A ==2) and G == "M"):
    print("fee is 100")
elif((A ==3 or A ==4) and G == "F"):
    print("fee is 200")
elif(A ==5 and G == "M"):
    print("fee is 500")
else:
    print("No fee")

#Single line if statement/ Ternary Operator

# <var>=<val1>if<condition>else<val2>
food = input("food: ")
eat = "Yes" if food == "cake" else "No"
print(eat)

# <stt1> if <condition> else <stt2>
food = input("food: ")
print("sweet") if food == "cake" or food == "chocolate" else print("no sweet")

#Practice Question 1 of Single line if statement
marks = int(input("marks: "))
result = "Pass" if marks >= 33 else "Fail"
print(result)

#Practice Question 2 of Single line if statement
marks = int(input("marks:"))
print("Pass") if marks >= 33 or marks <= 80 else print("Fail")

#Clever if / Ternary Operator
# 1.
age = int(input("age:"))
vote = ("yes", "no")[age < 18]
print(vote)

# 2.
salary = float(input("salary:"))
tax = salary*(0.1, 0.2) [salary > 50000]
print("Tax :", tax)


#------------------------------------------------------------------------------------------------
# Arithmetic Operators
# +(sum), -(difference), *(product), /(quotient), %(remainder), **(power), //(floor division)

# Assignment Operators
# =, +=, -=, *=, /=, %=, **=, //= (right to left)

# Comparison Operators
# ==, !=, >, <, >=, <=
#------------------------------------------------------------------------------------------------