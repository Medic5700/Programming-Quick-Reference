#imports functions from other files
#can be used for on the fly importing
modules = []
for i in ["factorial","fib"]: # http://stackoverflow.com/questions/951124/dynamic-loading-of-python-modules
    modules.append(__import__(i))
    
print(modules[0].factorial(5))
print(modules[1].fib(5))