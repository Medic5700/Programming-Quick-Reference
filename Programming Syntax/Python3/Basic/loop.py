for i in range(0,10): #range is usfull for generating lists NOTE: range doesn't include last number
    print ("Loop 0 iteration " + str(i))
for i in range(10,-1,-1): #making a list, and going in reverse
    print ("Loop 1 iteration " + str(i))

i = 0
while (True):
    print ("Loop 2 iteration " + str(i))
    i=i+1
    if i==10:
        break
    
for i in range(0,10):
    print ("Loop 3 iteration " + str(i))
else: #else applies to loops to... will exicute when no break has been exicuted
    print ("----------Loop 3 finished")
    
i=0
while(i<10):
    print ("Loop 4 iteration " + str(i))
    i=i+1
else:
    print ("----------Loop 4 finished")
    
for i in range(0,10):
    print ("Loop 5 iteration " + str(i))
    if i<9:
        continue #continure will immediatly exicute the next iteration of the loop
    print ("----------Loop 5 finished")