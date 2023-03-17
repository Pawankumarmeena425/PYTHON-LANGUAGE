# a = int(input("Enter a number"))
# # if use enter the string, then it will value error
# print(a)

# l = [2,3,4]
# print(l[4]) # this is index error

# l.print()  # this is attributs error, no print function define in the list class

# print(3/0)# when number is divisible by zero , it is zero error

# d = {"name":"Pawan","roll":2424}
# print(d["id"])  # id not exist in the dictionary  , so it is key error

# print(y)  # this is name error


# print(4+"43") # this is type error




# Built in functions

m  = locals()['__builtins__']  # all exception class and various method inside the __builtins__
for x in m.__dict__:
    print(m.__dict__[x])


# Case 1 : when user enter string
try:
    a = int(input("Enter a number"))
    print(a)
except ValueError as e:
    print("Entered value is not a number")

print("hello") # here hello also print, because implictly exeption handle


# Case 2 : when user enter string
try:
    a = int(input("Enter a number"))
    print(a)
except ZeroDivisionError as e:
    print("Entered value is not a number")
# now if we enter string , and here exceptly define exception is ZDE , so it can't be able to handle it and python explictly handle it , so bleow code not execute 
print("hello")



try:
    a = int(input("enter the number"))
    b = int(input("Enter another number"))
    c = a/b
    print("Result : ",c)

except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
except:
    print("Some Exception")
else:
    print("no exception")
finally:
    print("I am going to run in all situations")

print("Sonme other code")