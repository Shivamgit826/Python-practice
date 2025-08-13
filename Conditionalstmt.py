#Conditional statements
#if, elif, else

Marks = int(input("Enter your marks: "))
if(Marks >= 90):
    Grade = "A"
elif(Marks >= 80 and Marks < 90):
    Grade = "B"
elif(Marks >= 60 and Marks < 80):
    Grade = "C"
elif(Marks < 33):
    Grade = "Fail"
else:
    Grade = "D"

print("Your grade is:", Grade)

#Nested if statements(Nesting)
age = int(input("Enter your age: "))
if(age >= 18):
    if(age >= 80):
        print("Can not drive")
    else:
        print("You can drive.")
    
else:
    print("You cannot drive, you are underage.")


#Practice Questions
Num = 18
if(Num % 2 == 0):
    print("Even")
else:
    print("Odd")

Num1 = int(input("Enter a number: "))
Rem = Num1 % 2
if(Rem == 0):
    print("Even")
else:
    print("Odd")

#Practice Question 2
A = int(input("Enter first number:"))
B = int(input("Enter second number: "))
C = int(input("Enter third number:"))

if(A >= B and A >= C):
    print("A is the largest number")
elif(B >= C):
    print("B is the greatest number")
else:
    print("C is the greatest number")