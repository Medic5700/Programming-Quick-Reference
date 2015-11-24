Param([switch]$help, $test="test", [String]$test2) #handeling inputs in a more controlled way, or you can directly access the arguments using the '$args' variable(you can use one XOR the other!)

#a comment
<# a block comment #>
echo "Hello World`n`nHello World" #the "`" is an escape character
#note: the `b doesn't work as expected in the ISE vs the shell

if($help -eq $true){
    echo "help switch activated"
    echo "$test"
}

$true
$false
$NULL

#The usual piping and command line stuff work, except redirecting a file into a command, redirecting out to a file works fine
