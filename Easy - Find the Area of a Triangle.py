# This program is to find the area of a traingle using Python

# get three sides of the triangle from the user and store them in variables a, b, and c

a = float(input("a = "))

b = float(input("b = "))

c = float(input("c = "))

# compute semiperimeter s

s = (a+b+c)/2

# compute area and print it

area = (s*(s-a)*(s-b)*(s-c))**0.5

print(f"The area of the triangle for the given sides a,b and c is {area}")