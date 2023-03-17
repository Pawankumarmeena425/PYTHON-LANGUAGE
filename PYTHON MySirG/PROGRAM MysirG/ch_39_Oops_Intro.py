# Types of Variable

x = 5   # global variable
def f1():
    a = 6   # local varialbe
class A:
    y=98   # class object variable
    def __init__(self):
        self.b = 3  # Instance object variablec


#  way to create instance object variable
# useing __init__
class A:
    def __init__(self,a,b):
        self.a  =a
        self.b = b

# Using instance function
    def f1(self):
        self.c = 5


obj1 = A(10,20) # __init__(obj1,10,20)
obj1.f1()  # now create instance variable c for obj1
print(obj1.a,obj1.b,obj1.c)


# print(obj1.a,obj1.b,obj1.c,obj1.d)  # it will give error, d variable not define

# Direct using instance object
obj1.d  =34
print(obj1.a,obj1.b,obj1.c,obj1.d)  # now it work



# Way to create class object variable
class B:
    x =3 
    @classmethod
    def f2(cls):
        cls.x3=9
B.f2()
print(B.x,B.x3)

B.y = 342342
print(B.y)