/* a comment */	/* using '//' is risky as different compilers might not recognize it as a comment */
/* the "\" is the escape characture

#include <stdio.h> /* a basic includ statment, it litteraly copys the text line by line to the this file, then compiles it */
#include <string.h>

int main(int argc, char **argv){ /* usualy argc is for the number of arguments, and argv is an array of strings, the first arg is always the program itself */		
	
	printf("string %s, number1 %d, number2 %05d, hex %x, float %5.2f, unsigned value %u.\n", "Hello?", 123456, 89, 255, 3.14159, 250); /* showing how printf works */
	/* note: printf DOESN'T auto-print a newline char */
	/* usual '\' is the escape character */
	
	
	/* true is represented by a non-zero number, false by a 0 */
	
	/* 'NULL' is used for pointers */
	
	return 0; /* all prorams must return something to the calling program, ususaly a 0 for a run without errors */
}

