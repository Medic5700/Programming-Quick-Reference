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
