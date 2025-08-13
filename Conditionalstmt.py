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
    if(age <= 80):
        print("Can Drive")
    
else:
    print("You cannot drive, you are underage.")