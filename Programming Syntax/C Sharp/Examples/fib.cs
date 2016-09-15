class fibProgram
{
    static void Main()
    {
        for (int i = 0; i <= 10; i++) //note: since these are single line statments, I can exclude the brackets in this case
            System.Console.WriteLine("fib("+i+")\t= " + fib(i));
    }
    public static int fib(int x)
    {
        if (x == 0)
        {
            return 0;
        }
        else if (x == 1)
        {
            return 1;
        }
        else
        {
            return fib(x - 1) + fib(x - 2);
        }
    }
}