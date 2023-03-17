# Case 1: implictly rase, Defalut exception handler
a = int(input("Enter a number"))
b  = int(input("Enter another number"))
c = a/b
# Program terminate if exception occurs, and below code not execute
print(c)

# Case 2: implictly rase,  Explicit exception handler

try:
    a = int(input("Enter a number"))
    b = int(input("enter another number"))
    c = a/b
except ZeroDivisionError:
    print("division by zero exception")

print(c)
print("Program still continue")

# Case 3 : explictly raise  , Default exception handler
a = int(input("Enter a number"))
b = int(input("enter another number"))
if b==0:
    raise ZeroDivisionError("zero division error") # pythohn default exception handler handle error, so terminate program
c = a/b
print(c)
print("Program still continue")


# Case 4 : Explictly rsise, and explictly exception handler
try:
    a = int(input("Enter a number"))
    b = int(input("enter another number"))
    if b==0:
        raise ZeroDivisionError("zero division error") # pythohn default exception handler handle error, so terminate program
    c = a/b
    print(c)
except ZeroDivisionError as e:
    print(e)

print("Program still continue")



