# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 06:42:56 2019

Quick Python tutorial. Based od Python 3

@author: token
"""


### Basics
# Print text value
print("Hello World")

# Print number
print(123)

# Assign None value (like null)
x = None
print(x)

# Check datatype
type(123)

# Help
help(str)


### Numbers

# Integer number example
print(3)

# value type
type(33)

# Float example
print(3.14)

# complex numbers
# "j" sign and parenthesis
x = (15 + 5j)

# check datatype
type(x)



### Strings

'Hello World'

# or

"Hello World"

# String concatenation and variables
a = "Hello "
b = "World"
c = a+b

print(c)

# is is eqwual to:
print("Hello "+'World')


# string multiplication
"Hello World! " * 3

# Substring from left. Numbers from 0
"Hello World! "[1]
"Hello World! "[6:12]
# or
var = "Sample text"
var[7]

# Substring from right
"Hello World! "[-5]

# String reverse in Python
x = "I like learning Python"
print(x[::-1])

# Lower case and upper case on string Value
x = "I like learning Python"
print(x.upper())
print(x.lower())

# You can insert variable into string value.
# Use %s if you want to insert string value.
# Use %d if you want to insert integer number.
# Use %f if you want to insert float number.
# Float with defined fraction %.<number of digits>f 

x = 28
print("Ann is %d years old." % x)

# You can use more than one variable
x = 28
y = "Paris"
print("Ann is %d years old and she is from %s" % (x, y))

# Insert more than one value with same datatype
name = "Ann"
age = 29
score = 78.5
year = 2019
city = "Paris"
print("%s is from %s. She is %d years old. She wrote last exam in %d and reach %.1f points" 
      % (name, city, age, year, score ))


# Check the number of occurrences of the character or string in other string
x = "I like learning Python. Python is the best programming language"
print(x.count("g"))
print(x.count("Python"))

# You can also check the position of string or character in other strig
# Python will return position of first occurence
x = "I like learning Python. Python is the best programming language"
print(x.index("g"))
print(x.index("Python"))

# Check start and end string parts
# It will return True or False 
x = "I like learning Python"
print(x.startswith("I like"))
print(x.endswith("Pyt"))

# Create list of strings from other string
# You need to choose delimiter for example space or "," or ";"
x = "I like learning Python. Python is the best programming language"
print(x.split(" "))

### Operators

# Arithmetic Operators
# use +, -, *, /

# sum 
4 + 2 + 12.2

# multiplication
x = 5 * 5
x

# devide
5 / 2

# devide withot rest
51 // 2

# rest from division
7 % 3

# power
10 **2

# Other way to use arithetic operators - Assignment
x = 17
x += 2
x

# example with power
x = 12
x **= 2
x

# If you want to do longer calculation
x = (2+6) * 2 / 3
print(x)

# Example with string value
#
x = []
x += "Hello World"
print(x)

# Comparision operators
# Comparision operators will retur True or False values
# You can use them in conditional statement
x= 123

print(x==120)
print(x==123)
print(x>=123)
print(x<=123)
print(x>120)
print(x<123)

# Logical operators




### Variables and datatpes
# Variable name cannot start from number
# upper and lower case are important 
# You can use a-z, 0-9 and "-"
# don't use pyhon command to name variables
# In Python you don't need to declare variable before using them

# You can create more than one variable in one line
x,y,z = 1,2,3
print(x)
print(y)
print(z)

# Check datatype
# variable with string datatype
x  = "Python"
type(x)

# variable with list datatype
x = []
type(x)

# variable with float datatype
x = 123.890
type(x)

## Data collections

## Tuples
# Tuple can handle values with different datatype
# Tuple cannot be sort
# Create tuple using ()
# Each element has index
# tuple can handle diffrent datatypes
# You cannot modify list elements
x = 12, "Python", 0.123, (12+5j), (1,2,3,4,5,6)
type(x)

# You can index tuple elements. Index numbers start from 0 value
x[2]
x[0]

# You can also start from right
x[-1]

# 
x[-1][3]

# Adding new values to tuple. "," is needed
y = 'Hello World !',
z = x + y
z

# Tuple multiplication
print(z * 3)


# Checking index number of tuple elements
z.index("Python")
# index will return index of value first occurence
(z*3).index("Python")

# Count occurence of tuple element
z.count("Python")
# or
(z*3).count("Python")

# number of tuple elements
len(z)

# Sum, min, max on tuple elements, when tuple have only numeric values
a = (1, 2, 3.14, 8)
# min
min(a)
# max
max(a)
# sum
sum(a)


## Python lists
# Lists can handle different datatypes values
# Create list using []

l = [1, 2, 'Python', "Learn more"]
type(l)

# You can modify list elements
l[2] = 'abc'
l

# You can index list elements. Index numbers start from 0 value
l[2]
l[0]

# You can also start from right
[-1]

# You can add new values
m = l + [1,2,3,4]
m

# or
l.append("New string value")
l

# Choose element from list
l[-2]

# Choose list elements
l[0:3]

# You can change more than one element
l[0:2] = [1,2,3,4,5,6]
l

# Remove list element using list value
l.remove('Learn more')
l

# Delete list elements using index number
del(l[1:2])
l
# Sort list elements
l.sort
l

# Sort list descending
n = [1,5,2,6,8,3.14]
n.sort(reverse=True)
n

# List elements generator. List of values from 0 to 99
o = list(range(1,100))
o

# How to use arithmetic operations with lists
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)



## Sets in Python
# You can create set using {}.
# Set can contain values of different datatypes
# Elements cannot be repeated
# Elements order is not important
# You cannot sort or index sets

# Create set
x = {1,2,3,4,1,2,3,4,"Hello World", "Python", "Python",1,2,3,4}
x

# You can add new elements to set
x.add(987)
x

# You can remove elements from set
x.remove(987)
x

## Dictionaries in Python
# Key-value datatype 
# Keys need to be uniqe
# Dicts have keys, not indexes
# You can kreate keys also using string values
d ={1:"Python", 2:"is", 3:"the", 4:"best", 7: "programming", 9:"language"}
d

# Choosing value using key number
d[1]
d[9]

# You can modify value using key
d[1] = "Python 3"
d

# You can delete value
del d[7]
d

# You can list keys
d.keys()
# # #  Out[107]: dict_keys([1, 2, 3, 4, 9])

# You can list values
d.values()
# # # Out[108]: dict_values(['Python 3', 'is', 'the', 'best', 'language'])

## zip() function can join different type of collection

my_tuple = 12, "Python", 0.123, (12+5j), (1,2,3,4,5,6)
my_list = [1, 2, 'Python', "Learn more"]
my_set = {1,2,3,4,1,2,3,4,"Hello World", "Python", "Python",1,2,3,4}
my_dict = {1:"Python", 2:"is", 3:"the", 4:"best", 7: "programming", 9:"language"}


# You can reate list using zip() function
zip_list = list(zip(my_tuple, my_list, my_set, my_dict))
zip_list

# You can create dict using zip() function
a=(1,2,3)
b=("Hello","Python","!")
zip_dict = dict(zip(a,b))
zip_dict

### if statement in Python
# You need use ":" in condition line
# use 4 space before result code
# use == if you want use equal condition
x = 100

if x > 100:
    print("Better than 100")
elif x == 100:
    print("x is 100")
elif x < 100:
    print("x is less then 100")
else:
    print("Never mind")


# Conditional statements
x = 10.1
print(x, 'is', 'greater than 100' if x > 100 else 'is not greater than 100')


### For loop
# numbers from 0 to 99
for i in range(100):
    print("number: " + str(i))

# numbers from 1 to 100
for i in range(100):
    print("number: " + str(i+1))

### While loop

n = 10
while n < 101:
    print("current number: ", n)
    n += 2
    

# using break, if you want to quit while loop ealier
n = 10
while n < 101:
    print("current number: ", n)
    n += 2
    if n == 50:
        break

### Loop using sequences
# List crate
[i for i in range(4)]
# or
[i**2 for i in range(4)]

# You can use if statement inside
[i**2 for i in range(4) if i == 4]

### Functions
# You can define your own functions using def statement

# function without input parm
def myFunction():
    print("Hello")

myFunction()

# function with input parm
def myNewFunction(x):
    return x * 10

myNewFunction(5)

### Lambda statement
# You can create new function using lambda statement

myLambdaFunction = lambda x: x ** 10

myLambdaFunction (2)

### Libraries in Python

# math lib
import math

math.e
math.sin(0)
math.pi

# Random values lib
import random
# random value
random.random()

random.seed(100)

# math , statistic, matrix
import numpy

numpy.abs(-100)

