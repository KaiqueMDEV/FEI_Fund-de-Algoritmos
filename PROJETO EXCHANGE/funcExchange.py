from datetime import datetime
import random   
import json

global userlogin

btc_price = 402484.10
xrp_price = 2.95
eth_price = 14070.10

def acao(): #função que receberá um número do usuário, usado como condição para acessar menus.
    while True: 
        try: #caso o usuário insira texto ou "float" ao invés de um valor int, a linha EXCEPT mostrará uma mensagem e reiniciará o laço.
           valor = int(input("Ação: ")) 
           return valor
               
        except ValueError:
           print("\nPorfavor insira um número válido.\n")

def procuraCPF(x,cadastros): #função usada para vasculhar o dicionário CADASTROS a busca de uma chave já existente.
    if str(x) in cadastros:
        return(True)
    else:
        return(False)


def cadastro(cadastros): #função para realizar o cadastro
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

        elif procuraCPF(cpf,cadastros) == True: #confere se o CPF inserido pelo usuário ja existe
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
                    with open('cadastros.json', 'a') as f:                                                   #relativa ao cpf digitado pelo usuário  
                        json.dump(cadastros, f)  # Grava o dicionário em formato JSON no arquivo
                    break                                       
                    

def login(cadastros):
    while True:
        global userlogin
        userlogin = input("\nInsira seu CPF associado a uma conta: ") #usuário entra com um cpf  
        if userlogin in cadastros: #verifica se o cpf inserido pelo uusário se encontra no dicionário "cadastros"
            while True:
             global usersenha
             usersenha = input("\nInsira a sua senha: ") #agora pede o value "senha" associado a key "cpf" inserida anteriormente
             if usersenha == (cadastros[userlogin][1]): #verificação se o valor bate com a chave.
                 global usuariologado 
                 usuariologado = (cadastros[userlogin][0]) #caso o login seja bem sucedido, as variáveis são atualizadas para receber as que estão registradas no dicionário.
                 global saldousuario
                 saldousuario = (cadastros[userlogin][2])
                 global bitcoinusuario
                 bitcoinusuario = (cadastros[userlogin][4])
                 global etherumusuario
                 etherumusuario = (cadastros[userlogin][5])
                 global rippleusuario
                 rippleusuario = (cadastros[userlogin][6])
                 with open('dados.txt', 'w') as file:
                    file.write(usuariologado)
                 return(True)
                 break
             else:
                 print("\nSenha incorreta!")
        else:
            print("\nCPF não cadastrado!")

def verificaSenha(cadastros): #essa função será usada para quase toda operação no MENU, ira bater a senha inserida ANTES de realizar uma transação, com a senha registrada em seu CPF
    senhatest = input("\nConfirme sua senha: ")
    if senhatest == (cadastros[userlogin][1]): #compara a senha inserida com o valor no dicionário, semelhante ao login
        return True
    else:
        return False

def consultaSaldo(cadastros):
    if verificaSenha(cadastros) == True:
        #todos os saldos em cada moeda com as formatações que melhor se adequam a eles
        print("\nBRL: %.2f" %saldousuario)
        print("\nBTC: %.8f" %bitcoinusuario)
        print("\nETH: %.8f" %etherumusuario)
        print("\nXRP: %.2f" %rippleusuario)
    else:
        print("\nSenha inválida!")

def consultaExtrato(cadastros):
    if verificaSenha(cadastros) == True:
         print("\nNome: " + usuariologado + "\nCPF: " + userlogin + "\n") #exibe o nome do usuário logado e seu cpf
         print(*cadastros[userlogin][3], sep='\n') #exibe a lista de extratos presente no dicionário, com uma separação de quebra de linha entre cada item, usando o sep='\n'


