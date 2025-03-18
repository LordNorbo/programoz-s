using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace tombok_feladat
{
    class Program
    {
        static void Main(string[] args)
        {
            //1.
            int[] vasgyurok = new int[100];
            int osszeg = 0;
            Random rnd = new Random();

            for (int i = 0; i < vasgyurok.Length; i++)
            {
                vasgyurok[i] = rnd.Next(25, 65);
                
            }

            //a

            for (int i = 0; i < vasgyurok.Length; i++)
            {
                osszeg = osszeg + vasgyurok[i];
            }

            Console.WriteLine("Átlag:"+osszeg/vasgyurok.Length+"cm");

            Console.ReadKey();

            //b

            int szamlalo = 0;
            for (int i = 0; i < vasgyurok.Length; i++)
            {
                if (vasgyurok[i]>50)
                {
                    szamlalo++;
                }
            }
            Console.WriteLine("50cm-nél nagyobb karú rabok: "+szamlalo+"db");

            Console.ReadKey();

            //c

            int legnagyobb = vasgyurok[0];

            for (int i = 1; i < vasgyurok.Length; i++)
            {
                if (vasgyurok[i]>legnagyobb)
                {
                    legnagyobb = vasgyurok[i];
                }
            }
            Console.WriteLine("A legnagyobb kar: "+legnagyobb+"cm");

            Console.ReadKey();

            //d

            int j = 0;

            while (j<vasgyurok.Length && vasgyurok[j]<=60)
            {
                j++;
            }
            if (j<vasgyurok.Length)
            {
                Console.WriteLine("Van 60cm-nél nagyobb karú rab");
            }
            else
            {
                Console.WriteLine("Nincs 60cm-nél nagyobb karú rab");
            }

            Console.ReadKey();
            //2.

            int[] jegyek = new int[30];
            for (int i = 0; i < jegyek.Length; i++)
            {
                jegyek[i] = rnd.Next(1, 6);
            }

            //a
            j = 0;

            while (j<jegyek.Length && jegyek[j]!=1)
            {
                j++;
            }
            if (j<jegyek.Length)
            {
                Console.WriteLine("Van bukott diák a "+(j+1)+". helyen");
            }
            else
            {
                Console.WriteLine("Nincs bukott diák");
            }
            Console.ReadKey();

            //b
            szamlalo = 0;
            for (int i = 0; i < jegyek.Length; i++)
            {
                if (jegyek[i]==5)
                {
                    szamlalo++;
                }
            }
            Console.WriteLine("Ennyi jeles tanuló van: " + szamlalo);

            Console.ReadKey();

            //c
            osszeg = 0;
            for (int i = 0; i < jegyek.Length; i++)
            {
                osszeg = osszeg + jegyek[i];
            }
            Console.WriteLine("A csoport átlaga:"+ osszeg/jegyek.Length);

            Console.ReadKey();

            //3. a

            string[] nevek = new string[2];
            int[] fizika = new int[2];
            
            for (int i = 0; i < nevek.Length; i++)
            {
                Console.WriteLine("Adja meg a tanuló nevét");
                nevek[i] = Console.ReadLine();
                //fizika[i] = rnd.Next(1, 6);
                Console.WriteLine("Adja meg a tanuló jegyét");
                fizika[i] = Convert.ToInt32(Console.ReadLine());

                Console.WriteLine(nevek[i]+"fizika jegye: " + fizika[i]);
            }

            Console.ReadKey();
            //b
            int legkisebbhelye = 0;

            for (int i = 0; i < fizika.Length; i++)
            {
                if (fizika[i]<fizika[legkisebbhelye])
                {
                    legkisebbhelye = 1;
                }
            }
            Console.WriteLine(nevek[legkisebbhelye]+ "a leggyengébb fizikából");

            Console.ReadKey();

            //c
            j = 0;
            while (j<fizika.Length&&fizika[j]!=3)
            {
                j++;
            }
            if (j<fizika.Length)
            {
                Console.WriteLine("Van 3mas, mégpedig: "+ nevek[j]);
            }

            Console.ReadKey();

            //4.
            string[] osztaly = new string[2];
            int[] proba = new int[2];
            for (int i = 0; i < osztaly.Length; i++)
            {
                Console.WriteLine("Adja meg a tanuló nevét");
                osztaly[i] = Console.ReadLine();
                Console.WriteLine("Adja meg a tanuló probálkozásainak számát");
                proba[i] = Convert.ToInt32(Console.ReadLine());

                Console.WriteLine(osztaly[i] + "tanuló probálkozásainak száma: "+ proba[i]);
            }
            //a
            j= 0;

            while (j<osztaly.Length && proba[j]!=10)
            {
                j++;
            }
            if (j<osztaly.Length)
            {
                Console.WriteLine("Van olyan aki 10nél többször próbálkozott");
            }
            else
            {
                Console.WriteLine("Nincs olyan aki 10nél többször próbálkozott");
            }

            //b
            Console.ReadKey();

            j = 0;

            while (j < osztaly.Length && proba[j] != 0)
            {
                j++;
            }
            if (j < osztaly.Length)
            {
                Console.WriteLine("Van olyan aki 0szor próbálkozott");
            }
            else
            {
                Console.WriteLine("Nincs olyan aki 0szor próbálkozott");
            }

            Console.ReadKey();
            
            //c





        }
    }
}
