// Program to read and write Registry
using Microsoft.Win32;
using System;

class Program
{
    static void Main(string[] args)
    {
        // Specify the registry key and value to read
        string keyPath = @"HKEY_LOCAL_MACHINE\SOFTWARE\Adobe\Registration";
        string valueName = "NAME";

        // Open the registry key and read the value
        object value = Registry.GetValue(keyPath, valueName, null);

        // Output the value to the console
        Console.WriteLine("The value of {0}\\{1} is: {2}", keyPath, valueName, value);
        
        Console.ReadLine(); // wait for user input to exit
    }
}
