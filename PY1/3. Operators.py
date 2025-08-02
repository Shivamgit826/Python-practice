#------------------------------------------------------------------------------------------------
# Arithmetic Operators
# +(sum), -(difference), *(product), /(quotient), %(remainder), **(power), //(floor division)

# Assignment Operators
# =(assignment), +=(addition assignment), -=(subtraction assignment), *=(multiplication assignment), /=(division assignment), %=(remainder assignment), **=(power assignment), //=(floor division assignment) (right to left)

# Comparison Operators / Relational Operators
# ==(equal to), !=(not equal to), >(greater than), <(less than), >=(greater than or equal to), <=(less than or equal to)

# Logical Operators
# and, or, not
#------------------------------------------------------------------------------------------------


#Assignment Operators
num = 10
num = num + 10      # U can also use += 10
print(num)          # U can also use print("num =", num)
# ANS = 20

# It work for addition, subtraction, multiplication, division, remainder, power, floor division in same variable

# Logical Operators
        # and, or, not
print(not False)
print(not True)

a = 50
b = 20
print( not (a>b))

val1 = True
val2 = False
print("AND Operator: ", val1 and val2)

print("OR Operator: ", a == b or val2)

print("OR Operator: ",(a == b) or (a > b))

print(type(val1))
print(type(a))