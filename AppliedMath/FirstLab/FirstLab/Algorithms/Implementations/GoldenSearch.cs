using System;
using System.Collections.Generic;
using FirstLab.Loggers;

namespace FirstLab.Algorithms.Implementations
{
    public class GoldenSearch : Algorithm
    {
        public GoldenSearch(ILogger logger, FunctionDelegate function, int accuracy)
            : base(logger, function, accuracy)
        {
        }

        public override void Execute(double left, double right)
        {
            var intervalLengths = new List<double>();
            var goldenPoint = (Math.Sqrt(5) + 1) / 2;
            var currentLeft = left + (right - left) / Math.Pow(goldenPoint, 2);
            var currentRight = left + (right - left) / goldenPoint;
            var currentLength = right - left;
            while (Math.Round(right - left, Accuracy + 1)  > Epsilon)
            {
                intervalLengths.Add(currentLength);
                if (Function(currentLeft) <= Function(currentRight))
                {
                    right = currentRight;
                    currentRight = currentLeft;
                    currentLeft = left + (right - left) / Math.Pow(goldenPoint, 2);
                }
                else
                {
                    left = currentLeft;
                    currentLeft = currentRight;
                    currentRight = left + (right - left) / goldenPoint;
                }
                
                currentLength = right - left;
                Logger.Write(intervalLengths.Count, intervalLengths.Count * 2, currentLength, (left + right) / 2);
            }
            
            intervalLengths.Add(currentLength);
            Logger.Write(intervalLengths.Count, intervalLengths.Count * 2, currentLength, (left + right) / 2);
        }
    }
}