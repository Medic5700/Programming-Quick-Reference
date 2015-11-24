public class loop {
  public static void main(String[] args) throws Exception {
    for(int i=0; i<10;i++){
      System.out.println("Loop 0 iteration " + i);
    }
    for(int i=0,j=1; (i<10) && (j<1024); i++,j=j*2){ //you can iterate multiple variables in one loop
      System.out.println("Loop 1 iteration " + i + " - " + j);
    }
    
    Integer[] myArray = new Integer[3]; 
    myArray[0]=0; //assiging values to avoid null pointer exception
    myArray[1]=0;
    myArray[2]=0;
    int i = 0;
    for (int j: myArray){ //this will iterate over a list.
      j = i*i;
      System.out.println("Loop 2 iteration " + i + " - " + j);
      i++;
    }
    
    i = 0;
    while (true) { //while loop
      if (i==10){
        break;
      }
      System.out.println("Loop 3 iteration " + i);
      i++;
    }
    
    i = 0;
    do{ //do-while loop
      System.out.println("Loop 4 iteration " + i);
      i++;
    } while(i<10);
  }
}