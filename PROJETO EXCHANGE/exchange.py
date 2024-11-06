#------------------------------BIBLIOTECAS-------------------------------------------------
from datetime import datetime
import random   

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
        try:
            senha = int(input("\nDigite sua senha: "))
        except ValueError:
            print("\nPorfavor, insira apenas números.")
        else:
            if senha > 999999 or senha < 100000:
                print("\nInsira uma senha válida.")

            else:
                senha2 = int(input("\nCONFIRME sua senha: ")) #confirmação da senha digitada anteriormente pelo usuário, bem comum na criação de contas, porém não é 100% necessário
                if senha2 != senha:
                    print("\nAs senhas não coincidem!")

                else:                
                    cadastros[str(cpf)] = str(nome), str(senha), float(0), [], float(0), float(0), float(0) #ao final da função, todas as informações são adicionadas a um dicionario, em uma chave 
                    break                                       #relativa ao cpf digitado pelo usuário
                    

def login():
    while True:
        global userlogin
        userlogin = input("\nInsira seu CPF associado a uma conta: ")
        if userlogin in cadastros:
            while True:
             global usersenha
             usersenha = input("\nInsira a sua senha: ")
             if usersenha == (cadastros[userlogin][1]):
                 global usuariologado 
                 usuariologado = (cadastros[userlogin][0])
                 global saldousuario
                 saldousuario = (cadastros[userlogin][2])
                 global bitcoinusuario
                 bitcoinusuario = (cadastros[userlogin][4])
                 global etherumusuario
                 etherumusuario = (cadastros[userlogin][5])
                 global rippleusuario
                 rippleusuario = (cadastros[userlogin][6])
                 global usuariosenha
                 return(True)
                 break
             else:
                 print("\nSenha incorreta!")
        else:
            print("\nCPF não cadastrado!")

def verificaSenha(): #essa função será usada para quase toda operação no MENU, ira bater a senha inserida ANTES de realizar uma transação, com a senha registrada em seu CPF
    senhatest = input("\nConfirme sua senha: ")
    if senhatest == (cadastros[userlogin][1]):
        return True
    else:
        return False

def consultaSaldo():
    if verificaSenha() == True:
        print("\nBRL: %.2f" %saldousuario)
        print("\nBTC: %.8f" %bitcoinusuario)
        print("\nETH: %.8f" %etherumusuario)
        print("\nXRP: %.3f" %rippleusuario)
    else:
        print("\nSenha inválida!")

def consultaExtrato():
    print("\nNome: " + usuariologado + "\nCPF: " + userlogin + "\n")
    print(*cadastros[userlogin][3], sep='\n')


def saque():
    global saldousuario
    if verificaSenha() == True:
        try:
            sacado = float (input("\nQuanto deseja sacar?: R$"))
        except ValueError:
            print("\nEntrada inválida.")
        else:
            if saldousuario - sacado >= 0:  #verificando se o usuario tem saldo o suficiente para tal transação, caso o valor final seja inferior a 0, a ação é cancelada
                saldousuario = saldousuario - sacado #atribui o novo saldo ao usuario, subtraindo o valor do saque
                print("\nValor do saque: R$%.2f" %sacado)
                print("Novo saldo: R$%.2f" %saldousuario)
                data_hora_atual = datetime.now()
                data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
                extrato = (str(data_hora_formatada) + ' - ' + str(sacado) + " BRL")
                cadastros[userlogin][3].append(extrato)
                cadastros[userlogin] = (cadastros[userlogin][0], cadastros[userlogin][1], saldousuario, cadastros[userlogin][3], bitcoinusuario, etherumusuario, rippleusuario)
            else:
                print("\nTransação inválida! Saldo insuficiente.")
    else:
        print("\nSenha incorreta!")
    
def comprarCripto():
    print("\nCotação Atual: \n", btc_price, "\n", eth_price, "\n", xrp_price, "\nDeseja Continuar?")
    while True:
        print("\n1. Sim \n2. Não\n")
        resultado = acao()
        if resultado == 1:
            global saldousuario
            print("\nQual moeda deseja comprar? \n1. Bitcoin \n2. Ethereum \n3. Ripple\n")
            resultado = acao()
            if resultado == 1:
                global bitcoinusuario
                valor = float(input("\nQuanto deseja comprar? (em R$): \n"))
                valortaxado = valor + ((valor / 100)*2)
                if valortaxado <= saldousuario:
                    saldousuario = saldousuario - valortaxado
                    bitcoinusuario = bitcoinusuario + (valor / btc_price)
                    break
                else:
                    print("\nSaldo Insuficiente.")
            elif resultado ==2:
                global etherumusuario
                valor = float(input("\nQuanto deseja comprar? (em R$): \n"))
                valortaxado = valor + ((valor / 100)*1)
                if valortaxado <= saldousuario:
                    saldousuario = saldousuario - valortaxado
                    etherumusuario = etherumusuario + (valor / eth_price)
                    break
                else:
                    print("Saldo Insuficiente.")
            elif resultado ==3:
                global rippleusuario
                valor = float(input("\nQuanto deseja comprar? (em R$): \n"))
                valortaxado = valor + ((valor / 100)*1)
                if valortaxado <= saldousuario:
                    saldousuario = saldousuario - valortaxado
                    rippleusuario = rippleusuario + (valor / xrp_price)
                    break
                else:
                    print("\nSaldo Insuficiente.")
            elif resultado ==4:
                break
        elif resultado == 2:
            break
        else:
            ("\nOpção Inválida")
    
    
