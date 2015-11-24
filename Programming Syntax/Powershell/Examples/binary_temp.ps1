Function binary ($t1){
    $t2 = ""
	for ($i=0;$i -le 32;$i++){
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
    $t2 = 0
    for ($i=0;$i -le 32; $i++){

    }
}

for ($i=0;$i -le 255;$i++){
	echo ("$i`t= " + (binary($i)) + "`t=`t")
}
