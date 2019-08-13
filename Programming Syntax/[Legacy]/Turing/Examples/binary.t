/**
 *Auther:
 *convert int to binary string, binary string to int
 **/

function binary (t0 : int) : string
    var t1 : int := t0
    var t2 : string := ""
    for i : 1 .. 32
	if (t1 mod 2) = 1 then
	    t2 := "1" + t2
	else
	    t2 := "0" + t2
	end if
	t1 := t1 div 2
    end for
    result t2
end binary

function number (t0 : string) : int
    var t1 : int := 0
    for i : 1 .. 32
	t1 := t1 * 2
	if t0 (i) = '1' then
	    t1 := t1 + 1
	end if
    end for
    result t1
end number

setscreen ("text")
for i : 0 .. 255
    put intstr (i), "\t=\t", binary (i), "\t=\t", number (binary (i))
end for
