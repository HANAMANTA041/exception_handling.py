#1.Predefined Exceptions or in-built exceptions and 2.User Defined(Customized or programatic) Exceptions
#class classname(predefined exception class name):
#    def __init__(self,arg):
#        self.msg = arg

class TooYoungException(Exception):
    def __init__(self,arg):
        self.msg = arg

class TooOldException(Exception):
    def __init__(self,arg):
        self.msg = arg
age = int(input("Enter Age:"))
if age<18:
    raise TooYoungException("Not Eligible")
elif age>18:
    raise TooOldException("Eligible")
else:
    print("You will get email!!!")
    
