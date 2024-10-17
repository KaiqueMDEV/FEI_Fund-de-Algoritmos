#Construa um algoritmo que, tendo como dados de entrada o preço de um produto e seu código de origem, mostre o preço junto de sua procedência. Caso o código não seja nenhum dos
# especificados, o produto deve ser encarado como importado.



preco = float(input("Informe o preço: "))
codigo = int(input("Informe o codigo "))

if codigo == 1:
    print("%.2f - Sul" %preco)
elif codigo == 3:
    print("%.2f - Leste" %preco)
elif codigo == 4:
    print("%.2f - Oeste " %preco)
elif codigo == 5 or codigo == 6:
    print("%.2f - Nordeste" %preco)
elif codigo >= 10 and codigo <= 20:
    print("%.2f - Centro-Oeste" %preco)
elif codigo >= 25 and codigo <= 30:
    print("%.2f - Nordeste" %preco)
    