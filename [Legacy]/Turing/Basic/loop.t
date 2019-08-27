for i : 0 .. 9 %inclusive!
    put "Loop 0 iteration ", i
end for

for decreasing i : 'j' .. 'a' %'decresing' can be used to count backwards
    %alternate itterators can be used, like letters in this example
    put "Loop 1 iteration ", i
end for

var i : int := 0
loop
    put "Loop 2 iteration ", i
    i := i + 1
    exit when i = 10
    if i = 11 then
	break %break works to
    end if
end loop
