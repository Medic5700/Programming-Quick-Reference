<?php
	function factorial ($t1){
		if ($t1 > 0){
			return $t1*factorial($t1-1);
		}
		else {
			return 1;
		}
	}
	
	function fib ($t1){
		if ($t1 == 0){
			return 0;
		}
		elseif ($t1 == 1){
			return 1;
		}
		else {
			return fib($t1 - 1) + fib($t1 - 2);
		}
	}

	for ($i=0;$i<=10;$i++){
		echo "$i!\t= ", factorial($i), "\t\tfib($i)\t= ", fib($i), "<br>\n";
	}
?>