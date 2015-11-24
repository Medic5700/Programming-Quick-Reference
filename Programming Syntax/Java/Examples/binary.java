public class binary {

 /**
 * Authour:Miles Dias
 * convert a int to a string of binary, and a string of binary to an int
 < Effiecientcy:processing = 4 >
 < Effiecientcy:memory  = 4 >
 < Reliability   = 3 >
 < Simplicity   = 3 >
 < Modularity   = N/A >
 < Readability   = 4 >
 **/  
  
 public static void main(String[] args) {
  for (int i=0;i<=255;i++)
   System.out.println(i + "\t=\t" + binary(i) + "\t=\t" + number(binary(i)));
 }

 public static String binary(int t0){
  String t1 = "";
  for (int i=0;i<32;i++){
   if (t0%2==0)
    t1 = "0" + t1;
   else
    t1 = "1" + t1;
   t0 = t0 / 2;
  }
  return t1;
 }
 
 public static int number(String t1){
  int t2 = 0;
  for (int i=0;i<32;i++){
   t2 = t2*2;
   if (t1.charAt(i)=='1')
    t2 = t2 + 1;
  }
  return t2;
 }
}
