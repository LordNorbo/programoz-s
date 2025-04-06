using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace masodik
{
    class Program
    {
        static void Main(string[] args)
        {
         
            
            

            string nev; //egy szöveg típusú változó deklarációja
            Console.Write("Hogy hívnak? ");
            nev = Console.ReadLine(); //név változónak értékül adjuk azt, amit a felhasználó begépel

            Console.WriteLine("Jó napot kívánok kedves" + nev + "!");

            Console.ReadKey();

            int kor; // ez egy egész típusú változó
            Console.Write("Hány éves vagy? ");
            kor = Convert.ToInt32(Console.ReadLine()); // a beolvasott sort egész számmá konvertáljuk

            Console.WriteLine(nev + " " + kor + "éves");

            Console.ReadKey();
        }
    }
}
