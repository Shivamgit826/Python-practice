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

Marks_Lists = [87.8, 92.5, 78.0, 88.5, 90.0]
print(Marks_Lists)
print(len(Marks_Lists))
print(Marks_Lists[2])  #Accessing third element


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


#Tuples in Python
#Tuples are similar to lists but are immutable, meaning their content cannot be changed after creation.
#Tuples are defined using parentheses ().
Marks_Tuple = (87.8, 92.5, 78.0, 88.5, 90.0)
print(Marks_Tuple)      #Printing the tuple
print(type(Marks_Tuple))  #Checking the type of the tuple
print(len(Marks_Tuple)) #Getting the length of the tuple

### Marks_Tuple[0] = 100.0  #This will raise an error because tuples are immutable

Tup = () #Creating an empty tuple
print(Tup)  #Printing the empty tuple
print(type(Tup))  #Checking the type of the empty tuple

# Tup_1 = (1)  #Creating a tuple with one element
Tup_1 = (1,)  #Creating a single-element tuple with a comma
print(Tup_1)  #Printing the single-element tuple
print(type(Tup_1))  #This will not be a tuple, it will be an integer

#Slicing a tuple
Tup_2 = (1, 2, 3, 4, 5)
print(Tup_2[1:4])  #Accessing elements from index 1 to 3
print(Tup_2[:3])   #Accessing elements from start to index 2
print(Tup_2[2:])   #Accessing elements from index 2 to end
print(Tup_2[-3:])  #Accessing last three elements

#Tuple Methods
Tup_3 = (1, 2, 3, 4, 5)
print(Tup_3.index(3))  #Finding the index of the element 3
print(Tup_3.count(2))  #Counting occurrences of the element 2


#Practice Exercise
Fav_Movies = []  #Creating an empty list for favorite movies
Mov_1 = input("Enter the name of Movie: ")
Mov_2 = input("Enter the name of Movie: ")
Mov_3 = input("Enter the name of Movie: ")

Fav_Movies.append(Mov_1)  #Adding first movie to the list
Fav_Movies.append(Mov_2)  #Adding second movie to the list
Fav_Movies.append(Mov_3)  #Adding third movie to the list
print(Fav_Movies)  #Printing the list of favorite movies

# 2nd Method to add movies
Fav_Movies_2 = []  #Creating another empty list for favorite movies
Mov = input("Enter the name of Movie: ")
Fav_Movies_2.append(Mov)
Mov = input("Enter the name of Movie: ")
Fav_Movies_2.append(Mov)
Mov = input("Enter the name of Movie: ")
Fav_Movies_2.append(Mov)
print(Fav_Movies_2)  #Printing the list of favorite movies

# 3rd Method to add movies
Fav_Movies_3 = []  #Creating another empty list for favorite movies
Fav_Movies_3.append(input("Enter the name of Movie: "))
Fav_Movies_3.append(input("Enter the name of Movie: "))
Fav_Movies_3.append(input("Enter the name of Movie: "))
print(Fav_Movies_3)  #Printing the list of favorite movies

