class variable
{
    public static void Main()
    {
        int varInt1 = 5;
        /* int
         * float
         * char
         * string
         * bool
         */
        var varInt2 = 6; //using 'var' lets the compiler infer the type of the variable

        //arrays
        int[] arrayInt1 = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
        int[] arrayInt2 = new int[10];
        int[] arrayInt3 = new int[] { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
        int[,] arrayInt4 = new int[4, 4]; //a multidimensional array
        int[,] arrayInt5 = { { 1, 2 }, { 3, 4 } };
        int[][] arrayInt6 = new int[4][]; //a 'jagged array', IE: an array of arrays
    }
}