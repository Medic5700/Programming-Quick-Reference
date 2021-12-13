A function based language, interprited.
a simple learning curve, easy to learn after that
start all source code with the "#lang scheme" to select the source language

Development Stack:
    Linux: # Ubuntu
        # Install Scheme
            $ sudo apt install racket
        # install Microsoft Visual Studio Code
            $ sudo snap install code --classic #--classic because this version breaks the normal snap sandbox, thus requiring the --classic override
            # Extensions: (File -> Preferences -> Extensions)
                $ code --install-extension    karyfoundation.racket            # Scheme-Racket     Random scheme-racket extension for syntax highlighting

Run:
    $ racket                    # starts interpriter
    $ racket helloWorld.rkt     # runs file

Reference:
    The Scheme Programming Language Fourth Edition        https://www.scheme.com/tspl4/
    https://racket-lang.org/
