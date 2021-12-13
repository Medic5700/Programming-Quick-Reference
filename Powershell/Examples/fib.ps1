<#
Author: Medic5700

This is an example of generating the fibonacci sequence using recursion.
#>

Function fib($t1){
    <# Takes in a number $t1, returns the ($t1)th number of the fionacci sequence using recursion #>
    if ($t1 -eq 0){ return 0 }
    elseif ($t1 -eq 1){ return 1 }
    else { return (fib($t1-1)) + (fib($t1-2)) }
}

for ($i=0;$i -le 10;$i++){
    echo ("fib($i)`t= " + (fib($i)))
}