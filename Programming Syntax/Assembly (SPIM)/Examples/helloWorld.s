	.data	#Miles Dias
hello:	.asciiz	"Hello World\n"
	.text
main:	la	$a0,	hello
	li	$v0,	4
	syscall
end:	li	$v0, 10		#program terminate
	syscall
