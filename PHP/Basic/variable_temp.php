<?php
	//primitives
	$var_bool = TRUE;
	$var_str  = "foo";
		// http://www.php.net/manual/en/language.types.string.php
	$var_int = 12;
		$var_int = 0777; //a '0' infront of the number represents a octle number
		$var_int = 0xff; //a '0x' infront of the number represents a hex number
		$var_int = 0b11; //a '0b' infront of the number represents a binary number
		$var_int = 12; //a decimal number
	$var_float = 3.14159;
		$var_float = 1.234; 
		$var_float = 1.2e3; 
		$var_float = 7E-10;

	
	echo gettype($var_bool); // prints out:  boolean
	
	echo is_int($var_int); //returns true if it's an int
	echo is_string($var_bool);
	
	echo "<br><br><br>"; //just a line spacer for the output

	//casting
	echo ((bool) $var_str);

	echo "<br><br><br>";

	//arrays
	// http://www.php.net/manual/en/language.types.array.php
	/* the array associates a key value pair (like a dictionary/hashmap) */
	$var_array = [ //key "random" with value "b"
		0 => "a",
		"random" => "b"
		];
	$var_array = ["a","b","c","d","e"]; //or you can leave out the keys (and they will automaticaly get numbers instead
	//multi-dimentional arrays work too
	var_dump($var_array); //outputs the entire array
	
	echo "<br><br><br>";

	echo ($var_array[0]);
	sort($var_array);
	unset($var_array[2]); // This removes the element from the array
	unset($var_array); // This deletes the whole array
	




	/* to integrate! */
	//variable variables -> http://www.php.net/manual/en/language.variables.variable.php
	// Valid constant names
	define("FOO",     "something");
	define("FOO2",    "something else");
	define("FOO_BAR", "something more");
	const CONSTANT = 'Hello World';
	//http://www.php.net/manual/en/language.constants.predefined.php
	//references -> http://www.php.net/manual/en/language.operators.assignment.php


?>
