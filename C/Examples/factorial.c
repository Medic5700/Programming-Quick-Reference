/**
 * Authour: Medic5700
 * 
 * Print factorials
**/

#include<stdio.h>

int factorial(int t1){
	if (t1 > 1){
		return t1 * factorial(t1 - 1);
	}
	else{
		return 1;
	}
}
int main(){
	int i;
	for (i=0; i<=10; i++){
		printf("%d!\t= %d\n", i, factorial(i));
	}
	return 0;
}
