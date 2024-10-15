using System;

namespace BLocoTryCatch
    class Program
    {
        static void Main(string[] args)
        {
            var nomes = new[] { "joel", "fagner", "tom" };
            for (var indice = 0; indice < nomes.Length; indice++)
            {
                Console.WriteLine(nomes[indice]);
            }
      
        }
    }
}