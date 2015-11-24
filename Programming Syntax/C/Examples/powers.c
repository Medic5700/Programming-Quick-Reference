/**
 * Authour: 
 * Discription: Print all the powers of 2, from 0 to 20
**/
#include<stdio.h>
int main(){
	int i;
	int t1=1;
	for (i=0;i<=20;i++){
		printf("2^%d\t=\t%d\n", i, t1);
		t1=t1*2;
	}
	
	return 0;
}
