/**
 * Author: 
 * Discription: describing variables and how to use them and such
 * what what with a crumpit on top
**/

#include <stdio.h>
#include <stdlib.h>
#define LENGTH 50 /* This insructs the compiler to replace the text of every occurence of "LENGTH" in this file with "50" */

struct structure1 {
	/* can include as many variables as desired */
	int blah1;
	float blah2;
	/* can use these variables by struct_name.blah1 = soemthing */
};

int main(){
	typedef int score;		/* can use typedef to change what it looks like in source code, it just makes it more readible, doesn't really do anything (IE: a cosmetic change) */
	score player = 5000;	/* here it is being used */	   
	
	/* some primatives */
	/* note: the number variables can have a prefex of 'short', 'long' */
	int primative1 = 0;	   /* signed and size is machine dependent */
	float primative2 = LENGTH;	 /* "LENGTH" has been replaced by "50" */
	char primative3;
	/* using a prefex of 'static' for a variable in a function call will essentialy make it similar to a global variable (IE: it will retain it's previouse value since the last time you called the function) */
	static int static_test;
		
	/* pointers */
	/* they are indicated with a '*' infront of the verible when declaring */
	/* they are also a variable type, they are that important! */
	char *pointers1 = (char*) malloc(sizeof(char)*LENGTH);	  /* malloc MUST be cast, and it takes in the number of bytes to be allocated, therefor sizeof is used, can be called with any type */
	int *pointers2 = (int*) calloc(LENGTH, sizeof(char));
	
	/* arrays */
	int array1[LENGTH]; /* makes an array numbered 0-49 */
	int *array2 = (int*) malloc(sizeof(int)*LENGTH);/* also makes an array, in a sense */
	int array3[3] = {1,2,3}; /* you can initialize arrays with curly brackets */
	
	int i;
	pointers2 = array2;

	for (i=0; i<LENGTH; i++){
		array1[i] = i*i;
		
		array2[i] = i*i;
		*pointers2 = i*i;
		pointers2++;
	}
	pointers2 = array2;
	
	/* strings, they are just an array of char */
	printf("%i\n", LENGTH);
	
	return 0;
}
