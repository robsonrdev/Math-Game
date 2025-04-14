import tkinter as tk
from logica import gerar_nova_operacao
from tkinter import messagebox

# Variáveis globais para atualizar depois
labels = {}
pontos = 0
partida = 0
ja_marcou = False


def gerar_nova_questao():
    global op_escolhido, partida, ja_marcou
    ja_marcou = False
    partida += 1
    num1, num2, op_escolhido, resposta = gerar_nova_operacao()
    
    tk.Label(inicio, text=f"Partida: {partida}", font="Arial 10", bg='#000040', fg="white").place(x=300, y=50)
    labels["num1"].config(text=num1, bg='#000040', fg="white")
    labels["num2"].config(text=num2, bg='#000040', fg="white")
    labels["resposta"].config(text=resposta, bg='#000040', fg="white")
    labels["sinal"].config(text="?", bg='#000040', fg="white")
    certo = tk.Label(inicio, text="   ",  width=100, height=10, bg='#000040', fg="white").place(x=600, y=300)  
    errado = tk.Label(inicio, text="     ",  width=100, height=10, bg='#000040', fg="white") .place(x=600, y=300) 
    # Esconde a resposta real por enquanto

def comecaJogo():  
    frame = tk.Frame(master=inicio, width=800, height=600, bg='#000040')
    frame.place(x=0, y=0)
    global pontos
    rodape= tk.Label(frame, text="Desenvolvido por: Robson Rodrigues, Luiz Fernando e Italo Sales (Senai Betim 2025)", font="Arial 10", bg='#000040', fg="white").place(x=150, y=575)
    tk.Label(frame, text=f"Pontos :{pontos}", font="Arial 10", bg='#000040', fg="white").place(x=200, y=50)
    tk.Label(frame, text=f"Partida: {partida}", font="Arial 10", bg='#000040', fg="white").place(x=300, y=50)
    tk.Label(frame, text="Tempo= 00:00", font="Arial 10", bg='#000040', fg="white").place(x=370, y=50)
    tk.Button(frame, text="Para", font="Arial 10", bg='white', fg="black").place(x=480, y=50)

    # Gera a primeira operação
    global op_escolhido
    num1, num2, op_escolhido, resposta = gerar_nova_operacao()

    labels["num1"] = tk.Label(frame, text=num1, font="Arial 30", bg='#000040', fg="white")
    labels["num1"].place(x=200, y=200)

    labels["sinal"] = tk.Label(frame, text="?", font="Arial 30", bg='#000040', fg="white")
    labels["sinal"].place(x=300, y=200)

    labels["num2"] = tk.Label(frame, text=num2, font="Arial 30", bg='#000040', fg="white")
    labels["num2"].place(x=400, y=200)

    tk.Label(frame, text="=", font="Arial 30", bg='#000040', fg="white").place(x=500, y=200)

    labels["resposta"] = tk.Label(frame, text=resposta, font="Arial 30", bg='#000040', fg="white")
    labels["resposta"].place(x=600, y=200)

    # Botões das operações
    tk.Button(frame, text="+", font="Arial 30", height=1, width=2, command=mais, bg='#02476f', fg='white').place(x=200, y=300)
    tk.Button(frame, text="-", font="Arial 30", height=1, width=2, command=menos, bg='#02476f', fg='white').place(x=300, y=300)
    tk.Button(frame, text="*", font="Arial 30", height=1, width=2, command=mult, bg='#02476f', fg='white').place(x=400, y=300)
    tk.Button(frame, text="/", font="Arial 30", height=1, width=2, command=dividir, bg='#02476f', fg='white').place(x=500, y=300)

    # Botão para gerar nova questão
    tk.Button(frame, text="Nova Questão", font="Arial 12", command=gerar_nova_questao, bg='#02476f', fg='white').place(x=350, y=400)


