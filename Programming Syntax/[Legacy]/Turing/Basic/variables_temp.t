%primitives
var var_nat : nat
const var_int : int := 5 %the 'const' is a constant declaration
var var_real : real
var var_bool : boolean
var var_string : string

%some stuff with arrays
var t7 : flexible array 1 .. 0 of string %a flexable array can be resized
var t8 : array 1 .. 2, 1 .. 7 of int := init (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14) %a static array can't be resized
new t7, 7 %resizes the felxible array

for i : 1 .. upper (t7) %'upper(t7)' finds the size of array
    put t7 (i)
end for
for i : 1 .. upper (t8, 1) %with multi-demensional arrays, you must specify which dimension you want from the array with 'upper(array, dimension)'
    for j : 1 .. upper (t8, 2) %finding the size of dimension '2' of array
        put "t8 value at (", i, ",", j, ") = ", t8 (i, j)
    end for
end for