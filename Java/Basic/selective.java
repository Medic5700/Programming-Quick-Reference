public class selective {
  public static void main(String[] args) throws Exception {
    /**
     * "|" the OR operator 
     * "&" the AND operator
     * "^" the XOR operator
     * "!" the NOT operator
     * "||" the short-circuit OR operator
     * "&&" the short-circuit AND operator
     * "==" the EQUAL TO operator
     * "!=" the NOT EQUAL TO operator
     * "?:" the IF-THEN-ELSE operator
     * "<", ">", "<=", ">=", "!=" the usual math comparisons
     **/
    for(int i=0; i<10;i++){
      if (i == 0){
        System.out.println("if statement 0 option 0");
      }
      else if (i == 1){
        System.out.println("if statement 0 option 1");
      }
      else{
        System.out.println("if statement 0 option 2");
      }
    }
    
    for(int i=0; i<10;i++){
      System.out.println((i<4)?"if statment 1 option 0":"if statment 1 option 1"); //simple boolean if/else that RETURNS something
    }
    
    for(int i=0; i<10;i++){ //switch
      switch(i){
        case 0: System.out.println("if statement 2 option 0"); break;
        case 1: System.out.println("if statement 2 option 1"); break;
        case 2: System.out.println("if statement 2 option 2"); //notice, without break, case 2 exicutes case 3 and default as well
        case 3: System.out.println("if statement 2 option 3");
        default:System.out.println("if statement 2 option 4");
      }
    }
  }
}