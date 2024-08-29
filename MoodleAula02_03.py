forma = str(input("Você deseja calcular o volume do dodecaedro ou icosaedro: "))

if forma == "dodecaedro":
    a = int(input("Digite o valor da aresta A em metros: "))
    calculo = (a + (7 * 2.23607))
    print("O volume é %f" %calculo)


if forma == "Icosaedro":
    a = int(input("Digite o valor da aresta A em metros: "))
    calculo = 5 / 12 * (3+(5 ** (1/2))) * (a ** 3)
    print("O volume de um %s regular com %.2d metro de aresta é: %f" %forma,a,calculo)