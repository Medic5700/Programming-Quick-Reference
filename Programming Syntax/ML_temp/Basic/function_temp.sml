fn x => x + 1; (* an unnamed function *)
fun function1 x => x + 1; (* binding a name to a fucntion *)
fun function2 (x,y) => x+y;

(* pattern matching *)
fun function3 ([],[]) => 

fun fucntion4 (_,_) =>

fun even 0 = true
  | even x = odd (x - 1)
and odd 0 = false
  | odd x = even (x - 1);