An interprited scripting language that is dynamic
Easy to learn and program in
High level
indenting matters!

Development Stack:
    Windows: #Windows 10
        # install python
        Windows Store -> Python 3.X - Python Software Foundation
        $ python -m pip install --upgrade pip #upgrades pip to latest version
        #install windows terminal
        Windows Store -> Windows Terminal - Microsoft Corporation
            # Extentions: (File -> Preferences -> Extensions)
            $ code --install-extension    ms-python.python                #Python     Microsoft Python language general
            $ code --install-extension    ms-python.vscode-pylance        #Pylance    Microsoft python
    Linux: #Ubuntu
        # install python
            $ sudo apt install python3 #installs python, but should be included by default
            $ sudo apt install python3-pip
            $ python -m pip install --upgrade pip
        # install Microsoft Studio code
            $ sudo snap install code --classic #Microsoft Visual Studio Code, --classic because Snap updated, but Code did not [last checked 2020-12-13]
            # Extensions
                $ code --install-extension    ms-python.python            #Python     Microsoft Python language general
                $ code --install-extension    ms-python.vscode-pylance    #Pylance    Microsoft python

to run from command line:
    $ python program.py args

References:
    Python Documentation                https://docs.python.org/3/index.html
    The Python Language Reference       https://docs.python.org/3/reference/index.html
    The Python Standard Library         https://docs.python.org/3/library/index.html
    The Python Tutorial                 https://docs.python.org/3/tutorial/index.html
