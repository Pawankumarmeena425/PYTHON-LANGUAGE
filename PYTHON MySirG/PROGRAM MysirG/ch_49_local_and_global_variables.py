# Case 1 :
x=20
def f1():
    X=10  #local varialbe
    print(x)  #local variable x

f1()
print(x)  #global variable x

# Case 2:
x1=40
def f2():
    global x
    x1  =10
    print(x1)

f2()
print(x1)


# case 3:
x1=40
def f2():
    # x=54 error
    global x
    x1  =10
    print(x1)

f2()
print(x1)

# Case 4 : how global and local variable access in same function
x1=40
def f2():
   
    x1  =10  #local variable
    print(x1)  #print local variable
    d =  globals()
    d['x1']=90
    print(d['x1'])

f2()
print(x1)


