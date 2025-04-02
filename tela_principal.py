import tkinter as tk

# Criar a janela principal
def janela_principal():
    root = tk.Tk()  
    root.title("The Math Game")
    root.geometry("800x600")

    root.resizable(False, False)
    root.continua_jogo = tk.BooleanVar(value = False)
    root.running = True
    # Executar a interface gráfica
    root.mainloop()

# Chamar a função para exibir a janela
janela_principal()
