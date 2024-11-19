print ("\n======== Bem-vindo(a) ao caderno do Estudante ========\n")
print ("------------------ Descrição ------------------")
print ("Feito para você fazer exercícios de casa.\n")
print ("===== Nossos produtos:\n")

print ("1 - Adição")
print ("2 - Subtração")
print ("3 - Divisão")
print ("4 - Multíplicação")
print ("5 - Potenciação")
print ("6 - Porcentagem")
print ("7 - Tabuada")
print ("8 - °C para °F")

while True :
    escolha = int(input("\n=== Escolha os números de 1 a 8 conforme oque deseja (0 para sair): "))

    if escolha == 0 :
        print ("\n=== saindo...\n")
        break