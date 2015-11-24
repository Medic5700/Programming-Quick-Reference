%recursion isn't possible in Turing, so using loops instead

function factorial (t1 : int) : int
    var t2 : int := 1
    for i : 1 .. t1
        t2 := t2 * i
    end for
    result t2
end factorial

for i : 0 .. 10
    put i, "!\t= ", factorial (i)
end for
