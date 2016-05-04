#basic try/except
temp = 0
try:
    temp = 2/0
except: #this will execute when ANY error comes up in the above try statment
    print("Error 0: attempt to divide by zero")

#this one allows you to see what error information is given
try:
    temp = 2/0
except Exception as inst:
    print("Error 1: " + str(inst))
    
