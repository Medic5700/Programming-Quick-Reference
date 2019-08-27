<?php
	//basicaly work like while, do-while, and for in C
	
	$i = 0;
	while ($i < 10){
		echo "Loop 0 iteration $i<br>";
		$i = $i + 1;
	}
	
	$i = 0;
	do {
		echo "Loop 1 iteration $i<br>";
		$i++;
	} while ($i < 10);
	
	for($j=0;$j<10;$j++){
		echo "Loop 2 iteration $j<br>";
	}
	
	$i = [0,1,2,3,4,5,6,7,8,9]; //declaring an array
	foreach($i as $j){ //notice the syntax here... $i is the array, with $j stepping through the array... not the other way around
		echo "Loop 3 iteration $j<br>";
	}
	
	for($j=0;$j<10;$j++){
		for($k=0;$k<10;$k++){
			echo "Loop 4 iteration $j $k<br>";
			if ($k == 1){
				break 2; //break has an optional argument to specify how many levels to break out of
			}
		}
	}
	
	//continue -> http://www.php.net/manual/en/control-structures.continue.php
?>
