#Lists
#Lists are used to store multiple items in a single variable.
#They are ordered, changeable, and allow duplicate values.
#Lists are defined using square brackets [].
#Lists are mutable, meaning you can change their content without changing their identity.
#Lists can contain different data types, including strings, integers, and even other lists.
#Lists can be nested, meaning you can have lists within lists.


Marks1 = 87.8
Marks2 = 92.5
Marks3 = 78.0
Marks4 = 88.5
Marks5 = 90.0

Marks = [87.8, 92.5, 78.0, 88.5, 90.0]
print(Marks)
print(len(Marks))
print(Marks[2])  #Accessing third element


#We can change the value of a list item
Student = ["Shivam", 100, 17, "UP"]
print(Student[0])  #Accessing first element
Student[0] = "Dubey"  #Changing first element
print(Student)

#Lists Slicing
Marks_1 = [87.8, 92.5, 78.0, 88.5, 90.0]
print(Marks_1[1:4])  #Accessing elements from index 1 to 3
print(Marks_1[:3])   #Accessing elements from start to index 2
print(Marks_1[2:])   #Accessing elements from index 2 to end    
print(Marks_1[-3:])  #Accessing last three elements


#Lists Methods
Marks_2 = [87.8, 92.5, 78.0, 88.5, 90.0]
Marks_2.append(95.0)  #Adding an element at the end
print(Marks_2)

Marks_2.insert(2, 85.0)  #Inserting an element at index 2
print(Marks_2)

Marks_2.remove(78.0)  #Removing an element by value
print(Marks_2)

Marks_2.pop()  #Removing the last element
print(Marks_2)

Marks_2.sort()  #Sorting the list
print(Marks_2)

Marks_2.sort(reverse=True)  #Sorting the list in reverse order
print(Marks_2)

Marks_2.reverse()  #Reversing the list
print(Marks_2)

Marks_2.insert(0, 100.0)  #Inserting an element at the beginning
print(Marks_2)

Marks_2.remove(100.0)  #Removing the element we just added
print(Marks_2)
