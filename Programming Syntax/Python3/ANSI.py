'''
Prints using ANSI escape codes to colour apply colours and effects to text
This was tested in the Ubuntu Terminal, other terminal support varies
https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python
http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html
'''

for i in range(0,128):
	code = '\33[' + str(i) + 'm' #this is the ANSI escape code
	text = '\\33[' + str(i) + 'm'
	end = '\33[0m' #this is the ANSI escape code terminator
	print(code + text.ljust(10) + end, end='')
	print("") if (i%8 == 7) else None
print("")

#you can also combine multiple codes together like the following
print('combining multiple ANSI codes together')
print('\33[4;5;31;47m Hello World \33[0m')

#TODO some stuff on moving the curser around
