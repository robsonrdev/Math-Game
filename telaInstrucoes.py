import tkinter as tk
from logica import gerar_nova_operacao
from tkinter import messagebox

labels = {}
pontos = 0
partida = 0
ja_marcou = False
tempo_restante = 60
tempo_label = None
pontuacao_label = None
op_escolhido = ""

def gerar_nova_questao():
    global op_escolhido, partida, ja_marcou
    ja_marcou = False
    partida += 1

    if partida > 20:
        final_jogo()
        return

    num1, num2, op_escolhido, resposta = gerar_nova_operacao()
    atualizar_placar()
    
    labels["num1"].config(text=num1)
    labels["num2"].config(text=num2)
    labels["resposta"].config(text=resposta)
    labels["sinal"].config(text="?")

def fim_do_tempo():
    frame_fim = tk.Frame(master=inicio, width=800, height=600, bg="darkred")
    frame_fim.place(x=0, y=0)

    tk.Label(frame_fim, text=" O tempo acabou!",height=800, width=600, font=("Arial", 30, "bold"), fg="white", bg="red").pack(pady=50)
    tk.Label(frame_fim, text=f"Você marcou {pontos} ponto(s)", font=("Arial", 20), fg="white", bg="red").pack(pady=10)

    tk.Button(frame_fim, text="Jogar Novamente", font=("Arial", 14), bg="#02476f", fg="white", command=recomecar).pack(pady=20)
    tk.Button(frame_fim, text="Sair", font=("Arial", 14), bg="#800000", fg="white", command=fechar_jogo).pack(pady=10)

def atualizar_tempo():
    global tempo_restante
    if tempo_restante > 0:
        tempo_restante -= 1
        tempo_label.config(text=f"Tempo: {tempo_restante:02d}")
        inicio.after(1000, atualizar_tempo)
    else:
        fim_do_tempo()

def aumentar_tempo():
    global tempo_restante
    tempo_restante += 5
    tempo_label.config(text=f"Tempo: {tempo_restante:02d}")

def diminuir_tempo():
    global tempo_restante
    tempo_restante -= 5
    if tempo_restante < 0:
        tempo_restante = 0
    tempo_label.config(text=f"Tempo: {tempo_restante:02d}")

def atualizar_placar():
    tempo_label.config(text=f"Tempo: {tempo_restante:02d}")
    pontuacao_label.config(text=f"Pontos: {pontos}")
    partida_label.config(text=f"Partida: {partida}")

def final_jogo():
    frame_final = tk.Frame(master=inicio, width=800, height=600, bg="green")
    frame_final.place(x=0, y=0)

    tk.Label(frame_final, text="Fim de Jogo",height=800, width=600, font=("Arial", 30, "bold"), fg="white", bg="#001f3f").pack(pady=50)
    tk.Label(frame_final, text=f"Você marcou {pontos} ponto(s)!", font=("Arial", 20), fg="white", bg="#001f3f").pack(pady=10)

    tk.Button(frame_final, text="Jogar Novamente", font=("Arial", 14), bg="#02476f", fg="white", command=recomecar).pack(pady=20)
    tk.Button(frame_final, text="Sair", font=("Arial", 14), bg="#800000", fg="white", command=fechar_jogo).pack(pady=10)

def recomecar():
    global pontos, partida, tempo_restante
    pontos = 0
    partida = 0
    tempo_restante = 60
    comecaJogo()

def responder(op):
    global pontos, ja_marcou
    if ja_marcou:
        return

    if op == op_escolhido:
        pontos += 1
        aumentar_tempo()
        msg = "Acertou"
        cor = "green"
    else:
        if pontos > 0:
            pontos -= 1
        diminuir_tempo()
        msg = "Errou"
        cor = "red"

    ja_marcou = True
    tk.Label(inicio, text=msg, font="Arial 15", fg=cor, bg='#000040').place(x=600, y=300)
    atualizar_placar()
    inicio.after(500, gerar_nova_questao)

def comecaJogo():
    global tempo_label, pontuacao_label, partida_label
    frame = tk.Frame(master=inicio, width=800, height=600, bg='#000040')
    frame.place(x=0, y=0)

    rodape = tk.Label(frame, text="Desenvolvido por: Robson, Luiz e Italo (Senai Betim 2025)", font="Arial 10", bg='#000040', fg="white").place(x=150, y=575)
    
    pontuacao_label = tk.Label(frame, text=f"Pontos: {pontos}", font="Arial 10", bg='#000040', fg="white")
    pontuacao_label.place(x=200, y=50)
    
    partida_label = tk.Label(frame, text=f"Partida: {partida}", font="Arial 10", bg='#000040', fg="white")
    partida_label.place(x=300, y=50)
    
    tempo_label = tk.Label(frame, text=f"Tempo: {tempo_restante:02d}", font="Arial 10", bg='#000040', fg="white")
    tempo_label.place(x=400, y=50)

    botoes = [("+", 200), ("-", 300), ("*", 400), ("/", 500)]
    for simb, x in botoes:
        tk.Button(frame, text=simb, font="Arial 30", height=1, width=2,
                  command=lambda s=simb: responder(s), bg='#02476f', fg='white').place(x=x, y=300)

    labels["num1"] = tk.Label(frame, text="", font="Arial 30", bg='#000040', fg="white")
    labels["num1"].place(x=200, y=200)

    labels["sinal"] = tk.Label(frame, text="?", font="Arial 30", bg='#000040', fg="white")
    labels["sinal"].place(x=300, y=200)

    labels["num2"] = tk.Label(frame, text="", font="Arial 30", bg='#000040', fg="white")
    labels["num2"].place(x=400, y=200)

    tk.Label(frame, text="=", font="Arial 30", bg='#000040', fg="white").place(x=500, y=200)

    labels["resposta"] = tk.Label(frame, text="", font="Arial 30", bg='#000040', fg="white")
    labels["resposta"].place(x=600, y=200)

    atualizar_tempo()
    gerar_nova_questao()

def fechar_jogo():
    if messagebox.askyesno("Sair", "Tem certeza que deseja fechar o jogo?"):
        inicio.destroy()

inicio = tk.Tk()
inicio.geometry("800x600")
inicio.title("The Math Game")
inicio.resizable(False, False)
inicio.config(bg='#000040')

tk.Label(inicio, text="Clique na operação que corresponde ao resultado entre dois números mostrados.\nOperações: +, -, *, /", font="Arial 10", bg='#000040', fg="white").pack(pady=100)
tk.Button(inicio, text='Jogar', command=comecaJogo, height=5, width=10, bg='#02476f', fg='white').pack()

tk.Label(inicio, text="Desenvolvido por: Robson, Luiz e Italo (Senai Betim 2025)", font="Arial 10", bg='#000040', fg="white").pack(side=tk.BOTTOM, pady=5)

inicio.protocol("WM_DELETE_WINDOW", fechar_jogo)
inicio.mainloop()
