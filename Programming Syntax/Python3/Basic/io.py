#basic input/output to console
print("Some output")
test = input("input test:") #some input
print("The ", end="") #can specify what print and the line with
print("input is = " + test)

#some stuff on files
f1 = open("bin\\test.txt", "w", encoding="utf-8") #note: adding 'b' to the read mode make it read/write as binary
f1.write("This is a test")
f1.close()

f1 = open("bin\\test.txt", "r", encoding="utf-8")
print("This is what's in the file:\"" + f1.read() + "\"") #noteL read() returns '' when EOF reached
f1.close()
#some usefull methods for files:
# close()
# readable()
# seek(offset, whence=SEEK_SET|SEEK_CUR|SEEK_END)

#some basic stuff on reading webpages
import urllib.request #for url stuff
webpageObject = urllib.request.urlopen("http://www.google.com/robots.txt")
data = (webpageObject.read()).decode('utf-8')
print("Data from www.google.com/robots.txt:\n"+data)
