using System;
using System.Collections.Generic;
using FirstLab.Loggers;

namespace FirstLab.Algorithms.Implementations
{
    public class ParabolicMethod : Algorithm
    {
        public ParabolicMethod(ILogger logger, FunctionDelegate function, int accuracy)
            : base(logger, function, accuracy)
        {
        }

        public override void Execute(double left, double right)
        {
            var intervalLengths = new List<double>();
            var mid = (left + right) / 2;
            var f1 = Function(left);
            var f2 = Function(mid);
            var f3 = Function(right);
            var currentLength = right - left;
            while (Math.Round(currentLength, Accuracy + 1) > 2 * Epsilon)
            {
                intervalLengths.Add(currentLength);
                var u = mid - (Math.Pow(mid - left, 2) * (f2 - f3) - Math.Pow(mid - right, 2) * (f2 - f1)) /
                    (2 * ((mid - left) * (f2 - f3) - (mid - right) * (f2 - f1)));
                var fu = Function(u);

                if (mid <= u)
                {
                    if (f2 <= fu)
                    {
                        right = u;
                        f3 = fu;
                    }
                    else
                    {
                        left = mid;
                        mid = u;
                        f1 = f2;
                        f2 = fu;
                    }
                }
                else
                {
                    if (fu <= f2)
                    {
                        right = mid;
                        mid = u;
                        f2 = fu;
                        f3 = f2;
                    }
                    else
                    {
                        left = u;
                        f1 = fu;
                    }
                }


                currentLength = right - left;
                Logger.Write(intervalLengths.Count, intervalLengths.Count * 2, currentLength, (left + right) / 2);
            }

            intervalLengths.Add(currentLength);
            Logger.Write(intervalLengths.Count, intervalLengths.Count * 2, currentLength, (left + right) / 2);
            DrawGraph(intervalLengths);
        }
    }
}