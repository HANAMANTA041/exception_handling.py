"""#the code which causes exception called risky code
try:
    x = int(input("Enter a number:"))
    d = 100/x
    print("Division: ",d)
except ValueError:
    print("Please enter a number")
except:#default exception block
    print("Something Went  wrong")
else:
    print("Else block execution")
finally:
    print("Finally block execution")
print(type(ZeorDivisionError))

#Exception Handling concept applicable for runtime Errors not for syntax errors
#Customized Exception Handling by using try-except
#The code which may raise exception is called risky code and we have to take 
#risky code inside try block. The corresponding handling code we have to take 
#inside except block

print("stmt-1")
try:
    print(10/0)
except ZeroDivisionError:
    print(10/2)
print("stmt-3")

#try with multiple except blocks
try:
    x = int(input("Enter First Number: "))
    y = int(input("Enter Second Number: "))
    print(x/y)
except ZeroDivisionError:
    print("Can't Divide with Zero")
except ValueError:
    print("please provide int value only")
#Python interpreter will always consider from top to bottom until 
#matched except block identified.

#Case-1 If there is no exception
try:
    print("try")
except:
    print("except")
finally:
    print("finally")

#Case-2:If there is an exception raised but handled
try:
    print("try")
    print(10/0)
except ZeroDivisionError:
    print("except")
finally:
    print("finally")

"""
#else block with try-except-finally
try:
    print("try")
    print(10/5)
except:
    print("except")
else:
    print("else")
finally:
    print("finally")
