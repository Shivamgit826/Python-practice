#Conditional statements

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