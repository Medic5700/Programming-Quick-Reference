#include <stdio.h>
#include <string.h>

int main(int argc, char **argv){
	int i = 0;
	for (i=0;i<10;i++){
		printf("Loop 0 iteration %i\n",i);
	}
	
	i=0;
	while (i<10){
		printf("Loop 1 iteration %i\n",i);
		i++;
	}
	
	i=0;
	do{
		printf("Loop 2 iteration %i\n",i);
		i++;
	}while (i<10);
	
	/*breaks*/
	
	i=0;
	while(1){
		if(i==10){
			break;
		}
		printf("Loop 3 iteration %i\n",i);
		i++;
	}
	
	i=0;
	while(1){
		printf("Loop 4 iteration %i\n",i);
		i++;
		if(i<10){
			continue;
		}
		break;
	}	 
	return 0;
}
