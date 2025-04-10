import tkinter as tk
from logica_jogo import *
def comecaJogo():  
    frame = tk.Frame(master=inicio, width=800, height=600, bg="white").place(x=0, y=0)
    pontuacao=tk.Label(frame, text="Pontuação = 0", font="Arial 10", bg="white")
    pontuacao.place(x=200, y=50) 
    partida=tk.Label(frame, text="Partida= 0", font="Arial 10", bg="white")
    partida.place(x=300, y=50) 
    tempo=tk.Label(frame, text="Tempo= 00:00", font="Arial 10", bg="white")
    tempo.place(x=370, y=50) 
    parar=tk.Button(frame, text="Para", font="Arial 10", bg="black", fg="white") 
    parar.place(x=480, y=50)      
    num = tk.Label(frame, text=num1  , font="Arial 30", bg="white")
    num.place(x=200, y=200)
    sinal = tk.Label(frame, text="?", font="Arial 30", bg="white" )
    sinal.place(x=300, y=200)
    num = tk.Label(frame, text=num2 , font="Arial 30", bg="white")
    num.place(x=400, y=200)
    igual = tk.Label(frame, text="=", font="Arial 30", bg="white" )
    igual.place(x=500, y=200)
    resp = tk.Label(frame, text=resposta, font="Arial 30", bg="white" )
    resp.place(x=600, y=200)
    btnOp1 = tk.Button(frame,  text="+", font="Arial 30", height=1, width=2, command=mais)
    btnOp1.place(x=200, y=300)
    btnOp2 = tk.Button(frame, text="-", font="Arial 30", height=1, width=2, command=menos)
    btnOp2.place(x=300, y=300)
    btnOp3 = tk.Button(frame, text="*", font="Arial 30", height=1, width=2, command=mult)
    btnOp3.place(x=400, y=300)
    btnOp4 = tk.Button(frame, text="/", font="Arial 30", height=1, width=2, command=dividir)
    btnOp4.place(x=500, y=300)
    
    
def mais():
    user_resp ='+'
    if user_resp != op_escolhido:
        print("errou")
    else:
        print("acertou")
        certo = tk.Label(inicio, text="Você acertou")
        certo.place(x=600, y=300)
        
def menos():
    user_resp ='-'
    if user_resp != op_escolhido:
        print("errou")
    else:
        print("acertou")
        certo = tk.Label(inicio, text="Você acertou")
        certo.place(x=600, y=300)
          
def mult():
    user_resp ='*'
    if user_resp != op_escolhido:
        print("errou")
    else:
        print("acertou")
        certo = tk.Label(inicio, text="Você acertou")
        certo.place(x=600, y=300)
           
def dividir():
    user_resp ='/'
    if user_resp != op_escolhido:
        print("errou")
    else:
        print("acertou")
        certo = tk.Label(inicio, text="Você acertou")
        certo.place(x=600, y=300)
        
        

        
        
    
     
inicio = tk.Tk()

inicio.geometry("800x600")
inicio.title("The Math Game")
inicio.resizable(False, False)
instrucao = tk.Label(inicio, text=("Clique para começar o jogo"), font="Arial 30")
instrucao.grid(row=0, column=0, pady=100)

btn = tk.Button(inicio, text='Começar jogo', command= comecaJogo)
btn.grid(row = 1, column=0, padx=350, pady=10)


inicio.mainloop()