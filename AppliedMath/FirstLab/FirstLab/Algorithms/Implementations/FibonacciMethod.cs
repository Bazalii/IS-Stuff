using System;
using System.Collections.Generic;
using FirstLab.Loggers;

namespace FirstLab.Algorithms.Implementations
{
    public class FibonacciMethod : Algorithm
    {
        public FibonacciMethod(ILogger logger, FunctionDelegate function, int accuracy)
            : base(logger, function, accuracy)
        {
        }

        public override void Execute(double left, double right)
        {
            var intervalLengths = new List<double>();
            var fibonacciNumbers = CalculateFibonacciNumbers((right - left) / Epsilon);
            var currentLeft = left + (double) fibonacciNumbers[^3] / fibonacciNumbers[^1] * (right - left);
            var currentRight = left + (double) fibonacciNumbers[^2] / fibonacciNumbers[^1] * (right - left);
            var currentLength = right - left;
            for (int i = 0; i < fibonacciNumbers.Count - 3; i++)
            {
                intervalLengths.Add(currentLength);
                if (Function(currentLeft) <= Function(currentRight))
                {
                    right = currentRight;
                    currentRight = currentLeft;
                    currentLeft = left + (double) fibonacciNumbers[^(i + 4)] / fibonacciNumbers[^(i + 2)] *
                        (right - left);
                }
                else
                {
                    left = currentLeft;
                    currentLeft = currentRight;
                    currentRight = left + (double) fibonacciNumbers[^(i + 3)] / fibonacciNumbers[^(i + 2)] *
                        (right - left);
                }

                currentLength = right - left;
                Logger.Write(intervalLengths.Count, intervalLengths.Count * 2, currentLength, (left + right) / 2);
            }

            currentRight = currentLeft + Epsilon;
            if (Function(currentLeft) > Function(currentRight))
            {
                right = currentRight;
            }
            else
            {
                left = currentLeft;
            }

            Logger.Write(intervalLengths.Count, intervalLengths.Count * 2, currentLength, (left + right) / 2);
            DrawGraph(intervalLengths);
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