Power shell is a CUI, and has many similar properties to various shells
Unlike many shells, instead of passing information as text between various programs, it passes objects between programs
Powershell is a scripting language
Shares a lot of aliases with bash (in linux) and the cmd (in windows)
pipping stuff through "Get-Member" command will be your new best friend when you get started

Note:
    powershell shares many aliases with bash (IE: 'ls' is an alias to list the files in a directory)

Development Stack:
    Windows: # Windows 10
        # included by default in windows
        # install Microsoft Visual Studio Code
            Windows Store -> Visual Studio Code - Microsoft Corporation
            # Extensions: (File -> Preferences -> Extensions)
                $ code --install-extension      ms-vscode.powershell                # Powershell    Microsoft Powershell Language Support for VIsual Studio Code

Running:
    Powershell by default restricts running powershell scripts. To set it to run local scrips, run
        $ Set-Executionpolicy -Scope CurrentUser remotesigned
    Powershell is an interpriter, no compiling required
