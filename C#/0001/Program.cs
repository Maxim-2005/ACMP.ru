using System;

class Program
{
    static void Main()
    {
        string numbers = Console.ReadLine();
        string[] digit = numbers.Split();

        int[] digits = new int[digit.Length];

        for (int i =0; i < digit.Length; i++)
        {
            digits[i] = int.Parse(digit[i]);
        }

        Console.WriteLine(digits[0] + digits[1]);
    }
}