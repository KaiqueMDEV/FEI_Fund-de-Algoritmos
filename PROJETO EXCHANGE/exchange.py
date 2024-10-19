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
    while True:
        userlogin = input("\nInsira seu CPF associado a uma conta: ")
        if userlogin in cadastros:
            while True:
             usersenha = input("\nInsira a sua senha: ")
             if usersenha == (cadastros[userlogin][1]):
                 global usuariologado 
                 usuariologado = (cadastros[userlogin][0])
                 return(True)
                 break
             else:
                 print("\nSenha incorreta!")
        else:
            print("\nCPF não cadastrado!")

def consultaSaldo():
    print()

def consultaExtrato():
    print()
    
def saque():
    print()
    
def comprarCripto():
    print()
    
def venderCripto():
    print()
    
def atualizarCota():
    print()
    
def deposito():
    print()


#----------------------LISTAS------------------------------------------------------------------------------------------------------------------------------------------------
cadastros = {
    '53406698824':('kaique','12345')
    }


#----------------------MAIN-----------------------------------------------------------------------------------------------------------------------------------------------------

print("\nBem vindo a CryptoSpy! \nPorfavor, Cadastre-se caso seja novo ou faça Login caso ja possua uma conta \n")

while True:
    print("1. Cadastro \n2. Login\n") #opções disponíveis para entrada do usuário
    resultado = acao() 
    if resultado == 1:
        cadastro()
        
        

    elif resultado == 2:
        if login() == True:
            break

    else:
        print("\nAção não reconhecida, porfavor insira uma ação correspondente da lista abaixo:\n") #digitar um número que não aparece no menu apenas voltará ao inicio do bloco.


print("\nOlá %s seja bem vindo(a) a CryptoSpy!\nO que deseja fazer em seguida?" %usuariologado)
while True:
    print("\n1. Consultar saldo\n2. Consultar Extrato\n3. Depositar\n4. Sacar\n5. Comprar criptomoedas\n6. Vender criptomoedas\n7. Atualizar Cotação\n8. Sair\n")
    resultado = acao() 
    if resultado == 1:
        consultaSaldo()
    elif resultado == 2:
        consultaExtrato()
    elif resultado == 3:
        deposito()
    elif resultado == 4:
        saque()
    elif resultado == 5:
        comprarCripto()
    elif resultado == 6:
        venderCripto()
    elif resultado == 7:
        atualizarCota()
    elif resultado == 8:
        break
    else:
        print("\nAção não reconhecida, porfavor insira uma ação correspondente da lista abaixo:")