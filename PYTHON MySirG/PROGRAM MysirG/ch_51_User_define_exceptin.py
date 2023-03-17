# Case 1 : 
# User define Exception
# class InsufficientBalance(Exception):
#     def __init__(self,errmsg):
#         self.errmsg = errmsg
#     def __str__(self):
#         return self.errmsg


# class Account:
#     def __init__(self,accno, bal):
#         self.accno = accno
#         self.bal = bal
#     def showbalance(self):
#         print("Your current balance is : ",self.bal)
#     def withdraw(self,amt):
        
#         if amt>self.bal:
#             raise InsufficientBalance("Insufficient Balance")
#             # implictly python defalut exception run so , terminate programm
#         self.bal = self.bal-amt
#         print("You have withdrawn",amt)

# my_acc = Account(131231212, 5000)
# my_acc.showbalance()
# my_acc.withdraw(7000)
# my_acc.showbalance()




# Case 2:
# User define Exception
class InsufficientBalance(Exception):
    def __init__(self,errmsg):
        self.errmsg = errmsg
    def __str__(self):
        return self.errmsg


class Account:
    def __init__(self,accno, bal):
        self.accno = accno
        self.bal = bal
    def showbalance(self):
        print("Your current balance is : ",self.bal)
    def withdraw(self,amt):
        
        if amt>self.bal:
            raise InsufficientBalance("Insufficient Balance")
            
        self.bal = self.bal-amt
        print("You have withdrawn",amt)

my_acc = Account(131231212, 5000)
my_acc.showbalance()
try:
    my_acc.withdraw(7000)
except InsufficientBalance as e:
    print(e)
# here exception is handle explictly , so blow code will be execute
my_acc.showbalance()