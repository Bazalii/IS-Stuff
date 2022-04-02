using System;

namespace FirstLab.Loggers.Implementations
{
    public class ConsoleLogger : ILogger
    {
        public void Write(int iteration, int functionEvaluations, double intervalLength, double currentResult)
        {
            Console.Write(
                $"Iteration: {iteration}.\n" +
                $"Number of function evaluations: {functionEvaluations}.\n" +
                $"Interval length: {intervalLength}\n" +
                $"Current result: {currentResult}\n\n");
        }
    }
}