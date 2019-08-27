fun factorial 0 = 1
  | factorial n = n * factorial (n-1);

fun factorial2 n = 
  if n = 0 then 1 else n * factorial2 (n-1);

val temp = map factorial [0,1,2,3,4,5,6,7,8,9,10];
