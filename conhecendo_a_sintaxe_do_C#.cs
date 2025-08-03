using System;

public class Desafio
{
    public static void Main()
    {
    //Lê os valores de Entrada:
    float valorSalario = float.Parse(Console.ReadLine());
    float valorBeneficios = float.Parse(Console.readLine());

    float valorImposto = 0;
    if (valorSalario >= 0 && valorSalario <= 1100)
    {
    //Atribiu a aliquota de 5% madiante o salário:
    valorImposto = 0.05F * valorSalario;
    }
    else if (valorSalario >= 1100.01 && valorSalario <= 2500)
    {
        valorImposto = 0.10F * valorSalario;
    }
    else
    {
            valorImposto = 0.15F * valorSalario;
    }

    //Calcula e imprime a Saída (com 2 casas decimais):
    float saida = valorSalario - valorImposto + valorBeneficios;
    console.writeLine(saida.ToString("0.00"));
    }
}