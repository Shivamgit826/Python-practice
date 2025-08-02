# Variables = Value

a = 10
b = 20
name = "Shivam"
age = b
price = 99.99

print(a+b)
print("Hello World")
print("This is My First Python Program")
print(23)
print("This is My Name", name)
print("This is My Name", "Shivam")
print("Age :", "20")
print("Age :", b)
print(age)
print(price)

sum = a + b
diff = a - b
print(sum)
print(diff)


# Data Types
# 1. String
# 2. Integer
# 3. Float
# 4. Boolean
# 5. List
# 6. Tuple
# 7. Dictionary

print(type(a))
print(type(b))
print(type(price))
print(type(age))
print(type(name))

# Expression Execute in Python

# String & Numeric values can operate together with *
A,B = 2,10
txt1 = "@"
print(2*txt1*10)

A,B = 2,10
txt2 = "Hello"
print(A*txt2*B)

# String & String can Operate with +
C,D = "2", 3
txt3 = "@"
print((C+txt3)*D)

# Numerical Value can Operate with all arithmetic operators
A, B = 2, 3
C = 4
print(A+B*C)

# Arithmetic Expression with Integer & Float will Result In Float
A, B = 2, 3.0
C = A*B
print(C)

# Result of division is always float
A, B = 2, 2
C = A/B
print(C)

A, B = 2, 3
C = A/B
print(C)

#  Integer division with float & int will give int displayed as float
A, B = 1.5,3
C = A//B        #Integer Division // shows int as float by minimum round off e.e, 0.1=0, 0.9=0, 1.9=1, 1.1=1, 1.5=1, 1.9=1, 2.5=2, 2.9=2, 3.5=3, 3.9=3
print(C, A/B)

# Remainder is negative when denominator is negative
A, B = 2, -3
C = A%B         # % = Modulo/Remainder, A%B = A/B
print(C)

# Remainder is positive when denominator is positive
A, B = 2, 3
C = A%B
print(C)

print(A**B)