/**Discription
 * Auther       : 
 * Purpose      : fib and factorial example, not using recursion (recursion is not possible in Turing
 **/
%note: "procedure" is a function definition that doesn't return anything
function fib (t1 : int) : int
    var t2 : int := 0
    var t3 : int := 1
    var temp : int
    for i : 1 .. t1
	temp := t2 + t3
	t2 := t3
	t3 := temp
    end for
    result t2
end fib

function factorial (t1 : int) : int
    var t2 : int := 1
    for i : 1 .. t1
	t2 := t2 * i
    end for
    result t2
end factorial

for i : 0 .. 10
    put i, "!\t= ", factorial (i), "\t\tfib(", i, ")\t= ", fib (i)
end for
