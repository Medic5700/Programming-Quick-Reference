Low level, Fast
Compiling required
Requires knowledge of how to manage memory/memory pointers

Development Stack:
    Linux: # Ubuntu
        # gcc is included in Ubuntu by default
            $ sudo apt install build-essential #installs gcc, g++, make
        # install Microsoft Visual Studio Code
            $ sudo snap install code --classic #--classic because this version breaks the normal snap sandbox, thus requiring the --classic override
            # Extensions: (File -> Preferences -> Extensions)
                $ code --install-extension    ms-vscode.cpptools-extension-pack   # C/C++         Microsoft C/C++ Extension Pack

Compile source code:
    Linux: #Ubuntu
        $ gcc helloWorld.c -o helloWorld.exe
