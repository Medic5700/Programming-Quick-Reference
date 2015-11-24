<?php

	/* basic math operators
	 * "+"	- Addition 
	 * "-"	- Subtraction 
	 * "*"	- Multiplication 
	 * "/"	- Division
	 * "%"	- Modulus
	 */

	/* bitwise operators
	 * "&" 	- And
	 * "|"	- Or
	 * "^"	- Xor
	 * "~"	- Not
	 * "<<"	- Shift left 
	 * ">>"	- Shift right
	 */
?> 

<?php
	$output = `dir`; //stuff in "``" will be exicuted as shell commands (since this is running on a windows machine, thats the list files command for CMD
	echo "<pre>$output</pre>";
?> 
