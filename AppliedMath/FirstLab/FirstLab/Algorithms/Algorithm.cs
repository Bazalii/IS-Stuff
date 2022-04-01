using System;
using System.Collections.Generic;
using FirstLab.Loggers;

namespace FirstLab.Algorithms
{
    public abstract class Algorithm
    {
        protected ILogger Logger;
        
        protected FunctionDelegate Function;

        protected int Accuracy;

        protected double Epsilon;

        protected Algorithm(ILogger logger, FunctionDelegate function, int accuracy)
        {
            Logger = logger;
            Function = function;
            Accuracy = accuracy;
            Epsilon = Math.Pow(10, -Accuracy);
        }

        public abstract void Execute(double left, double right);

        protected void DrawGraph(List<double> points)
        {
            
        }
    }
}