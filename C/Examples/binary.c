/**
 * Authour: Medic5700
 * 
 * Convert a int to a string of binary, and a string of binary to an int
**/

#include<stdio.h>
#include<stdlib.h>

void binary (int t1, char *t2){
	int i;
	for (i=31; i>=0; i--){
		t2[i] = ((t1 & 1) + '0');
		t1 = t1 >> 1;
	}
	t2[32]=0;
}

int number(char* t1){
	int t2 = 0;
	int i;
	for (i=0; i<32; i++){
		t2 = t2 << 1;
		if (t1[i] == '1')
			t2 = t2 + 1;
	}
	return t2;
}

int main(){
	int i;
	char *binaryString = (char *) malloc(33 * sizeof(char));
	for (i=0; i<=255; i++){
		binary(i, binaryString);
		printf("%d\t=\t%s\t=\t%d\n", i, binaryString, number(binaryString));
	}
	free(binaryString);
	return 0;
}
