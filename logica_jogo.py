import random
from tela_instrucoes import *


num1 = random.randint(0,9)
num2 = random.randint(0,9)

operador = ["+", "-", "*", "/"]

op_escolhido = random.choice(operador)

if op_escolhido == "+":
    resposta = num1 + num2
    
elif op_escolhido == "-":
    resposta = num1 - num2

elif op_escolhido == "/":
    resposta = num1 / num2
    
else:
    resposta = num1 * num2
