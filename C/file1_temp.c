/**
 * Authour:
 * open a file, write to a file, read from a file
**/

#include <stdio.h>

int writefile (FILE *filestream, int *array){
	fwrite(array, sizeof(int), 50, filestream);
	return 0;
}

int readfile (FILE *filestream, int *array){
	fread(array, sizeof(int), 50, filestream);
	return 0;
}

int main (int argc, char **argv){
	FILE *filestream;
	int array[50];
	int i;
	
	for (i=0; i<50; i++)
		array[i]=i*50;
		
	filestream = fopen("temp.txt", "w");
	writefile (filestream, array);
	fclose(filestream);
	
	filestream = fopen("temp.txt", "r");
	readfile (filestream, array);
	fclose(filestream);
	
	for (i=0; i<50; i++)
		printf("%i\n", array[i]);
	
	return 0;
}
