#basic try/except
temp = 0
try:
    temp = 2/0
except: #this will execute when ANY error comes up in the above try statment
    print("Error 0: attempt to divide by zero")

try:
    temp = 2/0
except NameError: #this allows the catching and handling of muletiple difference errors
    print("Error 1: NameError")
except ZeroDivisionError:
    print("Error 1: ZeroDicisionError")
except: #the all case, will catch any remaining error
    print("Error 1: SomeError")

#this one allows you to see what error information is given
try:
    temp = 2/0
except Exception as inst:
    print("Error 2: " + str(inst))
    