def saque(cadastros):
    global saldousuario
    if verificaSenha(cadastros) == True:
        try:
            sacado = float (input("\nQuanto deseja sacar?: R$"))
        except ValueError:
            print("\nEntrada inválida.")
        else:
            if saldousuario - sacado >= 0:  #verificando se o usuario tem saldo o suficiente para tal transação, caso o valor final seja inferior a 0, a ação é cancelada
                saldousuario = saldousuario - sacado #atribui o novo saldo ao usuario, subtraindo o valor do saque
                print("\nValor do saque: R$%.2f" %sacado)
                print("Novo saldo: R$%.2f" %saldousuario)
                data_hora_atual = datetime.now() #declara uma variável que chama a função datetime.now, que exibe a data e hora atuais no dispositivo
                data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S") #declara uma outra variável que formata a data e hora atual de forma mais organizada
                extrato = (str(data_hora_formatada) + ' - ' + str(sacado) + " BRL") #ao final do saque, todas as informações são concatenadas em uma variável
                cadastros[userlogin][3].append(extrato) #esta variável é adicionada a lista de extratos do dicionário
                #valores de um dicionário não podem ser modificados, são como tulpas, então é necessário redefini-lo por completo:
                cadastros[userlogin] = (cadastros[userlogin][0], cadastros[userlogin][1], saldousuario, cadastros[userlogin][3], bitcoinusuario, etherumusuario, rippleusuario)
            else:
                print("\nTransação inválida! Saldo insuficiente.")
    else:
        print("\nSenha incorreta!")
    
def comprarCripto(cadastros):
    if verificaSenha(cadastros) == True:           
            global etherumusuario
            global rippleusuario
            data_hora_atual = datetime.now()
            data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
            print("\nCotação Atual: \nBTC: ", btc_price, "\nETH: ", eth_price, "\nXRP: ", xrp_price) #exibe a cotação mais recente do programa
            while True:
                print("\nDeseja Continuar?")
                print("\n1. Sim \n2. Não\n")
                resultado = acao()
                if resultado == 1:
                        global saldousuario
                        print("\nQual moeda deseja comprar?\n \n1. Bitcoin \n2. Ethereum \n3. Ripple \n4. Sair\n")
                        resultado = acao()
                        if resultado == 1:
                            global bitcoinusuario
                            try:
                                valor = float(input("\nQuanto deseja comprar? R$: "))
                            except ValueError:
                                print("\nValor inválido.")
                            else:
                                valortaxado = valor + ((valor / 100)*2) #aplica uma taxa de x% (relativa ao tipo da criptomoeda) na compra da moeda
                                if valortaxado <= saldousuario: #verifica se o valor COM TAXA está no saldo do usuario para realizar a operação.
                                    saldousuario = saldousuario - valortaxado #subtrai o valor taxado do saldo do usuário
                                    bitcoinusuario = bitcoinusuario + (valor / btc_price) #divide o valor em REAIS pelo preço da moeda e adiciona o resultado à carteira de criptmoedas do usuário.
                                    valorfinal_str = "{:.2f}".format(valortaxado)
                                    extrato = (str(data_hora_formatada) + ' - ' + valorfinal_str + " BRL" + " CT: " + "{:.2f}".format(btc_price) + "     TX: 0.02 SALDO: R$ " + "{:.2f}".format(saldousuario) + " BTC: " + str(bitcoinusuario))
                                    cadastros[userlogin][3].append(extrato)
                                    cadastros[userlogin] = (cadastros[userlogin][0], cadastros[userlogin][1], saldousuario, cadastros[userlogin][3], bitcoinusuario, etherumusuario, rippleusuario)
                                    print("\nSucesso!")
                                    break
                                else:
                                    print("\nSaldo Insuficiente.")
                        elif resultado ==2:
                            try:
                                valor = float(input("\nQuanto deseja comprar? R$: ")) #usuario entra com um valor em reais
                            except ValueError:
                                print("\nValor Inválido.")
                            else:
                                valortaxado = valor + ((valor / 100)*1)
                                if valortaxado <= saldousuario:
                                    saldousuario = saldousuario - valortaxado
                                    etherumusuario = etherumusuario + (valor / eth_price)
                                    valorfinal_str = "{:.2f}".format(valortaxado)
                                    extrato = (str(data_hora_formatada) + ' - ' + valorfinal_str + " BRL" + " CT: " + "{:.2f}".format(eth_price) + "     TX: 0.02 SALDO: R$ " + "{:.2f}".format(saldousuario) + " ETH: " + str(etherumusuario))
                                    cadastros[userlogin][3].append(extrato)
                                    cadastros[userlogin] = (cadastros[userlogin][0], cadastros[userlogin][1], saldousuario, cadastros[userlogin][3], bitcoinusuario, etherumusuario, rippleusuario)
                                    print("\nSucesso!")
                                    break
                                else:
                                    print("Saldo Insuficiente.")
                        elif resultado ==3:
                            try:
                                valor = float(input("\nQuanto deseja comprar? R$: "))
                            except ValueError:
                                print("\nValor Inválido.")
                            else:
                                valortaxado = valor + ((valor / 100)*1)
                                if valortaxado <= saldousuario:
                                    saldousuario = saldousuario - valortaxado
                                    rippleusuario = rippleusuario + (valor / xrp_price)
                                    valorfinal_str = "{:.2f}".format(valortaxado)
                                    extrato = (str(data_hora_formatada) + ' - ' + valorfinal_str + " BRL" + " CT: " + "{:.2f}".format(xrp_price) + "     TX: 0.02 SALDO: R$ " + "{:.2f}".format(saldousuario) + " XRP: " + str(rippleusuario))
                                    cadastros[userlogin][3].append(extrato)
                                    cadastros[userlogin] = (cadastros[userlogin][0], cadastros[userlogin][1], saldousuario, cadastros[userlogin][3], bitcoinusuario, etherumusuario, rippleusuario)
                                    print("\nSucesso!")
                                    break
                                else:
                                    print("\nSaldo Insuficiente.")
        
                        elif resultado == 4:
                            break
                        print("\nOpção inválida.\n")
                elif resultado == 2:
                    break
    else:
        print("Senha incorreta!")
        
     
    
