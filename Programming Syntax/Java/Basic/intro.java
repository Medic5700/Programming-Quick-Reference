import java.io.*;
import java.util.*; //import the input scanner

public class intro { //The class name must be the same name as the file
 /**
  * Block Comment
  */
 //the '//' allows for regular comments
 //the "\" is the escape characture, usual escape characters apply
 public static void main(String[] args) throws Exception {
  /**
   * This is the main string, it is the main part of the program the the computer will run (denoted by the 'main')
   * the throws exception is error handling (not needed)
   **/
  System.out.println("Hello World\n\n"); //REMEMBER THE SEMICOLEN!
  
  //the repesentations of true,false,null
  System.out.println(true);
  System.out.println(false);
  System.out.println((String)null); //casted to string to print
  
  //accessing args passed in
  System.out.println(args.length);
   
 }
}
