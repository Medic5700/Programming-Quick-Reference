#TODO inheritance
#TODO multi-inheritance
#TODO abstractmethods
#TODO super() # https://www.programiz.com/python-programming/methods/built-in/super

class InstanceClass:
    """This class can be instatiated, note that all functions have 'self' as the first arg, and it there is an '__init__' function"""
    # https://docs.python.org/3/reference/datamodel.html#basic-customization
    def __init__(self):
        """This is the function that gets called when the class is instantiated (IE: this is the constructor)"""
        # https://docs.python.org/3/reference/datamodel.html#object.__init__
        pass
    
    def __repr__(self):
        """This should return a valid python expression to remake this object"""
        # https://docs.python.org/3/reference/datamodel.html#object.__repr__
        pass
    
    def __str__(self):
        """This returns a nicly formated string that represents the object, but doesn't have to be a valid python expression

        This function is called by built-in print() to print the object"""
        # https://docs.python.org/3/reference/datamodel.html#object.__str__
        pass

    def __del__(self):
        """This is a deconstructor called when this object is going to be deleted
        
        This function is called by built-in del"""
        # https://docs.python.org/3/reference/datamodel.html#object.__del__

    # Other "Dunder (Magic) Methods" =======================================================================

    #comparison stuff https://docs.python.org/3/reference/datamodel.html#object.__lt__
    def __lt__(self, other):
        pass
    def __le__(self, other):
        pass
    def __eq__(self, other):
        pass
    def __ne__(self, other):
        pass
    def __gt__(self, other):
        pass
    def __ge__(self, other):
        pass

    #container type stuff https://docs.python.org/3/reference/datamodel.html#emulating-container-types
    def __len__(self):
        pass
    def __getitem__(self, key): 
        #x = self[key]
        pass
    def __setitem__(self, key, value):
        #self[key] = x
        pass

class StaticClass:
    """This class will not be instatiated, note the lack of a '__init__' function, and functions do not have 'self' as their first argument"""
    def function1():
        pass
    
    def function2():
        pass

#TODO stuff on actually instantiating the class
#TODO stuff on the self.super() function (IE: calling the superclass of a class during instatiation of a class to return an oject that is an instantiated instance of the superclass)
