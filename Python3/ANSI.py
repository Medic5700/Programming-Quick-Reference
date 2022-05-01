'''
Prints using ANSI escape codes to colour apply colours and effects to text
This was tested in the Ubuntu Terminal, other terminal support varies
https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python
http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
https://tintin.sourceforge.io/info/ansicolor/
'''
# note: can use "\33[{xyz}m" or "\u001b[{xyz}m" since it's 'ESC' in ASCII, represented in Octal or Hexadecimal respectivly

for i in range(0,128):
	code = '\33[' + str(i) + 'm' # this is the ANSI escape code
	text = '\\33[' + str(i) + 'm'
	end = '\33[0m' # this is the ANSI escape code terminator
	print(code + text.ljust(10) + end, end='')
	print("") if (i%8 == 7) else None
print("")

# you can also combine multiple codes together like the following
print('combining multiple ANSI codes together')
print('\33[4;5;31;47m Hello World \33[0m')
print("")

'''
On the Ubuntu Terminal (where this was tested) it works as inteneded
On the Windows Powershell Terminal, more effort is required
you can use "> python ANSI.py | Out-Host" for it to display properly
See also https://stackoverflow.com/questions/51680709/colored-text-output-in-powershell-console-using-ansi-vt100-codes
'''
#TODO test colorama module support for Windows

'''
256 (8-bit) colours, support varies
'''
print("256 (8-bit) text colours of the form \\u001b[38;5;{n}m")
for i in range(256):
        code = '\u001b[38;5;' + str(i) + 'm'
        end = '\33[0m'
        print(code + str(i).ljust(4) + end, end='')
        print("") if (i%20 == 19) else None
print("\n")

print("256 (8-bit) background colours of the form \\u001b[48;5;{n}m")
for i in range(256):
        code = '\u001b[48;5;' + str(i) + 'm'
        end = '\33[0m'
        print(code + str(i).ljust(4) + end, end='')
        print("") if (i%20 == 19) else None
print("\n")

'''
Full RGB (24-bit) Colour, support is spotty? Tested on:
Ubuntu Terminal
'''
print("RGB (24-bit) Text Colours of the form \\u001b[38;2;{r};{g};{b}m")
for i in range(256):
	code = '\u001b[38;2;' + str(i) + ';0;0m'
	end = '\u001b[0m'
	print(code + "8" + end, end='')
for i in range(256):
	code = '\u001b[38;2;255;' + str(i) + ';0m'
	end = '\u001b[0m'
	print(code + "8" + end, end='')
for i in range(256):
	code = '\u001b[38;2;255;255;' + str(i) + 'm'
	end = '\u001b[0m'
	print(code + "8" + end, end='')
for i in range(256):
	code = '\u001b[38;2;' + str(255-i) + ';255;255m'
	end = '\u001b[0m'
	print(code + "8" + end, end='')
for i in range(256):
	code = '\u001b[38;2;0;' + str(255-i) + ';255m'
	end = '\u001b[0m'
	print(code + "8" + end, end='')
for i in range(256):
	code = '\u001b[38;2;0;0;' + str(255-i) + 'm'
	end = '\u001b[0m'
	print(code + "8" + end, end='')
print("")


print("RGB (24-bit) Background Colours of the form \\u001b[48;2;{r};{g};{b}m")
for i in range(256):
	code = '\u001b[48;2;' + str(i) + ';0;0m'
	end = '\u001b[0m'
	print(code + " " + end, end='')
for i in range(256):
	code = '\u001b[48;2;255;' + str(i) + ';0m'
	end = '\u001b[0m'
	print(code + " " + end, end='')
for i in range(256):
	code = '\u001b[48;2;255;255;' + str(i) + 'm'
	end = '\u001b[0m'
	print(code + " " + end, end='')
for i in range(256):
	code = '\u001b[48;2;' + str(255-i) + ';255;255m'
	end = '\u001b[0m'
	print(code + " " + end, end='')
for i in range(256):
	code = '\u001b[48;2;0;' + str(255-i) + ';255m'
	end = '\u001b[0m'
	print(code + " " + end, end='')
for i in range(256):
	code = '\u001b[48;2;0;0;' + str(255-i) + 'm'
	end = '\u001b[0m'
	print(code + " " + end, end='')
print("")

#TODO some stuff on moving the curser around
'''
Up: \u001b[{n}A moves cursor up by n
Down: \u001b[{n}B moves cursor down by n
Right: \u001b[{n}C moves cursor right by n
Left: \u001b[{n}D moves cursor left by n

Next Line: \u001b[{n}E moves cursor to beginning of line n lines down
Prev Line: \u001b[{n}F moves cursor to beginning of line n lines down

Set Column: \u001b[{n}G moves cursor to column n
Set Position: \u001b[{n};{m}H moves cursor to row n column m

Clear Screen: \u001b[{n}J clears the screen ◦n=0 clears from cursor until end of screen,
n=1 clears from cursor to beginning of screen
n=2 clears entire screen

Clear Line: \u001b[{n}K clears the current line
n=0 clears from cursor to end of line
n=1 clears from cursor to start of line
n=2 clears entire line

Save Position: \u001b[{s} saves the current cursor position
Save Position: \u001b[{u} restores the cursor to the last saved position
'''
