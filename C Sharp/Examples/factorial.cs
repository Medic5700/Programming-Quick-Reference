class program
{
    public static void Main()
    {
        for (int i = 0; i<=10; i++)
        {
            System.Console.WriteLine(i + "!\t= " + factorial(i));
        }
    }
    public static int factorial(int x)
    {
        if (x > 1)
        {
            return (x * factorial(x - 1));
        }
        else
        {
            return 1;
        }
    }
}