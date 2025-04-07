import random

num1 = random.randint(0,9)
num2 = random.randint(0,9)

operador = ["+", "-", "*", "/"]
op_escolhido = random.choice(operador)

print(f"{num1} {op_escolhido} {num2} = ?")

