import random

num1 = random.randint(0,9)
num2 = random.randint(2,8)

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
    
print(f"{num1} {op_escolhido} {num2} = ?")

user_resp = int(input("Qual a sua resposta \n"))

if user_resp != resposta:
    print(f"Você errou {resposta}")

else:
    print("Você acertou!")