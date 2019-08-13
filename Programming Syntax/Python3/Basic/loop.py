for i in [0,1,2,3,4,5,6,7,8,9]: #for iterates over a list, as opposed to in C where you would iterate over a mathimaticle progression of numbers
    print ("Loop 0 iteration " + str(i))
    
for i in range(0,10): #range is usfull for generating lists NOTE: range doesn't include last number
    print ("Loop 1 iteration " + str(i))
for i in range(10,-1,-1): #making a list, and going in reverse
    print ("Loop 2 iteration " + str(i))
print("=======================================================================")

i = 0
while (True):
    print ("Loop 3 iteration " + str(i))
    i=i+1
    if i==10:
        break
print("=======================================================================")
    
for i in range(0,10):
    print ("Loop 4 iteration " + str(i))
else: #else applies to loops to... will execute when no break has been executed
    print ("----------Loop 4 finished")
print("=======================================================================")
    
i=0
while(i<10):
    print ("Loop 5 iteration " + str(i))
    i=i+1
else:
    print ("----------Loop 5 finished")
    
for i in range(0,10):
    print ("Loop 6 iteration " + str(i))
    if i<9:
        continue #continue will immediatly execute the next iteration of the loop
    print ("----------Loop 6 finished")
print("=======================================================================")
