'''
TRAPEZOID PROGRAM
-------------------
Create a new program that will ask the user for the information needed to find the area of a trapezoid, and then print the area.

Test with the following:

base 1: 2       base 2: 3    height: 4    area: 10
base 1: 5       base 2: 7    height: 2    area: 12
base 1: 1       base 2: 2    height: 3    area: 4.5
base 1: 7       base 2: 2    height: 4    area: 18
'''
#A=a+b/2*h

print("this is a program that helps with finding the area of a trapezoid")

a=float(input("what is the first base"))

b=float(input("what is the second base"))

h=float(input("what is the height of the trapezoid"))

c=((a+b)/2)*h

print(c)