def venderCripto():
    print("\nCotação Atual: \n", btc_price, "\n", eth_price, "\n", xrp_price, "\nDeseja Continuar?")
    while True:
        print("\n1. Sim \n2. Não\n")
        resultado = acao()
        if resultado == 1:
            global saldousuario
            print("\nQual moeda deseja vender? \n1. Bitcoin \n2. Ethereum \n3. Ripple\n")
            resultado = acao()
            if resultado == 1:
                global bitcoinusuario
                valor = float(input("\nQuanto deseja vender? (em BTC): \n"))
                if valor <= bitcoinusuario:
                    valortaxado = valor - (((valor * btc_price) / 100) * 3) 
                    bitcoinusuario = bitcoinusuario - valor
                    saldousuario = valortaxado
                    break
                else:
                    print("\nSaldo Insuficiente.")
            elif resultado ==2:
                global etherumusuario
                valor = float(input("\nQuanto deseja vender? (em BTC): \n"))
                if valor <= bitcoinusuario:
                    valortaxado = valor - (((valor * btc_price) / 100) * 3) 
                    etherumusuario = bitcoinusuario - valor
                    saldousuario = valortaxado
                else:
                    print("Saldo Insuficiente.")
            elif resultado ==3:
                global rippleusuario
                valor = float(input("\nQuanto deseja comprar? (em R$): \n"))
                valortaxado = valor + ((valor / 100)*1)
                if valortaxado <= saldousuario:
                    saldousuario = saldousuario - valortaxado
                    rippleusuario = rippleusuario + (valor / xrp_price)
                    break
                else:
                    print("\nSaldo Insuficiente.")
            elif resultado ==4:
                break
        elif resultado == 2:
            break
        else:
            ("\nOpção Inválida")
    
def atualizarCota():
    dice = random.randint(0,1)
    global btc_price
    global eth_price
    global xrp_price
    if dice == 0:
        btc_price = btc_price + ((btc_price / 100) * 5)
        eth_price = eth_price + ((eth_price / 100) * 5)
        xrp_price = xrp_price + ((xrp_price / 100) * 5)
        print("\nCotação Atual: \n", btc_price, "\n", eth_price, "\n", xrp_price)
    else:
        btc_price = btc_price - ((btc_price / 100) * 5)
        eth_price = eth_price - ((eth_price / 100) * 5)
        xrp_price = xrp_price - ((xrp_price / 100) * 5)
        print("\nCotação Atual: \n", btc_price, "\n", eth_price, "\n", xrp_price)
    
def deposito():
    global saldousuario
    if verificaSenha() == True:
        try:
            depositado = float (input("\nQuanto deseja depositar?: R$"))
        except ValueError:
            print("Entrada inválida.")
        else:
            saldousuario = saldousuario + depositado
            print("\nValor depositado: R$%.2f" %depositado)
            print("Novo saldo: R$%.2f" %saldousuario)
            data_hora_atual = datetime.now()
            data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
            extrato = (str(data_hora_formatada) + ' + ' + str(depositado) + " BRL")
            cadastros[userlogin][3].append(extrato)
            cadastros[userlogin] = (cadastros[userlogin][0], cadastros[userlogin][1], saldousuario, cadastros[userlogin][3], bitcoinusuario, etherumusuario, rippleusuario)


    else:
        print("\nSenha incorreta!")


#----------------------VARIÁVEIS------------------------------------------------------------------------------------------------------------------------------------------------
cadastros = {
    '53406698824':('kaique','123456',200,[],1,1,1)
    }
extrato = []
btc_price = 402484.10
xrp_price = 2.95
eth_price = 14070.10


#----------------------MAIN-----------------------------------------------------------------------------------------------------------------------------------------------------

print("\nBem vindo a CryptoSpy! \nPorfavor, Cadastre-se caso seja novo ou faça Login caso ja possua uma conta")

while True:
    while True:
        print("\n1. Cadastro \n2. Login \n3. Sair \n") #opções disponíveis para entrada do usuário
        resultado = acao() 
    
        if resultado == 1:
            cadastro()
            
            
    
        elif resultado == 2:
            if login() == True:
                break
    
        elif resultado == 3:
            exit()
    
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