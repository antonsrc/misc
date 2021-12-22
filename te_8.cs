// te_8

using System;
using System.Threading;

namespace Timer501
{
    class te_8
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Press ENTER for start/pause");
            if (Console.ReadKey().Key == ConsoleKey.Enter)
                time_loop(TimeSpan.Zero);
        }

        static void time_loop(TimeSpan last_total_sec)
        {
            TimeSpan ts = TimeSpan.Zero;
            DateTime dt1 = DateTime.Now;
            DateTime dt2;

            while (!Console.KeyAvailable || Console.ReadKey().Key != ConsoleKey.Enter)
            {
                dt2 = DateTime.Now;
                ts = dt2.Subtract(dt1).Add(last_total_sec);
                Console.Write("\r" + ts.ToString(@"hh\:mm\:ss"));
                Thread.Sleep(1000);
            }

            Console.WriteLine("\nPress ENTER for continue or ESC for stop");
            if (Console.ReadKey(true).Key != ConsoleKey.Escape)
                time_loop(ts);
        }
    }
}