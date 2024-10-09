// See https://aka.ms/new-console-template for more information

Console.WriteLine("Digite a sua idade");
var idadeInput = Console.ReadLine();
var idade = Convert.ToInt32(idadeInput);

var teste = idade >= 18 ? "true" :  "false";

Console.WriteLine(teste);