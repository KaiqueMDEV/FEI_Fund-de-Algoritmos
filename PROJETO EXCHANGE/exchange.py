#------------------------------BIBLIOTECAS----------------------------------------------------------------------------------------------------------------------------------------

from datetime import datetime
import random   
import json
from funcExchange import *

#----------------------VARIÁVEIS------------------------------------------------------------------------------------------------------------------------------------------------

#No programa, todas as informações do usuário são guardadas em um dicionário "CADASTROS", onde cada KEY é o próprio CPF do usuário.
#As KEYS precisam ser CPF pois ele é único a cada indivíduo, já nomes e senhas podem conflitar.
#Dentro do CPF do usuário, temos (na ordem): o NOME, SENHA, SALDO, EXTRATO, BTC, ETH e XRP.

with open('cadastros.json', 'r') as f:
    cadastros = json.load(f)  # Lê o arquivo e converte de volta para um dicionário

#cotação das moedas, obtidas no dia 5/11 as 16:30 (todas em R$)

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
            cadastro(cadastros)
            
            
    
        elif resultado == 2:
            if login(cadastros) == True:
                with open('dados.txt', 'r') as file:
                   usuariologado = file.read()
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
            consultaSaldo(cadastros)
        elif resultado == 2:
            consultaExtrato(cadastros)
        elif resultado == 3:
            deposito(cadastros)
        elif resultado == 4:
            saque(cadastros)
        elif resultado == 5:
            comprarCripto(cadastros)
        elif resultado == 6:
            venderCripto(cadastros)
        elif resultado == 7:
            atualizarCota()
        elif resultado == 8:
            with open('cadastros.json', 'w') as f:                                                   #relativa ao cpf digitado pelo usuário  
                        json.dump(cadastros, f)
            break
        else:
            print("\nAção não reconhecida, porfavor insira uma ação correspondente da lista abaixo:")