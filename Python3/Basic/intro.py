'''block comment'''
#another comment
"""A docstring""" #this should only be used in functions, but it's here to show what it is ahead of time
import sys
import getopt

if __name__ == '__main__': #used to signify the main of a program, good practice but not necissary
    #indentation matters
    print("Hello World\n\n") # '\' is an escape character, all usual escape characters apply

    #note, to use these, they are case sensitive
    print(True)
    print(False)
    print(None) #'None' is the equivilent of null
    if (True):
        pass #a do nothing statment, litterally does nothing, but used so it doesn't break the parser

    #===========================================================================
    
    #access the arguments the old way
    #uses import sys
    print(sys.argv) #prints the list of args including running programs
    
    #another way to handle command line options
    # http://docs.python.org/2/library/getopt.html
    #uses import getopt
    try:
        opts, args = getopt.getopt((sys.argv[1:]),'h')
        #second argument is for which arguments to look for, one's that require an argument after an option must go after a ':'
        #opts is argument pairs, as parsed by getopt
        #args is everything else after the stuff you're looking for
    except getopt.GetoptError:
        print("argument error")
        sys.exit(2)
    for o, a in opts: #an example of using the options
        if o == "-h":
            print("some help text")
    print(opts)
    print(args)

    #===========================================================================

    #some keyword stuff
    assert 2 == 2 #asserts a logic statement, and throws an error if false. C
    #an be used during development to check that variables are holding expected values. Some runtime optimizations allow the ignoring of assertions while interpriting.

    #===========================================================================

    #you can implicidly not end a line using brackets, commas, etc
    print(
        "Implicid",
        "not end line"
        )

    #you can explicidly not end a line using the '\' at the end of a line
    print("Explicid" \
          + " not end line" \
          )
