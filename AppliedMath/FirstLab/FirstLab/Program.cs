using System;
using FirstLab.Algorithms.Implementations;
using FirstLab.Loggers.Implementations;

namespace FirstLab
{
    public static class Program
    {
        public static void Main()
        {
            var application =
                new Application(new BrentMethod(new ConsoleLogger(),
                    x => Math.Round(Math.Log(x * x, Math.E) + 1 - Math.Sin(x), 10),
                    5));
            application.Execute(-7, -2);
        }
    }
}