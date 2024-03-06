using System;

class Program
{
    static int Calculation(int N) 
    {
        return N + 1;
    }
    
    static void Result(int N)
    {
        Console.WriteLine(N);
    }

    static void Main()
    {
        int N = int.Parse(Console.ReadLine());
        N = Calculation(N);
        Result(N);
    }
}