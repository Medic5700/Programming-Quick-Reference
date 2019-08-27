var input : string

%input output to consol
put "output"
get input

var filename : string := "bin\\test.txt"
var f : int

%file write
open : f, filename, put % (get, put, read, write, seek, mod)
put : f, "test\ntest"
close : f

%file read
var line : string
open : f, filename, read
read : f, line % note: read takes the ENTIRE input file
put line
close : f
