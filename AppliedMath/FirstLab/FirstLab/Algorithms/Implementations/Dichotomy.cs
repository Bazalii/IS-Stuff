using System;
using System.Collections.Generic;
using FirstLab.Loggers;

namespace FirstLab.Algorithms.Implementations
{
    public class Dichotomy : Algorithm
    {
        public Dichotomy(ILogger logger, FunctionDelegate function, int accuracy)
            : base(logger, function, accuracy)
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
                if (Function(currentLeft) <= Function(currentRight))
                {
                    right = currentRight;
                }
                else
                {
                    left = currentLeft;
                }
                
                currentLength = right - left;
                Logger.Write(intervalLengths.Count, intervalLengths.Count * 2, currentLength, (left + right) / 2);
            }
            
            intervalLengths.Add(currentLength);
            Logger.Write(intervalLengths.Count, intervalLengths.Count * 2, currentLength, (left + right) / 2);
        }
    }
}