/**
 * Authour: Medic5700
 * 
 * Print the fibonacci sequence
**/

#include<stdio.h>

int fib(int t1){
	if (t1==0){
		return 0;
	}
	else if(t1==1){
		return 1;
	}
	else
		return fib(t1-1) + fib(t1-2);
}
int main(){
	int i;
	for (i=0;i<=10;i++){
		printf("fib(%d)\t= %d\n",i,fib(i));
	}
	return 0;
}
