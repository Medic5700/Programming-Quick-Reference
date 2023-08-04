'''
Author: Medic5700

Everything loops
'''

i : int # Note: this is how to properly annotate the itterator for a 'for loop', just before the 'for loop'
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]: # for iterates over a list, as opposed to in C where you would iterate over a mathimaticle progression of numbers
    print("Loop 0 iteration " + str(i))
print()
    
i : int
for i in range(0,10): # range is usfull for generating lists NOTE: range doesn't include last number
    print("Loop 1 iteration " + str(i))
print()

i : int
for i in range(10,-1,-1): # making a list, and going in reverse
    print("Loop 2 iteration " + str(i))
print()

for _ in range(0,10): # if the itterator isn't relavent, you can use the null veriable '_'
    print("Loop 3 iteration not relavent") 
print()

iteration : int
object : str
for iteration, object in enumerate(['a', 'b', 'c', 'd']): # enumerate allows you to track the itteration number while going through a for loop
    print("Loop 4 iteration " + str(iteration) + "\tobject = " + str(object))
print("=======================================================================")

i : int = 0
while (True):
    print("Loop 5 iteration " + str(i))
    i = i + 1
    if i == 10:
        break # 'break' will break out of the current looping structure
print("----------Loop 5 finished")

i : int
for i in range(0, 10):
    print("Loop 6 iteration " + str(i))
    if i < 9:
        continue # 'continue' will immediatly execute the next iteration of the loop
    print("----------Loop 6 finished")
print("=======================================================================")
    
i : int
for i in range(0, 10):
    print("Loop 7 iteration " + str(i))
else: # else applies to loops to... will execute when no break has been executed
    print("----------Loop 7 finished")
print()
    
i : int = 0
while(i < 10):
    print("Loop 8 iteration " + str(i))
    i = i + 1
else:
    print("----------Loop 8 finished")
print("=======================================================================")
    
