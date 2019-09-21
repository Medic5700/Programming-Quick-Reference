int main(){
	/* compairison operators
	 * "&&"	- and
	 * "||"	- or
	 * "!"	- not
	 * "=="	- euqal to
	 * "!="	- not equal to
	 * ">"	- greater then
	 * "<"	- less then
	 * ">="	- greater then or equal to
	 * "<="	- less then or equal to
	*/

	int i = 0;
	for (i=0 ;i<10 ;i++){
		if (i==0){
			printf("if statement 0 option 0\n");
		}
		else if (i==1){
			printf("if statement 0 option 1\n");
		}
		else {
			printf("if statement 0 option 2\n");
		}
	}
	for (i=0 ;i<10 ;i++){
		(i==0) ? printf("if statement 1 option 0\n") : printf("if statment 1 option 1\n");
	}
	for (i=0 ;i<10 ;i++){
		switch (i){
			case 0:
				printf("if statement 2 option 0\n"); /* a lack of break allows the next case to be exicuted */
			case 1:
				printf("if statement 2 option 1\n");
				break;
			case 2:
				printf("if statement 2 option 2\n");
			default:
				printf("if statement 2 option 3\n");
		}
	}
	return 0;
}
