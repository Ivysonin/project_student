from caderno import operacoes

print ("\n======== Bem-vindo(a) ao caderno do Estudante ========")
print ("------------------ Descrição ------------------")
print ("    Feito para você fazer exercícios de casa.\n")
print ("===== Nossos Serviços:\n")

print ("1 - Adição")
print ("2 - Subtração")
print ("3 - Divisão")
print ("4 - Multíplicação")
print ("5 - Potenciação")
print ("6 - Porcentagem")
print ("7 - Tabuada")
print ("8 - Raiz quadrada")
print ("9 - °C para °F")

while True :
    escolha = input("\n=== Escolha os números de 1 a 9 conforme oque deseja (0 para sair): ")

    if escolha == "0" :
        print ("\n=== Encerrando...\n")
        break

    elif escolha == "1" :
        try:
            num1 = int(input ("====================\nDigite um número: "))
            num2 = int(input ("Digite outro número: "))
            print (f"====================\n{num1} + {num2} = {operacoes.adicao(num1,num2)}\n====================")
        except ValueError :
            print ("\n======== ERRO: digite números inteiros ========")

    elif escolha == "2" :
        try: 
            num1 = int(input ("====================\nDigite um número: "))
            num2 = int(input ("Digite outro número: ")) 
            print (f"====================\n{num1} - {num2} = {operacoes.subtracao(num1,num2)}\n====================")
        except ValueError :
            num1 = int(input ("====================\nDigite um número: "))
            num2 = int(input ("Digite outro número: ")) 
            print (f"====================\n{num1} - {num2} = {operacoes.subtracao(num1,num2)}\n====================")
            print ("\n======== ERRO: digite números inteiros ========")
 
    elif escolha == "3" :
        try:
            num1 = int(input ("====================\nDividendo: "))
            num2 = int(input ("Divisor: ")) 
            print (f"====================\n{num1} ÷ {num2} = {operacoes.divisao(num1,num2)}\n====================")
        except ZeroDivisionError :
            print ("\n======== ERRO: Não existe divisão por 0 ========")
        except ValueError :
            print ("\n======== ERRO: digite números inteiros ========")

    elif escolha == "4" :
        try:
            num1 = int(input ("====================\nDigite um número: "))
            num2 = int(input ("Digite outro número: ")) 
            print (f"====================\n{num1} x {num2} = {operacoes.multiplicacao(num1,num2)}\n====================")        
        except ValueError :
            print ("\n======== ERRO: digite números inteiros ========")

    elif escolha == "5" :
        try:
            num1 = int(input ("====================\nDigite o que você deseja expontenciar: "))
            num2 = int(input ("Digite quanto vai ser essa expontenciação ('2' para quadrada, '3' para cubica, ...): ")) 
            print (f"====================\n{num1}^{num2} = {operacoes.potenciacao(num1,num2)}\n====================")        
        except ValueError :
            print ("\n======== ERRO: digite números inteiros ========")

    elif escolha == "6" : 
        a_d = input("====================\nDigite '1' para acréscimo ou '2' para desconto: ")
        try:
            if a_d == '1' :
                valor = float(input ("====================\nDigite o valor: "))
                porcentagem = float(input ("Digite a porcentagem: "))
                print (f"====================\nAtribuindo {porcentagem}% a {valor}$ = {operacoes.porcentagem(a_d, porcentagem, valor)}$\n====================")        
            elif a_d == '2' : 
                valor = float(input ("====================\nDigite o valor: "))
                porcentagem = float(input ("Digite a porcentagem: "))
                print (f"====================\nDiminuindo {porcentagem}% a {valor}$ = {operacoes.porcentagem(a_d, porcentagem, valor)}$\n====================")        
            else:
                print ("\n======== ERRO: Siga instruções ========")
        except ValueError :
            print ("\n======== ERRO: digite números inteiros ========")

    elif escolha == "7" :
        try:
            numero = int(input ("====================\nDigite um número: "))
            operacoes.tabuada(numero)
            print ("==============")
        except ValueError :
            print ("\n======== ERRO: digite números inteiros ========")

    elif escolha == "8" : 
        try:
            numero = int(input ("====================\nDigite um número: "))
            print (f"A √{numero} é: {round(operacoes.raiz_quadrada(numero), 2)}")
            print ("==============")
        except ValueError:
            print ("\n======== ERRO: digite números inteiros Positivos ========")

    elif escolha == "9" : 
        try:
            c = float(input ("====================\nDigite quantos °C : "))
            print (f"{c}°C convertido para °F fica: {round(operacoes.C_para_F(c), 2)}°F")
            print ("==============")
        except ValueError:
            print ("\n======== ERRO: digite números inteiros Positivos ========")

    else:
        print ("\n======== ERRO: siga Instruções ========")

print("==================== Mais um estudo concluído ====================\n")