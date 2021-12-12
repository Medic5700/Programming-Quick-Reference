don't use tabs
functional programming

Development Stack:
	Linux: # Ubuntu
		# install Haskell
			$ sudo apt install ghc #installs haskell interactive interpriter
		# install Microsoft Visual Studio Code
            $ sudo snap install code --classic #--classic because this version breaks the normal snap sandbox, thus requiring the --classic override
            # Extensions
				$ code --install-extension    haskell.haskell                     # Heskell       Heskell language

run:
    for interpriter use $ ghci
    Prelude> :load filename -- to load/interprite file
    Prelude> :reload -- to reload currently loaded file
    Prelude> :quit

compile:
    $ ghc HelloWorld.hs