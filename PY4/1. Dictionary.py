info = {
    "key" : "value",
    "name" : "John",
    "age" : 30,
    "is adult" : True,
    "city" : "New York",
    "learning" : ["Python", "JavaScript", "C++"],
    "topics" : ("Math", "Science", "History")
}

print(info)
print(type(info))

print(info["name"]) # Accessing value by key
print(info["learning"][0]) # Accessing value in a list inside the dictionary   

info["name"] = "Jane" # Modifying value
print(info["name"])
print(info)

info["surname"] = "Doe" # Adding new key-value pair

#Null Dictionary
Null_dict = {}
print(Null_dict)
print(type(Null_dict))
Null_dict["new_key"] = "new_value"
print(Null_dict)

#Nested Dictionary
Students = {
    "name" : "Alice",
    "age" : 22,
    "subjects" : {
        "Math" : 90,
        "Science" : 85,
        "History" : 88
    }
}
print(Students)
print(Students["subjects"])     # Accessing nested dictionary
print(Students["subjects"]["Math"]) # Accessing value in nested dictionary


# Dictionary Methods
print(info.keys())  # Returns a view object of all keys
print(info.values()) # Returns a view object of all values
print(info.items())  # Returns a view object of all key-value pairs
print(len(info))    # Returns the number of key-value pairs
print(info.values()) # Returns a view object of all values


print(list(info.keys()))  # Converts dictionary keys to a list
print(list(info.values())) # Converts dictionary values to a list