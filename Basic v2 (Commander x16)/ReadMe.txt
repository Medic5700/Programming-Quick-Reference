BASIC is a highlevel programming language from the 70s.
Popular on many machines including the Commador 64.
Will focus on the "Commander x16" environment on Ubuntu for ease of use reasons, even if it is currently under development.
Note: The Commander x16 uses PETSCII instead of ASCII (see "C64 Petscii Charts.png" taken from https://upload.wikimedia.org/wikipedia/commons/c/c4/C64_Petscii_Charts.png )

Getting started:
	Commander x16 setup:
		GOTO https://github.com/commanderx16/x16-emulator
		Find releases and download (https://github.com/commanderx16/x16-emulator/releases)
		extract and run "x16emu"
	Running:
		Read the ReadMe (https://github.com/commanderx16/x16-emulator/blob/master/README.md)
		$ ./x16emu
		$ ./x16emu -bas HelloWorld.bas 	#loads an ascii BASIC file and auto types it into the emulator
		$ ./x16emu -prg test.prg 	#loads an assembly program (a ROM) and injects it into memory

		#loading from inside the emulator, the "LOAD" and "SAVE" commands are intercepted allowing you to use the host file system
		] LOAD"$
		] LIST		#will show list of files in working directory
		] LOAD"TEST.PRG	#will load the rom
		
		] LOAD"HELLOWORLD.BAS	#will load a tokonized version of the BASIC program (not plain ascii), note: the emulator has trouble handling lowercase characters in file names, so use uppercase for file names
		SAVE"HELLOWORLD.BAS	#will save a tokonized version of the BASIC program (not plain ascii)

		#can alternativly use Ctrl+V to paste a basic program into the emulator

Reference:
	https://www.c64-wiki.com/wiki/Category:BASIC-Command


	#Other BASIC interpriters
	YaBasic:
		$ sudo apt install yabasic #a BASIC interpriter
	Commodore 64 Emulator (VICE):
		# This will install the emulator except for the kernal ROM
		$ sudo apt-get install vice
		
		#getting the kernal ROMS, which are included in the sorce code
		# http://iseborn.eu/wiki/index.php?title=Ubuntu/Install_and_set_up_VICE
		# Go to the directory where the system files are located, /usr/lib/vice. 
		# Create a temporary directory to work in, and enter it. 
		# Download the source file package for VICE ans unpack it in the temporary directory. 
		# Copy the relevant system ROMs from the unpacked source package to the appropriate system file directories. 
		$ cd /usr/lib/vice
		$ sudo mkdir temp
		$ cd temp
		$ sudo wget http://www.zimmers.net/anonftp/pub/cbm/crossplatform/emulators/VICE/vice-2.4.tar.gz
		$ sudo tar vzxf vice-2.4.tar.gz
	 
		# Copy the C64-specific system ROMs
		$ cd /usr/lib/vice/temp/vice-2.4/data/C64/
		$ sudo cp basic chargen kernal /usr/lib/vice/C64/
		 
		# Copy the common drive ROMs
		$ cd /usr/lib/vice/temp/vice-2.4/data/DRIVES/
		$ sudo cp d1541II d1571cr dos* /usr/lib/vice/DRIVES/
		 
		# Copy the common printer ROMs
		$ cd /usr/lib/vice/temp/vice-2.4/data/PRINTER/
		$ sudo cp cbm1526 mps801  mps803 nl10-cbm /usr/lib/vice/PRINTER/	

		# removing temporary files
		$ cd /usr/lib/vice/
		$ sudo rm -rf temp

