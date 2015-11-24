import java.util.*;

public class variables {
 static int z1 = 0;//the static means 'static, or class level'
 
 public static void main(String[] args) { 
  //the primitive variable types
  byte i1 = Byte.MAX_VALUE;
  short i2 = Short.MAX_VALUE;
  int i3 = Integer.MAX_VALUE; //regular integer values
  long i4 = Long.MAX_VALUE;
  float f1 = 1/2; //decimal numbers
  double f2 = Math.PI; //Handles decimal numbers with more precision then float
  char s1 = 'h'; //character
  final boolean b1 = false;//the 'final' makes it a constant
  
  String s2 = new String("test"); //the constructor on the right is normally implied when you use the below line
  String s3 = "test"; //IE: this means the same as above
  
  //time for some math...
  int t1 = 101, t2 = 7;
  double t3 = 2f; //the 'f' in '2f' makes the constant '2' a float
  double t4 = 0.125;
  
  //arrays, zero indexed
  int[][] intArray = new int[5][6];
  for (int i = 0;i<intArray.length;i++){
   for (int j = 0;j<intArray[i].length;j++){
    intArray[i][j] = i*j;
    System.out.println("array value at position i=" + i + "\tj=" + j + "\t = " + intArray[i][j]);
   }
  }
  System.out.println(intArray); //Note: prints the reference to the array, not the contents of the array

  //array lists (ArrayList) - an array whos size can be changed and etc
  // http://javarevisited.blogspot.ca/2011/05/example-of-arraylist-in-java-tutorial.html
  ArrayList listArray = new ArrayList();
  for(int i = 0; i<=10;i++){
   listArray.add(i);
  }
  System.out.println("size of listarray: " + listArray.size());
  listArray.remove(3); //removing elements
  listArray.remove(2);
  System.out.println("size of listarray: " + listArray.size());
  for(int i=0; i<listArray.size();i++){
    System.out.println("Content of listarray[" + i + "]: " + listArray.get(i));
  }
  
  //'HashMaps', also known as 'dictionaries'
  java.util.HashMap<Character, Double> hashBrown= new java.util.HashMap<Character, Double>();
  for (char i='a';i<='j';i++){
   hashBrown.put(i,(double)i);
  }
  if (hashBrown.containsKey(s1)){
   System.out.println("hash map contrains key: \"" + s1 + "\" and value: \"" + hashBrown.get(s1) + "\"");
   System.out.println("\tand contains: \"" + hashBrown.size() + "\" elements");
  }
  System.out.println("hash map not empty = " + hashBrown.isEmpty());
 }
}
