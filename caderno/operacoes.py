from math import sqrt

def adicao(a, b : int) -> int :
    return a + b
if __name__ == "__main__" :
    """Testando a adicao"""
    #print (adicao(-3, -4))

def subtracao(a, b : int) -> int :
    return a - b
if __name__ == "__main__" :
    """Testando subtracao"""
    #print (subtracao(-2, -5))

def divisao(a, b : int) -> int :
    return a / b

def multiplicacao(a, b : int) -> int :
    return a * b

def potenciacao(a, b : int) -> int :
    return a ** b

def porcentagem(a_d : int, porcentagen: int | float, valor : int | float) -> float :
    if a_d == '1' : # Acrescimo
        resultado = valor + (valor * porcentagen/100)
        return resultado
    elif a_d == '2' : # Desconto
        resultado = valor - (valor * porcentagen/100)
        return resultado
if __name__ == "__main__" :
    """Testtando porcentagem"""
    #escolha = int(input ("Digite '1' para acrescimo '2' para desconto: "))
    #if escolha == 1 : # Acrescimo
        #valor = float(input ("Digite um valor: "))
        #porcentagem_ = float(input ("Digite a porcentagem: "))

    #elif escolha == 2 : # Desconto
        #valor = float(input ("Digite um valor: "))
        #porcentagem_ = float(input ("Digite a porcentagem: "))
#print (f"Diminuindo {porcentagem_}% a {valor} fica {porcentagem(escolha, porcentagem_, valor)}")

def tabuada (a : int) -> int :
    for i in range(1, 10+1) :
        resultado = a * i
        print (f"{a} x {i} = {resultado}")
if __name__ == "__main__" :
    """Testando tabuada"""
    #tabuada(-2)

def raiz_quadrada (a: int) -> float :
    return sqrt(a)

def C_para_F (c : float) -> float :
    f = (c * 9/5) + 32
    return f