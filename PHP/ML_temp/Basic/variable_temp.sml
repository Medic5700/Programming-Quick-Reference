(*variable types
unit - the only member is ()
bool - booleans
int - integers
real - reals
string - strings
(<type_0>*<type_1>*...*<type_n>) - typles
<type> list - list
<input-type> -> <output-type> - functions
*)

val varint = 2; (* variable decliration *)
val varreal = 2.0;


varreal = real(2);
type vartest = real;
datatype number = R of real | I of int;

(* some stuff on arrays/tuples *)
val vartuple = ["test",1.0,2,3,4,5,6,7,8,9]; (* tuples NOT zero initialized *)
#2 vartuple; (* accesses the tuples's second element, only applys to tuples *)
val vararray = [0,1,2,3,4,5,6,7,8,9];
42::vararray; (* the '::' is a constructor, rememeber to append a 'nil' to the end of a list if you want to make it a list *)
vararray@vararry; (* the '@' combines two lists OF THE SAME TYPE together *)
hd vararray; (* the first element *)
tl vararray; (* the remaining elements *)

fun function1 x =>
  let
    fun temp (y::ys) => y*temp(ys)
      | temp [] = 0
  in
    temp x
  end;