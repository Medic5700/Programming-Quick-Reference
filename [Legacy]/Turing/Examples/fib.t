%recursion isn't possible in Turing, so using loops instead

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

for i : 0 .. 10
    put "fib(", i, ")\t= ", fib (i)
end for