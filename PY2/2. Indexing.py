#Indexing is the process of accessing the elements of a string by their position.
#Indexing starts from 0.
#Indexing is used to access the elements of a string by their position.
#Indexing is used to access the elements of a string by their position.


str = "Hello! I am a string"
ch = str[5]
print(ch)

str2 = "Hello! I am a string 2"
print(str2[4])

str3 = "This is a string 3"
print(str3[1:6])

str4 = "I am a string 4"
print(str4[5:len(str)])     #len(str) is used to get the length of the string

str5 = "This is a string 5"
print(str5[:7])

str6 = "I am a string 6"
print(str6[5:]) #print(str5[5:]) is used to print the string from index 5 to the end of the string


#Negative Indexing

#Negative Indexing is used to access the elements of a string by their position from the end of the string.

str7 = "This is a string 7"
print(str7[-6:-2])