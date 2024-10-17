def acao():
    while True:
        try:
           valor = int(input("Ação: "))
           return valor
               
        except ValueError:
           print("\nPorfavor insira um número válido.\n")


def cadastro():
    while True:
         nome = input("\nDigite seu nome: ")
         if nome == "":
            print("\nInsira um nome válido.")
         else:
             break

    while True:
        while True:
            try:
               cpf = int (input("\nDigite seu CPF: "))
            except ValueError:
               print("\nPorfavor, utilize apenas números.")
            else:
                break
        if cpf < 10000000000:
            print("\nPorfavor digite um CPF válido.")
        else:
            break
    while True:
        senha = input("\nDigite sua senha: ")
        if senha == "":
            print("\nInsira uma senha válida.")
        else:
            senha2 = input("\nCONFIRME sua senha: ")
            if senha2 != senha:
                print("\nAs senhas não coincidem!")
            else:
                break
                 
    


def login():
    print("login")




#----------------------------------
print("\nBem vindo a CryptoSpy! \nPorfavor, Cadastre-se caso seja novo ou faça Login caso ja possua uma conta \n")
while True:
    print("1. Cadastro \n2. Login\n")
    resultado = acao() 
    if resultado == 1:
        cadastro()
        break

    elif resultado == 2:
        login()
        break

    else:
        print("\nAção não reconhecida, porfavor insira uma ação correspondente da lista abaixo:\n")