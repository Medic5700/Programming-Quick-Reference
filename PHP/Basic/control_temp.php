<?php
	/**
	 * "||" "or" the OR operator 
	 * "&&" "and" the AND operator
	 * "^" "xor" the XOR operator
	 * "!" the NOT operator
	 * "==" the EQUAL TO operator
	 * "===" identical
	 * "!=" NOT EQUAL
	 * "<>" not equal
	 * "!==" not identical
	 * "<", ">", "<=", ">=", "!=" the usual math comparisons
	 **/

	for ($i=0;$i<10;$i++){
		if ($i==0){
			echo "if statment 0 option 0<br>";
		}
		elseif ($i==1){
			echo "if statment 0 option 1<br>";
		}
		else {
			echo "if statment 0 option 2<br>";
		}
	}

	//switch -> http://www.php.net/manual/en/control-structures.switch.php
?>

<!-- http://www.php.net/manual/en/language.basic-syntax.phpmode.php -->
<?php 
	$expression = true;
	if ($expression == true): 
?>
  This will show if the expression is true.
<?php else: ?>
  Otherwise this will show.
<?php endif; ?> 
