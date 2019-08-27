public class fib {
 public static void main(String[] args) {
  for (int i=0;i<=10;i++){
   System.out.println("fib(" + i + ")\t= " + fib(i));
  }
 }
 public static int fib (int t1){
  if (t1 == 0)
   return 0;
  else if (t1 == 1)
   return 1;
  else
   return fib(t1-1) + fib(t1-2);
 }
}