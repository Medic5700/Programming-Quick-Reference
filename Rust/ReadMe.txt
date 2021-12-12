#TODO

Development Stack:
    Windows: # Windows 10
        # https://www.rust-lang.org/learn/get-started
        #TODO
    Linux: # Ubuntu
        # install rust
            $ sudo apt install curl
            $ curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
                # follow installer instructions
                # restart shell
            $ cargo --version           # check that it installed, should print something like "cargo 1.57.0 (b2e52d7ca 2021-10-21)"
            $ restup update stable      # updates rust
        # install Microsoft Visual Studio Code
            $ sudo snap install code --classic #--classic because this version breaks the normal snap sandbox, thus requiring the --classic override
            # Extensions: (File -> Preferences -> Extensions)
                $ code --install-extension      rust-lang.rust                          # Rust          Rust language general

Running:
    cargo new [name]    # create a new project with [name], will create a simple 'HelloWorld'
    cargo build         # build project
    cargo run           # run project

References:
    https://www.rust-lang.org/                                      # The main website
    https://play.rust-lang.org/                                     # A browser based IDE for playing with simple code, allows for compiling and executing code
    https://en.wikipedia.org/wiki/Rust_(programming_language)       # Wikipedia
    https://doc.rust-lang.org/book/                                 # The book
