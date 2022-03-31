using System;
using System.Collections.Generic;

namespace FirstLab.Algorithms.Implementations
{
    public class Dichotomy : Algorithm
    {
        public Dichotomy(FunctionDelegate function, int accuracy)
            : base(function, accuracy)
        {
        }

        public override void Execute(double left, double right)
        {
            var intervalLengths = new List<double>();
            var currentLength = right - left;
            while (Math.Round(currentLength, Accuracy + 1) > Epsilon)
            {
                intervalLengths.Add(currentLength);
                var currentLeft = (left + right - Epsilon) / 2;
                var currentRight = (left + right + Epsilon) / 2;
                var leftValue = Function(currentLeft);
                var rightValue = Function(currentRight);
                if (leftValue <= rightValue)
                {
                    right = currentRight;
                }
                else
                {
                    left = currentLeft;
                }

                currentLength = right - left;
            }
            
            intervalLengths.Add(currentLength);
            Console.WriteLine($"{(left + right) / 2}");
            DrawGraph(intervalLengths);
        }
    }
}