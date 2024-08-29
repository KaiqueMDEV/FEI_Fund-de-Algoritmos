n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))

m = (n1 + n2) / 2

if m >= 5:
    print("Aprovado direto!!!")
else:
    exame = float(input("Informe a nota do exame: "))
    m = (m + exame) / 2
    if (m >= 5):
        print("Aprovado pelo exame!")
    else:
        print("Reprovado pelo exame!")