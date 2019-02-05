% puts the current directory you are in
put "The current directory this file is in is:"
put Dir.Current

var fileName : string := "Random.t"
var temp1 : string
%from turing help
% Create a file in the new directory
put "We now create a file in the current directory called \"", fileName, "\""
var f : int
/* I/O commands
 put     -writes one line of code to a file
 write   -
 mod     -

 get     -gets one line of code from file and stores to a variable
 read    -gets entire file and stores to a variable
 seek    -

 */


%open "connects the program to a file so the program can perform operations"
open : f, fileName, put % (get, put, read, write, seek, mod) are i/o comands
put : f, "const test : int := 5" %writes to the file whatever is in quoits
put : f, "const test2 : int := 7"
close : f %close "disconnects from the file"
put "File created"
delay (2000)


put "Desplaying file contents:"
open : f, fileName, read %opens file
read : f, temp1 %gets contents and stores to variable "temp1"
close : f %closes file
put temp1

put "RE-WRIGHTING to file"
open : f, fileName, put
put : f, "const test : int := 10" %OVER-writes to the file whatever is in quoits
close : f

put "Desplaying altered file:"
open : f, fileName, get
get : f, temp1 : * %gets contets and stores to variable "temp1"
close : f
put temp1


delay (2000)
% Delete the file in the current directory
put "We try to delete the file \"", fileName, "\" " ..
File.Delete (fileName)
if Error.Last = 0 then
    put "and succeed"
else
    put "but we get the following error: ", Error.LastMsg
end if

