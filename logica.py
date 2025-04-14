import random

def gerar_nova_operacao():
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    operador = random.choice(["+", "-", "*", "/"])

    if operador == "+":
        resposta = num1 + num2
    elif operador == "-":
        resposta = num1 - num2
    elif operador == "*":
        resposta = num1 * num2
    else:
        resposta = num1 / num2

    return num1, num2, operador, resposta