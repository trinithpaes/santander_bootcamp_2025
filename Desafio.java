import java.util.Scanner;

public class Desafio {

    public static void main(String[] args) {
        //Lê os valores de Entrada:
        Scanner leitorDeEntradas = new Scanner(System.in);
        float valorSalario = leitorDeEntradas.nextFloat();
        float valorBeneficios = leitorDeEntradas.nextFloat();

        float valorImposto = 0;
        if (valorSalario >= 0 && valorSalario <=1100) {
            //Atribuiu a aliquota de 5% mediante o salário:
            valorImposto = 0.05F * valorSalario;
        }else if (valorSalario >= 1100.01 && valorSalario <=2500) {
            //Atribuiu a aliquota de 10% mediante o salário:
            valorImposto = 0.10F * valorSalario;
        }else {
            //Atribuiu a aliquota de 15% mediante o salário:
            valorImposto = 0.15F * valorSalario;
        }

        //Calcula e imprime a Saída (com 2 casas decimaís):
        float saida = valorSalario - valorImposto + valorBeneficios;
        System.out.println(String.format("%.2f", saida));
    }
}