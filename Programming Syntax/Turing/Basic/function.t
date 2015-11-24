var t3 : int := 5
procedure a1 (t1, t2 : int)
    %runs a bunch of instruction with some input (if required)
    %doesn't return anything
    put t1
    put t2
    put t3 %note, varuables decleared outside procedure/function are accesible iff said variable is declared before procedure
end a1

function a2 (t1, t2 : int) : int
    %just like 'procedure', only it returns a value (that must be specified)
    result t1 * t2
end a2

a1 (1, 2)
put a2 (3, 4)
