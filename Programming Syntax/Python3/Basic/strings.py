string1 = 'Hello'
string2 = "Hello" #you can use both single quotes or double quotes for strings (don't mix them up)
print("Hello\nWorld") # '\' is the escape character

print(r"Hello\nWorld") #can use a "raw string" by appending an 'r' before the first quote, escape characters in the string are not treated as escape characters

#this is also valid, when wanting to print multi-line strings...
print('''Hello World
this is a test
but I don't want this line to start a new line \ 
so I escape the endline character''')

print("test" + "123") #string concatination
print("test" "123") #this is also string concatination... but only works because these are two string litterals, and no variables

#strings can also be accessed as an array
helloWorld = "Hello World"
for i in range(len(helloWorld)*2):
    print(helloWorld[i-len(helloWorld)])
print(helloWorld[1]) #just like an array
print(helloWorld[-1]) #unlike an array, you can use negative indexes to access the end of the string to the beginnning

print(helloWorld[1:5]) #slicing is supported
print(helloWorld[:5]) #this is valid, will print from beginning of string to [5]
print(helloWorld[1:]) #this is valid, will print from [1] to end of string
print(helloWorld[-2:]) #this is valid, will print from second last character to end of string

#helloWorld[5] = "2" #this won't work, as these string are immutable

#some usefull string methods
# https://docs.python.org/3/library/stdtypes.html#string-methods
print("Hello World".find("World")) # str.find(sub[, start[, end]]) Return -1 if sub is not found.
print("Hello World".rfind("World")) # str.rfind(sub[, start[, end]]) Return -1 on failure.
print("Hello World".index("World")) # str.index(sub[, start[, end]]) Like find(), but raise ValueError when the substring is not found.
print("Hello World".rindex("World")) # str.rindex(sub[, start[, end]]) Like rfind() but raises ValueError when the substring sub is not found.
print("Hello World".split(" ")) # str.split(sep=None, maxsplit=-1)
print("Hello World".strip("HeWld")) #Return a copy of the string with the leading and trailing characters removed. The chars argument is a string specifying the set of characters to be removed. If omitted or None, the chars argument defaults to removing whitespace.

#string formating
print("A number: " + str(1/7))
print("A number: " + str(5))
print("A number: " + str(5).rjust(5))
print("A number: " + str(5).ljust(5))
print("A number: " + str(5).center(5))
print("A number: " + str(5).zfill(5))
#string.format
print("Some Numbers: {0} {1} {2}".format(1,2,3)) #in the string, stuff between the '{}' is where the replacements occur
print("Some Numbers: {2} {1} {0}".format(1,2,3)) #the numbers in '{}' refer the to position of the argument passed to format
print("Some Numbers: {t1} {t2} {t3}".format(t1=1, t2=2, t3=3)) #keyword arguments work
print("An Array: {0!s}".format([1,2,3])) #'!s' or '!a' allows casting the variable with str() or ascii(), respectivly
print("A Number: {0:.4f}".format(100/7)) #adding ':' allows for further formating, in this case, rounding to 4 placed after the decimal
print("A Well Spaced Table: {0:8}{1:8.3f}{2:8d}".format(25,25/7,125)) #numbers after the ':' can specify minimum column width
