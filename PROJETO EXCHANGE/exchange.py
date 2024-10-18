#--------------------------FUNÇÕES----------------------------------------------------------

def acao(): #função que receberá um número do usuário, usado como condição para acessar menus.
    while True: 
        try: #caso o usuário insira texto ou "float" ao invés de um valor int, a linha EXCEPT mostrará uma mensagem e reiniciará o laço.
           valor = int(input("Ação: ")) 
           return valor
               
        except ValueError:
           print("\nPorfavor insira um número válido.\n")

def procuraCPF(x): #função usada para vasculhar o dicionário CADASTROS a busca de uma chave já existente.
    if str(x) in cadastros:
        return(True)
    else:
        return(False)


def cadastro(): #função para realizar o cadastro
    while True:
         nome = input("\nDigite seu nome: ")
         if nome == "": #aqui é verificado se o nome está vazio, futuramente farei uma verificação mais diversa.
            print("\nInsira um nome válido.")
         else:
             break

    while True:

        while True:
            try:
               cpf = int (input("\nDigite seu CPF: "))
            except ValueError: #metodo try para evitar que o usuário utilize letras e símbolos no CPF.
               print("\nPorfavor, utilize apenas números.") 
            else:
                break

        if cpf < 10000000000: #um CPF é composto por 11 números, essa condição confere se o cpf do usuário possui um valor superior a um valor de 11 digitos.
            print("\nPorfavor digite um CPF válido.")

        elif procuraCPF(cpf) == True: #confere se o CPF inserido pelo usuário ja existe
            print("CPF já existe!")

        else:
            break

    while True:
        senha = input("\nDigite sua senha: ")
        if senha == "":
            print("\nInsira uma senha válida.")

        else:
            senha2 = input("\nCONFIRME sua senha: ") #confirmação da senha digitada anteriormente pelo usuário, bem comum na criação de contas, porém não é 100% necessário
            if senha2 != senha:
                print("\nAs senhas não coincidem!")

            else:                
                cadastros[str(cpf)] = str(nome), str(senha) #ao final da função, todas as informações são adicionadas a um dicionario, em uma chave 
                break                                       #relativa ao cpf digitado pelo usuário
                    

def login():
    print("login")


#----------------------LISTAS------------------------------------------------------------------------------------------------------------------------------------------------
cadastros = {}


#----------------------MAIN-----------------------------------------------------------------------------------------------------------------------------------------------------

print("\nBem vindo a CryptoSpy! \nPorfavor, Cadastre-se caso seja novo ou faça Login caso ja possua uma conta \n")

while True:
    print("1. Cadastro \n2. Login\n") #opções disponíveis para entrada do usuário
    resultado = acao() 
    if resultado == 1:
        cadastro()
        print(cadastros)
        print(len(cadastros))
        
        

    elif resultado == 2:
        login()
        break

    else:
        print("\nAção não reconhecida, porfavor insira uma ação correspondente da lista abaixo:\n") #digitar um número que não aparece no menu apenas voltará ao inicio do bloco.

