/**
 * Function Class
 **/

var t3 : int := 5 %since this variable is declared before procedures/functions, they can use/modify this variable

procedure a1 (t1, t2 : int)
    %runs a bunch of instruction with some input (if required)
    put t1
    put t2
    put t3 %note, varuables decleared outside procedure/function are accesible iff said variable is declared before procedure
end a1

function a2 (t1, t2 : int) : int
    %just like 'procedure', only it returns a value (that must be specified)
    result t1 * t2 * t3
end a2

module a3
    %when included (or in this case, declared), will run any code in 'main'
    %modules are mainly used when only one instance is needed at most
    import Input
    export unqualified pervasive b3
    %the 'pervasive' allows it to be auto imported into any moduals (in case of advanced students)
    module b1
	export c1
	procedure c1
	    put "hello"
	end c1
    end b1
    procedure b2
	put "procedure 'b2' of module 'a3' active"
    end b2
    procedure b3
	b1.c1
	b2
    end b3
    b3 %will run this code upon initialization
end a3

a1 (1, 2)
put a2 (3, 4)
b3
put ""

%some stuff on classes
class x1
    %alot like a modual, but more then one can be constructed
    export initialize, print

    var y1 : string := ""
    var y2 : int := 0
    procedure initialize (t1 : string, t2 : int)
	y1 := t1
	y2 := t2
    end initialize
    procedure print
	put "name: ", y1, "\tvalue: ", y2
    end print
end x1

var classTest1 : ^x1 %declearing a variable  of type 'class x1'
new x1, classTest1 %actualy cronstructing the class (I Think?)
classTest1 -> initialize ("classTest1", 1) %using a command/procedure from the class
var classTest2 : ^x1 %creating a another instance of x1
new x1, classTest2
classTest2 -> initialize ("classTest2", 256)

%printing the variables of each instance side by side, to show the difference
classTest1 -> print
classTest2 -> print
