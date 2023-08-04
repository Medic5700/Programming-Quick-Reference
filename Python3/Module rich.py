"""
Rich Terminal Text

Installation:
    $ pip3 install rich
    Verify
    $ python3 -m rich

References:
    https://github.com/willmcgugan/rich
    https://rich.readthedocs.io/en/latest/index.html
    https://www.youtube.com/watch?v=4zbehnz-8QU
    https://pypi.org/project/rich/

Examples/Demos:
    $ python3 -m rich               #Test output, shows in general what it can do
    $ python3 -m rich.progress      #progress bar demo
    $ python3 -m rich.spinner       #spinner demo
    $ python3 -m rich.tree          #tree demo
    $ python3 -m rich.markup        #markup demo
    https://github.com/willmcgugan/rich/tree/master/examples
        Litterally a folder full of example programs

"""

from rich import inspect

inspect("test", methods=True) # Think of it like pythons built-in help(), but more usefull because it formats the help better instead of dumping a book onto the screen

#TODO https://www.willmcgugan.com/blog/tech/post/rich-tree/
