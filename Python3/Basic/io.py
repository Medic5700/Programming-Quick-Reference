#basic input/output to console
print("Some output")
test = input("input test:") # some input
print("The ", end="") # can specify what print ends the line with, in this case nothing
print("input is = " + test)

print("=======================================================================")

print("printing with str:   " + str("test \t\t test \u25a0"))
print("printing with repr:  " + repr("test \t\t test \u25a0")) # repr is like casting with str, but returns a human readable string in cases with standard escape characters
print("printing with ascii: " + ascii("test \t\t test \u25a0")) # ascii returns a string, but also converts all characters (think unicod) into a human readable string

print("=======================================================================")

#some stuff on files
f1 = open("test.log", "w", encoding="utf-8")
'''file modes:
'r' = read (default)
'w' = write
'x' = exclusive file creation, fails if file exists
'a' = append

'b' = binary mode
't' = text mode (default)

'+' = updating (reading and writing)
'''

f1.write("This is a test")
f1.flush() # flushes stuff writen writen to file to the file
f1.close()

f1 = open("test.log", "r", encoding="utf-8")
print("This is what's in the file:\"" + f1.read() + "\"") # note: read() returns '' when EOF reached
print(f1.tell())
f1.close()
''' some usefull methods for files:
read(size) - reads (size) Bytes from file, returns entire file if (size) is omitted or negative
readline() - returns one line of the file
readable() - 
write(x)   - write (x) to file
seek(offset, from_what) - seek to (offset) in file realitive to (from_what)[0=start, 1=current, 2=end]
tell()     - returns current file position
close()    - closes the file
'''
print("=======================================================================")
#TODO some stuff on the 'with' statement
# https://www.geeksforgeeks.org/with-statement-in-python/


print("=======================================================================")

#some basic stuff on reading webpages
import urllib.request # for url stuff
webpageObject = urllib.request.urlopen("http://www.google.com/robots.txt")
data = (webpageObject.read()).decode('utf-8')
print("Data from www.google.com/robots.txt:\n"+data)
print("=======================================================================")

#some basic stuff on reading/writing json
# https://docs.python.org/3/library/json.html#module-json
'''json is pretty secure/hard to exploit just because of how simple the decoder is
it is limited in what it can encode, and the result takes a lot more space'''
import json
anObject = [1,"test",3.5,[1,2,3,4,5,6,7,8]]
print(json.dumps(anObject)) # this returns a string representation of the object
print(json.dumps(anObject, sort_keys=True, indent=4))
newObject = json.loads(json.dumps(anObject)) # turns a string back into an object
print(newObject)

print("=======================================================================")

#some basic stuff on reading/writing csv files
# https://docs.python.org/3/library/csv.html
import csv
#TODO
print("=======================================================================")

#some basic stuff using pickle
# https://docs.python.org/3/library/pickle.html#module-pickle
import pickle
#TODO
print("=======================================================================")
