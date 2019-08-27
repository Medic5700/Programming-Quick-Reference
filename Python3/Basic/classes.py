class InstanceClass:
    """This class can be instatiated, note that all functions have 'self' as the first arg, and it there is an '__init__' function"""
    # https://docs.python.org/3/reference/datamodel.html#basic-customization
    def __init__(self):
        """This is the function that gets called when the class is instantiated (IE: this is the constructor)"""
        # https://docs.python.org/3/reference/datamodel.html#object.__init__
        pass
    
    def __repr__(self):
        # https://docs.python.org/3/reference/datamodel.html#object.__repr__
        pass
    
    def __str__(self):
        # https://docs.python.org/3/reference/datamodel.html#object.__str__
        pass

class StaticClass:
    """This class will not be instatiated, note the lack of a '__init__' function, and functions do not have 'self' as their first argument"""
    def function1():
        pass
    
    def function2():
        pass

#inheritance
