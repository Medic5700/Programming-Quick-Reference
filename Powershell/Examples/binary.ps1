<#
Author: Medic5700

An example of converting a number to a binary string and back
#>

Function binary ($t1){
    <# Takes in a number, returns a string representation of the number in binary (32-bit) #>
    $t2 = ""
	for ($i=0; $i -le 32; $i++){
		if ($t1%2 -eq 0){
            $t2 = "0" + $t2
        }
        else{
            $t2 = "1" + $t2
        }
        $t1 = [Math]::floor($t1/2)
	}
    return $t2
}

Function number ($t1){
    <# Takes in a number, returns a string representation of the number in binary (32-bit) #>
    $t2 = 0
    for ($i=0; $i -le 32; $i++){
        $t2 = $t2 * 2
        if ($t1[$i] -eq "1"){
            $t2 = $t2 + 1
        }
    }
    return $t2
}

for ($i=0; $i -le 255; $i++){
	echo ("$i`t= " + (binary($i)) + "`t=`t" + (number(binary($i))))
}