def venderCripto(cadastros):
    if verificaSenha(cadastros) == True:
        global etherumusuario
        global bitcoinusuario
        global rippleusuario
        data_hora_atual = datetime.now()
        data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
        print("\nCotação Atual: \n", "\nBTC: ", btc_price, "\nETH: ", eth_price, "\nXRP: ", xrp_price)
        while True:
            print("\nDeseja Continuar?")
            print("\n1. Sim \n2. Não\n")
            resultado = acao()
            if resultado == 1:
                    global saldousuario
                    print("\nQual moeda deseja vender? \n1. Bitcoin \n2. Ethereum \n3. Ripple\n4. Sair\n")
                    resultado = acao()
                    if resultado == 1:
                        global bitcoinusuario
                        try:
                            valor = float(input("\nQuanto deseja vender? (em BTC): \n")) #usuario entra com um valor de criptomoeda
                        except ValueError:
                            print("\nValor Inválido.")
                        else:
                            if valor <= bitcoinusuario: #verifica se o usuário possui o valor em cripto para realizar a operação.
                                valortaxado = ((valor * btc_price) / 100) * 3 #aplica uma taxa de x% (Relativa ao tipo da criptmoeda) no valor obtido da venda da criptomoeda
                                valorfinal = ((valor * btc_price) - valortaxado)
                                bitcoinusuario = bitcoinusuario - valor
                                saldousuario = saldousuario + valorfinal
                                valorfinal_str = "{:.2f}".format(valorfinal)
                                extrato = (str(data_hora_formatada) + ' + ' + valorfinal_str + " BRL" + " CT: " + "{:.2f}".format(btc_price) + "     TX: 0.03 SALDO: R$ " + "{:.2f}".format(saldousuario) + " BTC: " + str(bitcoinusuario))
                                cadastros[userlogin][3].append(extrato)
                                cadastros[userlogin] = (cadastros[userlogin][0], cadastros[userlogin][1], saldousuario, cadastros[userlogin][3], bitcoinusuario, etherumusuario, rippleusuario)
                                print("\nSucesso!")
                                break
                            else:
                                print("\nSaldo Insuficiente.")
                    elif resultado ==2:
                        try:
                            valor = float(input("\nQuanto deseja vender? (em ETH): \n"))
                        except ValueError:
                            print("\nValor Inválido.")
                        else:
                            if valor <= etherumusuario:
                                valortaxado = ((valor * eth_price) / 100) * 2
                                valorfinal = ((valor * eth_price) - valortaxado)
                                etherumusuario = etherumusuario - valor
                                saldousuario = saldousuario + valorfinal
                                valorfinal_str = "{:.2f}".format(valorfinal)
                                extrato = (str(data_hora_formatada) + ' + ' + valorfinal_str + " BRL" + " CT: " + "{:.2f}".format(eth_price) + "    TX: 0.02 SALDO: R$ " + "{:.2f}".format(saldousuario) + " ETH: " + str(etherumusuario))
                                cadastros[userlogin][3].append(extrato)
                                cadastros[userlogin] = (cadastros[userlogin][0], cadastros[userlogin][1], saldousuario, cadastros[userlogin][3], bitcoinusuario, etherumusuario, rippleusuario)
                                print("\nSucesso!")
                                break
                            else:
                                print("\nSaldo Insuficiente.")
                    elif resultado ==3:
                        try:
                            valor = float(input("\nQuanto deseja vender? (em XRP): \n"))
                        except ValueError:
                            print("\nValor Inválido.")
                        else:
                            if valor <= rippleusuario:
                                valortaxado = ((valor * xrp_price) / 100) * 2
                                valorfinal = ((valor * xrp_price) - valortaxado)
                                rippleusuario = rippleusuario - valor
                                saldousuario = saldousuario + valorfinal
                                valorfinal_str = "{:.2f}".format(valorfinal)
                                extrato = (str(data_hora_formatada) + ' + ' + valorfinal_str + " BRL" + " CT: " + "{:.2f}".format(xrp_price) + "    TX: 0.01 SALDO: R$ " + "{:.2f}".format(saldousuario) + " XRP: " + str(rippleusuario))
                                cadastros[userlogin][3].append(extrato)
                                cadastros[userlogin] = (cadastros[userlogin][0], cadastros[userlogin][1], saldousuario, cadastros[userlogin][3], bitcoinusuario, etherumusuario, rippleusuario)
                                print("\nSucesso!")
                                break
                            else:
                                print("\nSaldo Insuficiente.")
                    elif resultado == 4:
                        break
                    else:
                        print("\nOpção Inválida.\n")

            elif resultado == 2:
                break
            else:
                ("\nOpção Inválida")
    else:
        print("Senha inválida!")

def atualizarCota():
    dice = random.randint(0,1) #gera um número de 0 a 1 (chance de 50/50)
    global btc_price
    global eth_price
    global xrp_price
    if dice == 0: #se o número for 0, a cotação da moeda aumenta em 5% do valor anterior
        btc_price = btc_price + ((btc_price / 100) * 5)
        eth_price = eth_price + ((eth_price / 100) * 5)
        xrp_price = xrp_price + ((xrp_price / 100) * 5)
        print("\nCotação Atual: \n", btc_price, "\n", eth_price, "\n", xrp_price)
    else: #se o número for 1, diminui em 5% do valor anterior
        btc_price = btc_price - ((btc_price / 100) * 5)
        eth_price = eth_price - ((eth_price / 100) * 5)
        xrp_price = xrp_price - ((xrp_price / 100) * 5)
        print("\nCotação Atual: \n", btc_price, "\n", eth_price, "\n", xrp_price)
    
def deposito(cadastros):
    global saldousuario
    if verificaSenha(cadastros) == True:
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