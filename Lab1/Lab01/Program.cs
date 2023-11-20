using System;

namespace ConsoleApp1
{
    public class BiquadraticEquation
    {
        private double _coefA, _coefB, _coefC;

        public BiquadraticEquation()
        {
            _coefA = 0.0;
            _coefB = 0.0;
            _coefC = 0.0;
        }

        public void SetCoefA(double coefA)
        {
            _coefA = coefA;
        }

        public void SetCoefB(double coefB)
        {
            _coefB = coefB;
        }
        public void SetCoefC(double coefC)
        {
            _coefC = coefC;
        }

        public static double GetCoef()
        {
            Console.Write("\nВведите число: ");
            string? inputStr = Console.ReadLine(); /* if null -> не будет вызываться*/
            while (!double.TryParse(inputStr, out _))
            {
                Console.Write("Некорректный ввод!\nВведите число: ");
                inputStr = Console.ReadLine();
            }
            return Convert.ToDouble(inputStr);
        }
        public void CalculateRoots()
        {
            double discriminant = this._coefB * this._coefB - 4 * this._coefA * this._coefC;
            if (discriminant == 0)
            {
                Console.Write("Два корня: +/-{0}\n", Math.Sqrt(-this._coefB / (2.0 * this._coefA)));
            }
            else if (discriminant > 0)
            {
                Console.Write("Четыре корня: +/-{0}, ", Math.Sqrt((-this._coefB + Math.Sqrt(discriminant)) / (2.0 * this._coefA)));
                Console.Write("+/-{0}\n", Math.Sqrt((-this._coefB - Math.Sqrt(discriminant)) / (2.0 * this._coefA)));
            }
            else
                Console.Write("Нет корней\n");
        }
    }

    public class Program
    {
        public static void Main(string[] args)
        {
            // Создаем объект типа BiquadraticEquation
            BiquadraticEquation biquad = new BiquadraticEquation();
            if (args.Length == 0)
            {
                Console.Write("Коэффициент А:");
                biquad.SetCoefA(BiquadraticEquation.GetCoef());
                Console.Write("Коэффициент B:");
                biquad.SetCoefB(BiquadraticEquation.GetCoef());
                Console.Write("Коэффициент C:");
                biquad.SetCoefC(BiquadraticEquation.GetCoef());
            }
            else
            {
                try
                {
                    biquad.SetCoefA(Convert.ToDouble(args[0]));
                }
                catch (FormatException)
                {
                    Console.WriteLine("Некорректные аргументы командной строки.");
                    return;
                }

                try
                {
                    biquad.SetCoefB(Convert.ToDouble(args[1]));
                }
                catch (FormatException)
                {
                    Console.WriteLine("Некорректные аргументы командной строки.");
                    return;
                }

                try
                {
                    biquad.SetCoefC(Convert.ToDouble(args[2]));
                }
                catch (FormatException)
                {
                    Console.WriteLine("Некорректные аргументы командной строки.");
                    return;
                }
            }
            biquad.CalculateRoots();
        }
    }
}