def mais():
    global pontos, ja_marcou
    if op_escolhido != '+':
        certo = tk.Label(inicio, text="Errou", font="Arial 15", fg="red", bg='#000040').place(x=600, y=300)
        #if/else para tirar os pontos se for maior que zero
        if ja_marcou == False:
         if pontos == 0:
             pontos = pontos
             ja_marcou == True
         else:
            pontos -= 1
            ja_marcou = True
        tk.Label(inicio, text=f'{pontos}', font="Arial 10", bg='#000040', fg="white").place(x=250, y=50)
    else:
      errado = tk.Label(inicio, text="Acertou", font="Arial 15", fg="green", bg='#000040').place(x=600, y=300)
      if ja_marcou == False:
          pontos+=1
          ja_marcou = True
      tk.Label(inicio, text=f'{pontos}', font="Arial 10", bg='#000040', fg="white").place(x=250, y=50)
      
def menos():
    global pontos, ja_marcou
    if op_escolhido != '-':
        certo = tk.Label(inicio, text="Errou", font="Arial 15", fg="red", bg='#000040').place(x=600, y=300)
        #if/else para tirar os pontos se for maior que zero
        if ja_marcou == False:
         if pontos == 0:
             pontos = pontos
             ja_marcou == True
         else:
            pontos -= 1
            ja_marcou = True
        tk.Label(inicio, text=f'{pontos}', font="Arial 10", bg='#000040', fg="white").place(x=250, y=50)
    else:
      errado = tk.Label(inicio, text="Acertou", font="Arial 15", fg="green", bg='#000040').place(x=600, y=300)
      if ja_marcou == False:
          pontos+=1
          ja_marcou = True
      tk.Label(inicio, text=f'{pontos}', font="Arial 10", bg='#000040', fg="white").place(x=250, y=50) 
       
def mult():
   global pontos, ja_marcou
   if op_escolhido != '*':
        certo = tk.Label(inicio, text="Errou", font="Arial 15", fg="red", bg='#000040').place(x=600, y=300)
        #if/else para tirar os pontos se for maior que zero
        if ja_marcou == False:
         if pontos == 0:
             pontos = pontos
             ja_marcou == True
         else:
            pontos -= 1
            ja_marcou = True
        tk.Label(inicio, text=f'{pontos}', font="Arial 10", bg='#000040', fg="white").place(x=250, y=50)
   else:
      errado = tk.Label(inicio, text="Acertou", font="Arial 15", fg="green", bg='#000040').place(x=600, y=300)
      if ja_marcou == False:
          pontos+=1
          ja_marcou = True
      tk.Label(inicio, text=f'{pontos}', font="Arial 10", bg='#000040', fg="white").place(x=250, y=50)
      
def dividir():
    global pontos, ja_marcou
    if op_escolhido != '/':
        certo = tk.Label(inicio, text="Errou", font="Arial 15", fg="red", bg='#000040').place(x=600, y=300)
        #if/else para tirar os pontos se for maior que zero
        if ja_marcou == False:
         if pontos == 0:
             pontos = pontos
             ja_marcou == True
         else:
            pontos -= 1
            ja_marcou = True
        tk.Label(inicio, text=f'{pontos}', font="Arial 10", bg='#000040', fg="white").place(x=250, y=50)
    else:
      errado = tk.Label(inicio, text="Acertou", font="Arial 15", fg="green", bg='#000040').place(x=600, y=300)
      if ja_marcou == False:
          pontos+=1
          ja_marcou = True
      tk.Label(inicio, text=f'{pontos}', font="Arial 10", bg='#000040', fg="white").place(x=250, y=50)
    


def funcao_fechar():
    if messagebox.askysesno("Confirmação", "Você realmente deseja sair?"):
        inicio.runnig = False
        inicio.continua_jogo.set(True)
        inicio.destroy()


inicio = tk.Tk()
inicio.geometry("800x600")
inicio.title("The Math Game")
inicio.resizable(False, False)
inicio.config(bg='#000040')

instrucao = tk.Label(inicio, text="Clique na operação que corresponde ao resultado entre dois números mostrados\n.Operações: |+|-|/|*|", font="Arial 10", bg='#000040', fg="white")
instrucao.grid(row=0, column=0, pady=100)
rodape= tk.Label(inicio, text="Desenvolvido por: Robson Rodrigues, Luiz Fernando e Italo Sales (Senai Betim 2025)", font="Arial 10", bg='#000040', fg="white").place(x=150, y=575)
btn = tk.Button(inicio, text='Jogar', command=comecaJogo, height=5, width=10, bg='#02476f', fg='white')
btn.grid(row=1, column=0, padx=350, pady=10)

inicio.mainloop()
