
#Multiline Comments 

"""
This is Intro to Python
🙂
"""

#String Declaration
name="Satya"
print(name)

#String Operations

greet = "Hello Sam"
print(f"Lower: {greet.lower()}")
print(f"Upper: {greet.upper()}")

#Integer declaration
age = 10
print (age)

#Float Declaration
salary = 25000.50
print(salary)

#Boolean
boole = True
print(boole)

#None 
nothing = None
print (f"None: {nothing}")

a = 20
b = 30
c = 10
equate = c == b - a
Diff = c == b + a
print (f"Boolean: {equate}")
print (f"Boolean Diff: {Diff}")

print ("Data Types")

# Multi line Print Statements

print("""
Employee Details
--------------------
Employee Name : Sam
Age           : 25
Salary        : ₹25000
""")

# Single line Print Statements

print ("Name:", name , type(name))
print ("Age:", age , type(age))
print ("salary:", salary , type(salary))
print ("boole:", boole , type(boole))
print(type(("Name:", name)))

Role="Tester"
print ("Ram")
print(f"Role of Job: {Role}")

passed = 42
rate = 42 / 50
title = "login test"
ok = rate >= 0.8
missing = None
print(type(passed), type(rate), type(ok), type(title), missing)

# Math and Real Time Example

# Integer is returned for variable 

isinstance = 84
var = 42
float = isinstance / var
int = isinstance % var
print(f"float: {float:.3f}")
print(f"Integer: {int}")