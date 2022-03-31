using System;
using System.Collections.Generic;

namespace FirstLab.Algorithms.Implementations
{
    public class FibonacciMethod : Algorithm
    {
        public FibonacciMethod(FunctionDelegate function, int accuracy) : base(function, accuracy)
        {
        }

        public override void Execute(double left, double right)
        {
            var fibonacciNumbers = CalculateFibonacciNumbers((right - left) / Epsilon);
            var currentLeft = left + (double)fibonacciNumbers[^3] / fibonacciNumbers[^1] * (right - left);
            var currentRight = left + (double)fibonacciNumbers[^2] / fibonacciNumbers[^1] * (right - left);
            var leftValue = Function(currentLeft);
            var rightValue = Function(currentRight);
            for (int i = 0; i < fibonacciNumbers.Count - 3; i++)
            {
                leftValue = Function(currentLeft);
                rightValue = Function(currentRight);
                if (leftValue <= rightValue)
                {
                    right = currentRight;
                    currentRight = currentLeft;
                    currentLeft = left + (double)fibonacciNumbers[^(i + 4)] / fibonacciNumbers[^(i + 2)] * (right - left);
                }
                else
                {
                    left = currentLeft;
                    currentLeft = currentRight;
                    currentRight = left + (double)fibonacciNumbers[^(i + 3)] / fibonacciNumbers[^(i + 2)] * (right - left);
                }
            }

            currentRight = currentLeft + Epsilon;
            leftValue = Function(currentLeft);
            rightValue = Function(currentRight);
            if (leftValue > rightValue)
            {
                right = currentRight;
            }
            else
            {
                left = currentLeft;
            }
            
            Console.WriteLine($"{(left + right) / 2}");
        }

        private List<int> CalculateFibonacciNumbers(double number)
        {
            var result = new List<int>();
            result.Add(1);
            result.Add(1);
            var current = result[0] + result[1];
            var iterator = 2;
            while (current <= number)
            {
                current = result[iterator - 1] + result[iterator - 2];
                result.Add(current);
                iterator++;
            }

            return result;
        }
    }
}