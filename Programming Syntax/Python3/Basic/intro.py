'''block comment'''
#another comment

if __name__ == '__main__': #can be used to signify the main of a program
    #indentation matters
    print("Hello World\n\n") # '\' is an escape character, all usual escape characters apply

    #note, to use these, they are case sensitive
    print(True)
    print(False)
    print(None) #'None' is the equivilent of null
    pass #a do nothing statment, litterally does nothing, but used so it doesn't break the parser
    
    #access the arguments the old way
    import sys
    print(sys.argv) #prints the list of args including running programs
    
    #a better way to handle command line options
    # http://docs.python.org/2/library/getopt.html
    import getopt
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
