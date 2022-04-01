using System;
using System.Collections.Generic;
using FirstLab.Loggers;

namespace FirstLab.Algorithms.Implementations
{
    public class BrentMethod : Algorithm
    {
        public BrentMethod(ILogger logger, FunctionDelegate function, int accuracy)
            : base(logger, function, accuracy)
        {
        }
 
        public override void Execute(double left, double right)
        {
            var intervalLengths = new List<double>();
            var goldenPoint = (3 - Math.Sqrt(5)) / 2;
            var x = (left + right) / 2;
            var w = (left + right) / 2;
            var v = (left + right) / 2;
            var fx = Function(x);
            var fw = Function(w);
            var fv = Function(v);
            var d = right - left;
            var e = right - left;
            var currentLength = right - left;
            while (Math.Round(currentLength, Accuracy + 1) > 4 * Epsilon)
            {
                intervalLengths.Add(currentLength);
                var g = e;
                e = d;
                var u = w - (Math.Pow(w - x, 2) * (fw - fv) - Math.Pow(w - v, 2) * (fw - fx))
                    / (2 * ((w - x) * (fw - fv) - (w - v) * (fw - fx) + Math.Pow(10, -Accuracy - 4)));
                if (left + Epsilon <= u && u <= right - Epsilon && Math.Abs(u - x) < g / 2)
                {
                    d = Math.Abs(u - x);
                }
                else
                {
                    if (x < (right - left) / 2)
                    {
                        u = x + goldenPoint * (right - x);
                        d = right - x;
                    }
                    else
                    {
                        u = x - goldenPoint * (x - left);
                        d = x - left;
                    }
                }
    
                if (Math.Abs(u - x) < Epsilon)
                {
                    if (u - x < 0)
                    {
                        u = x - Epsilon;
                    }
                    else if (Math.Abs(u - x) > Epsilon)
                    {
                        u = x + Epsilon;
                    }
                    else
                    {
                        u = x;
                    }
                }
 
                var fu = Function(u);
                if (fu <= fx)
                {
                    if (u >= x)
                    {
                        left = x;
                    }
                    else
                    {
                        right = x;
                    }
 
                    v = w;
                    w = x;
                    x = u;
                    fv = fw;
                    fw = fx;
                    fx = fu;
                }
                else
                {
                    if (u >= x)
                    {
                        right = u;
                    }
                    else
                    {
                        left = u;
                    }
 
                    if (fu <= fw || Math.Abs(w - x) < Math.Pow(10, -4) * Epsilon)
                    {
                        v = w;
                        w = u;
                        fv = fw;
                        fw = fu;
                    }
                    else if (fu <= fv || Math.Abs(v - x) < Math.Pow(10, -4) * Epsilon ||
                             Math.Abs(v - w) < Math.Pow(10, -4) * Epsilon)
                    {
                        v = u;
                        fv = fu;
                    }
                }
 
 
                currentLength = Math.Abs(right - left);
                Logger.Write(intervalLengths.Count, intervalLengths.Count * 2, currentLength, (left + right) / 2);
            }
 
            intervalLengths.Add(currentLength);
            Logger.Write(intervalLengths.Count, intervalLengths.Count * 2, currentLength, (left + right) / 2);
            DrawGraph(intervalLengths);
        }
    }
}