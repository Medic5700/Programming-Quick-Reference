
public class FunctionsClasses {

	private static int temp1 = 0;
	private static int temp2 = 0;
	public static double temp3;
	
	/**
	 * @param args
	 */
	public static void main(String[] args) { //The class name must be the same name as the file
		//{access privilege | optional} {static | optional} {return type} {name | if main, will run} {parameters | in brackets} {exception handling | optional}
		/**
		 * The 'public' means any other class can use this class, other access (words?) are:
		 * "Protected"
		 * "Private" 
		 */
		
		powers();
		System.out.println("Now for a function " + aFunction(2,'a'));
		temp3 = temp1 + temp2;
		System.out.println(temp3);
	}
	
	private static void powers ()
	{
		//"private" means only available to this class
		//"void" means it doesn't return anything
		for(int i=0;i<=10;i++)
			System.out.println("2 to the power of   " + i + " = " + (int)Math.pow(2,i));
	}
	
	private static int aFunction (int t1, char c1){
		if (c1 == 'a'){
			temp1++;
			return t1 * 2;
		}
		else{
			temp2++;
			return t1;
		}
	}

}
