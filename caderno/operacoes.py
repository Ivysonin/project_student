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

def multiplicacao(a, b : int) -> int :
    return a * b

def divisao(a, b : int) -> int :
    return a / b

def potenciacao(a, b : int) -> int :
    return a ** b

def tabuada (a : int) -> int :
    for i in range(10+1) :
        resultado = a * i
        print (f"{a} x {i} = {resultado}")
if __name__ == "__main__" :
    """Testando tabuada"""
    #tabuada(-2)

def C_para_F (c):
    f = (c * 9/5) + 32
    return f