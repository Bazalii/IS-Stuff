using System;
using System.Collections.Generic;

namespace FirstLab.Algorithms
{
    public abstract class Algorithm
    {
        protected FunctionDelegate Function;

        protected int Accuracy;

        protected double Epsilon;

        protected Algorithm(FunctionDelegate function, int accuracy)
        {
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