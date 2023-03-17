# Instance object varialbe name conflict

# Case 1: 

# class A:
#     def __init__(self):
#         self.a = 3

# class B(A):
#     def __init__(self):
#         # not call parent class init , so only one variable is create which assign value 9
#         self.a =9


# obj1 = B()  # __init__(obj1)
# print(obj1.a)


# # Case 2:
# class A:
#     def __init__(self):
#         self.a = 3

# class B(A):
#     def __init__(self):
#         super().__init__()  # parents class init call , and value assing a to 3
#         self.a = 9   # now a is already available ,so value of a will be update and now a =  9


# obj2 = B()  # __init__(obj1)
# print(obj2.a)



# Case 3: 
class A:
    def __init__(self):
        self.a = 3

class B(A):
    def __init__(self):
        
        self.a = 9   # now a is not availabe , so a create and value assign 9
        super().__init__()  # parents class init call , a is already present so value will be update 3
obj2 = B()  # __init__(obj1)
print(obj2.a)



# Class object variable name conflict

class C:
    x=34
    y = 10
class D(C):
    x =23
print(C.y,D.y)   # Phle child class me check karta hai, nahi milta to parents class me dekta hai
print(C.x)  # x = 34
print(D.x)  #  x  =23



# Static method name conflict
class A:
    @staticmethod
    def f1(a,b):
        print("A")

class B(A):
    @staticmethod
    def f1(a,b):
        print("B static")
    def f1(a,b):
        print("B Instance")
# when two function are same in the same class, then first f1 point to first created function, and after create 2nd function it will start point to next functon , and python garbase collector delete previous function
# so only last function will exist , so no sense same name funciton in same class

B.f1(3, 4)



# Classmethod name conflict
class A:
    @classmethod
    def f1(cls,a):
        print("A")

class B(A):
    @classmethod
    def f1(cls,a,b):
        print("B ")
   

B.f1(7,9)



# 