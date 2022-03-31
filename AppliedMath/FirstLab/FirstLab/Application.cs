using FirstLab.Algorithms;

namespace FirstLab
{
    public class Application
    {
        private readonly Algorithm _algorithm;

        public Application(Algorithm algorithm)
        {
            _algorithm = algorithm;
        }

        public void Execute(double left, double right)
        {
            _algorithm.Execute(left, right);
        }
    }
    
    public delegate double FunctionDelegate(double x);
}