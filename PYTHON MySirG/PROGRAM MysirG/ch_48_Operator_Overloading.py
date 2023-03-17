class Line:
    def __init__(self,l):
        self.length=l
    def showlength(self):
        print("Length = ",self.length)

    def __add__(self,other):
        return Line(self.length+other.length)


l1 = Line(10)
l2  = Line(20)

# l3 = l1+l2   # + operator work for object , because they definiation define in their corrosponding class, for example it add two integer , because in integer class it defination define
# But here + operator not define in Line class , so can't be use
# so first we define operator in class


l3 = l1+l2  #l3 = l1.__add__(l2)-->>> __add(l1,l2)__
l3.showlength()

# another way
l3 = l1.__add__(l2)
l3.showlength()


#  ***********************************Operator overloading in way to implements polymarphism******************************************

