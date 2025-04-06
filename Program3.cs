using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace harmadik
{
    class Program
    {
        static void Main(string[] args)
        {
            /*
             * 1. feladat: Kérd be egy téglalap oldalainak hosszát.
             * Írd ki a területét és a kerületét
             * */
            //int a;
            //int b;
            //Console.Write("Kérem az 'a' oldal hosszát egész számként ");
            //a = Convert.ToInt32(Console.ReadLine());
            //Console.Write("Kérem a 'b' oldal hosszát egész számként ");
            //b = Convert.ToInt32(Console.ReadLine());

            //Console.WriteLine("Kerület=" + (2 * a + 2 * b) + "cm");
            //Console.WriteLine("Terület=" + (a * b) + "cm2");

            //Console.ReadKey();

            /* 2. feladat: Írj be két egész számot és írd ki az
             * -összegüket
             * -különbségüket(elsőből a második)
             * -hányadosukat(elsőben a második)
             * -a maradékot(elsőben a második)
             * -a szorzatot
             * */

            //int c;
            //int d;
            //Console.Write("Kérem az 'c' értékét egész számként ");
            //c = Convert.ToInt32(Console.ReadLine());
            //Console.Write("Kérem a 'd' értékét egész számként ");
            //d = Convert.ToInt32(Console.ReadLine());

            //Console.WriteLine("Kérem a két szám összegét");
            //Console.WriteLine("összeg=" + (c + d));

            //Console.WriteLine("Kérem a két szám különbségét");
            //Console.WriteLine("különbség=" + (c-d));

            //Console.WriteLine("Kérem a két szám hányadosát");
            //Console.WriteLine("hányados=" + (c/d));

            //Console.WriteLine("Kérem a két szám maradékát");
            //Console.WriteLine("maradék=" + (c%d));

            //Console.WriteLine("Kérem a két szám szorzatát");
            //Console.WriteLine("szorzat=" + (c*d));

            //Console.ReadKey();

            /* 3. feladat: Kérd be a felhasználó vezetéknevét és keresztnevét!
             * -írd ki a teljes nevét egy sorba
             * -köszönj neki angolul és magyarul is két külön utasításban */

            //string keresztnev;
            //string vezeteknev;
            //Console.Write("Mi a keresztneved?" );
            //keresztnev = Console.ReadLine();

            //Console.Write("Mi a vezetékneved?" );
            //vezeteknev = Console.ReadLine();
            //Console.WriteLine("teljes név:" + (keresztnev +  vezeteknev));

            //Console.WriteLine("Üdv" +  (keresztnev +  vezeteknev));
            //Console.WriteLine("Welcome" +  (vezeteknev +  keresztnev));
            //Console.ReadKey();

            //Házi feladat: Készítsd el a gondoltam egy számra játékot!

            double a;
            double b;
           
            
            Console.WriteLine("Gondolj egy számra");

            Console.WriteLine("Adj hozzzá 4-et");

            Console.WriteLine("Vonj ki belőle 6-ot");
           
            

            Console.WriteLine("Mennyi lett a kapott érték?");
            
            Console.Write("A kapott szám:" + (b));
           
            Console.WriteLine("A gondolt szám:" + (a=b+6-4));
           

            Console.ReadKey();





        }
    }
}
