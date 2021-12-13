<#
Author: Medic5700

This is an example of generating a factorial using recursion.
#>

Function factorial ($t1){
    <# Takes in a number $t1, returns the factorial of $t1 using recursion #>
    if ($t1 -gt 1){
        return $t1*(factorial($t1-1))
    }
    else{
        return 1
    }
}

for ($i=0;$i -le 10;$i++){
    echo ("$i!`t= " + (factorial($i)))
}