import java.io.*;
import java.util.*; //import the input scanner

public class io{
  public static void main(String[] args) throws Exception {
    //IO to and from console
    System.out.println("Hello World");
    System.out.print("Enter Number"); //print without explicidly going to a new line
    // http://pages.cs.wisc.edu/~hasti/cs368/JavaTutorial/NOTES/JavaIO_Scanner.html
    Scanner scanner = new Scanner(System.in);
    String number = scanner.nextLine(); //grabs the line as a string
    System.out.print("Enter Another Number");
    int number2 = scanner.nextInt(); //parses the string for the next number, but not neccisarily goes through the entire nextline (Be carefull)
    System.out.println("First input: " + number + "\nSecond input: " + number2);
    scanner.close();
    
    //File Write
    System.out.println("Writing to File");
    java.io.PrintStream f = new java.io.PrintStream( "bin\\test.txt" );
    f.print("test\ntest");
    f.close();
    
    //File Read
    System.out.println("Reading from File");
    Scanner inputFile = new Scanner(new File("bin\\test.txt"));
    while (inputFile.hasNext()){
      System.out.println(inputFile.nextLine());
    }
    inputFile.close();
  }
}

/**  
  //variuse forms of input
  Scanner input = new Scanner(System.in);
  //java.io.DataInput input2 = new java.io.DataInputStream(System.in);
  BufferedReader input3 = new BufferedReader(new InputStreamReader(System.in));
  
  int t1 = 5; //declaring a variable 
  String s1;
  System.out.println("regular text...\nnew line\ttab\n" + "a connication of some text " + 5 + "...including numers\nnow for a random char \"\u00BC \""); //printing a line
  System.out.print("Now printing a line without going to the next line... Enter a intiger number:"); //also printing a line
  t1 = input.nextInt(); //input, specifically getting the next integer from inputed sting
  //t1 = Integer.parseInt(input.readLine());
  //input.reset();
  System.out.print("Enter your name");
  s1 = input.nextLine();
  
  //formating output (a bit)
  java.text.DecimalFormat arbitraryFormat = new java.text.DecimalFormat("$#.000");
  System.out.println("\nYour entered number was: " + arbitraryFormat.format(t1) + "\t" + s1);
  
  input.close(); //closes the input stream, mostly reqired for handeling files
  //t1.free();
  **/
