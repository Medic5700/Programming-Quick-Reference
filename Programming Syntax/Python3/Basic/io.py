#basic input/output to console
print("Some output")
test = input("input test:") #some input
print("The ", end="") #can specify what print and the line with
print("input is = " + test)

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
f1.flush() #flushes stuff writen writen to file to the file
f1.close()

f1 = open("test.log", "r", encoding="utf-8")
print("This is what's in the file:\"" + f1.read() + "\"") #note: read() returns '' when EOF reached
print(f1.tell())
f1.close()
''' some usefull methods for files:
read(size) - reads (size) from file, returns entire file if (size) is omitted or negative
readline() - returns on line of the file
readable() - 
write(x)   - write (x) to file
seek(offset, from_what) - seek to (offset) in file realitive to (from_what)[0=start, 1=current, 2=end]
tell()     - returns current file position
close()    - closes the file
'''

#some basic stuff on reading webpages
import urllib.request #for url stuff
webpageObject = urllib.request.urlopen("http://www.google.com/robots.txt")
data = (webpageObject.read()).decode('utf-8')
print("Data from www.google.com/robots.txt:\n"+data)

#some basic stuff on reading/writing json
# https://docs.python.org/3/library/json.html#module-json
import json
anObject = [1,"test",3.5,[1,2,3,4,5,6,7,8]]

#some basic stuff on reading/writing csv files
# https://docs.python.org/3/library/csv.html
import csv

#some basic stuff using pickle
# https://docs.python.org/3/library/pickle.html#module-pickle
import pickle
