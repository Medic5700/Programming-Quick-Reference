<?php

	//class stuff -> http://www.php.net/manual/en/language.oop5.decon.php
	class SimpleClass {
		public $var_int = 42;
		protected $var_int2 = 52; //this can be changed when extending the class
		private $var_int2 = 50; //this can't be accessed when extending the class
		
		function simplefunction ($t1,$t2){
			echo "$t1 $t2<br>";
		}
	}
	$var_class = new simpleClass();
	$var_class->var_int = 25;
	$var_class->simplefunction($var_class->var_int,"testing"); //TODO: TEST

	class simpleClass2 {
		public static $var_string = "stuff";
	}
	echo simeplClass2::$var_string; //useing 'static', you can use functions/variablesbefore constructing the object
	//may result in confusion if using both classes you have to construct and static stuff in classes
	
	//function stuff
	$random = "outside variable";

	function test($t1, $t2) {
		global $random; //this allows you to use variables outside the function
		static $random2; //static variable will hold it's value after the function finishes
		echo "function test $t1 $t2";
		echo $random;
	}
	test ("testing", "test");

	function test2($type = "test") { //can give a variable a default value if it isn't passed in
		echo "$type<br>";
	}

?>
