using System;
using FirstLab.Algorithms.Implementations;

namespace FirstLab
{
    public static class Program
    {
        public static void Main()
        {
            var application =
                new Application(new GoldenSearch(x => Math.Round(Math.Log(x * x, Math.E) + 1 - Math.Sin(x), 10),
                    5));
            application.Execute(6, 10);
        }
    }
}