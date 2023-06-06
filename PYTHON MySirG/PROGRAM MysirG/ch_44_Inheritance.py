class Person:
    def __init__(self,n,a):
        self.name = n
        self.age  =a
    def showName(self):
        print(self.name)
    def showAge(self):
        print(self.age)

class Student(Person):
    def __init__(self,n,a,r):
        Person.__init__(self,n,a)#when we call instance object using class name, then implicitly no object is pass so explictly we rquire pass object
        super().__init__(n,a) # super given instance 
        self.rollno = r

    def setRollnl(self,r):
        self.rollno  = r
    def showRollno(self):
        print(self.rollno)

s1 = Student("rahul", 12, 123)
s1.showAge()
s1.showName()
s1.showRollno()