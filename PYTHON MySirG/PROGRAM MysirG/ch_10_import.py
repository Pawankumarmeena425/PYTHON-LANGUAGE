#import A1  #all modulde has been import
#print ("Value of x is read form A1 file",A1.x)

from A1 import x
x=6  #now x value will be reflect in the A1.py module , if we don't want to change value then use only import A1
print("value of x",x)


#Solution of above problem
from A1 import x as X
x = 7
print("value of x is ",x)
print("value of x of A1 module ",X)


# import "Keyword" module
import keyword
print(keyword.kwlist)

# 2nd way
from keyword import kwlist
print(kwlist)