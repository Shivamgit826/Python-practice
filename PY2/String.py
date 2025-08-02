str1 = "This is a string"
str2 = 'Shivam'
str3 = """This is a string"""

"This is shiva's Tutorial"  #If we want to use single quote in the string we can use double quote to enclose the string

str4 = "This is a string. We are creating it in python."
print(str4)

str5 = "This is a string.\nWe are creating it in python."   
print(str5)

str6 = "This is a string.\tWe are creating it in python."   #\t is used to print the string in a tab space
print(str6)


#--------------------------------------------------------------------------------------------------------------------
#Escape Sequence
# \n is used to print the string in a new line
# \t is used to print the string in a tab space
# \r is used to print the string in a new line and then the string after \r will be printed in the new line
# \b is used to print the string in a backspace
# \f is used to print the string in a form feed
# \a is used to print the string in a alert
# \v is used to print the string in a vertical tab
# \o is used to print the string in a octal value
# \x is used to print the string in a hexadecimal value
# \u is used to print the string in a unicode value
#--------------------------------------------------------------------------------------------------------------------


str7 = "Shivam"
len7 = len(str7)
print(len7)


str8 = " Dubey"
len8 = len(str8)    #Also calculated spaces in Length(len)
print(len8)


Final_str = str7 + str8
print(Final_str)