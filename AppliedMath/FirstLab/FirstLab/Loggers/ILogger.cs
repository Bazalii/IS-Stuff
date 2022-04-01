namespace FirstLab.Loggers
{
    public interface ILogger
    {
        void Write(int iteration, int functionEvaluations, double intervalLength, double currentResult);
    }
}