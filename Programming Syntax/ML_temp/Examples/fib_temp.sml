fun fib 0 = 0
  | fib 1 = 1
  | fib n = fib (n-1) + fib (n-2);

val temp = map fib [0,1,2,3,4,5,6,7,8,9,10];
