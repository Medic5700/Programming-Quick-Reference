An interprited scripting language that is dynamic
Easy to learn and program in
High level
indenting matters!

Development Stack:
    Windows: # Windows 10
        # install python
            Windows Store -> Python 3.X - Python Software Foundation # Currently using Python 3.8
            $ python -m pip install --upgrade pip #upgrades pip to latest version
        # install windows terminal, because proper ANSI support
            Windows Store -> Windows Terminal - Microsoft Corporation
        # install Microsoft Visual Studio Code
            Windows Store -> Visual Studio Code - Microsoft Corporation
            # Extensions: (File -> Preferences -> Extensions)
                $ code --install-extension    ms-python.python                # Python     Microsoft Python language general
                $ code --install-extension    ms-python.vscode-pylance        # Pylance    Microsoft python
    Linux: # Ubuntu
        # install python, python is included in Ubuntu by default
            $ sudo apt install python3 #installs python, but should be included by default
            $ sudo apt install python3-pip
            $ python -m pip install --upgrade pip
            $ sudo apt install python3-tk   #optional, GUI graphical stuff, included in the windows version by default, not included in the linux distribution by default
        # install Microsoft Visual Studio Code
            $ sudo snap install code --classic #--classic because this version breaks the normal snap sandbox, thus requiring the --classic override
            # Extensions: (File -> Preferences -> Extensions)
                $ code --install-extension    ms-python.python                # Python     Microsoft Python language general
                $ code --install-extension    ms-python.vscode-pylance        # Pylance    Microsoft python

to run from command line:
    $ python program.py args

References:
    Python Documentation                https://docs.python.org/3/index.html
    The Python Language Reference       https://docs.python.org/3/reference/index.html
    The Python Standard Library         https://docs.python.org/3/library/index.html
    The Python Tutorial                 https://docs.python.org/3/tutorial/index.html
