
public class test {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		/**
		 * "|" the OR operator 		 	* "&" the AND operator
		 * "^" the XOR operator		 	* "!" the NOT operator
		 * "==" the EQUAL TO operator	* "?:" the IF-THEN-ELSE operator
		 * "<", ">", "<=", ">=", "!=" the usual math comparisons
		 **/
		int t1 = 5;
		Integer t2 = 5;
		double f1 = 5.0;
		Double f2 = 5.0;
				
		if (t1 == 1){
			int[][] intArray = new int[5][6];
			for (int i = 0;i<intArray.length;i++){
				for (int j = 0;j<intArray[i].length;j++)
					intArray[i][j] = i*j;
			}
		}
		else if (t1 == 2)
			t2 = 0;
		else
			t1 = 0;
	}

}
