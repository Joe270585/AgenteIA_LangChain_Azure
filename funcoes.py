def soma(a, b):
    return a + b

def divisao(a, b):
    if b == 0:
        raise ValueError("Divisão por zero não permitida")
    return a / b
