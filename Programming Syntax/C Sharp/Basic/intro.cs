//A comment
/* A block comment */
using System; //allows you to use System methods without fully qualifying them (IE: Console.WriteLine() instead of System.Console.WriteLine())
namespace intro //defineing a namespace not neccissary on smaller stuff
{
    /* A namespace helps organize larger projects and help control the scope of various classes/methods
     * can be nested
     */
    class intro
    {
        /* abstract - this means the thing being defined has an incomplete definition
         */
        public static void Main(string[] args) //This is the main method for your class
        {
            /* static - 
             * void - 
             * public -
             * private - 
             * override - Overrides method from class inheritance
             */
            //Program args can be passed to your program via and array of strings, does not include the name of the executable
            System.Console.WriteLine("Hello World"); //lines end with ';'
        }
    }

    /*should the following stuff be in a different file?
     */
    struct temp1
    {

    }
    interface temp2
    {

    }
    enum temp3
    {

    }
}