	.data	#The data section, for variables...
hello:	.asciiz	"Hello World\n"	#comments
	.text	#the 'main' section for instructions
main:	la	$a0,	hello
	li	$v0,	4
	syscall
end:	li	$v0, 10		#program terminate
	syscall