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


#Palindrome (Ma'am, racecar)

#Practice Exercise 2
List_Palindrome1 = [1, 2, 1]
List_Palindrome2 = [1, 2, 3]

copy_list1 = List_Palindrome1.copy()
copy_list1.reverse()

if(copy_list1 == List_Palindrome1):
    print("Palindrome")
else:
    print("Non Palindrome")

copy_list2 = List_Palindrome2.copy()
copy_list2.reverse()
if(copy_list2 == List_Palindrome2):
    print("Palindrome")
else:
    print("Non Palindrome")


#Practice Exercise 3
Grade = ("C", "D", "A", "A", "B", "B", "A")
print(Grade.count("A"))  #Counting occurrences of grade 'A'
print(Grade.count("B"))  #Finding the index of the first occurrence of grade 'B'


#Practice Exercise 4
Grade_1 = ["C", "D", "A", "A", "B", "B", "A"]
Grade_1.sort()  #Sorting the list of grades
print(Grade_1)  #Printing the sorted list of grades