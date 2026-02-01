#1st code of week 3
def maximum(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("The max no. is", maximum(a, b, c))

#2nd code of week 3
import numpy as np
a = np.array([(1,2,3),(4,5,6)],dtype=float)
b = np.array([(7,8,9),(10,11,12)],dtype=float)
print(np.add(a,b))
print(np.multiply(a,b))
print(np.transpose(a))