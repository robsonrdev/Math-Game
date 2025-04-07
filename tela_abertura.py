import tkinter as tk

class TelaInicial:
    def __init__(self, window):
        self.janela = window

    def constroiLayout(self):
        # Layout da tela inicial
        rodape = tk.Label(
            self.janela,
            text="Desenvolvido por kucetinha.com (Senai Betim 2025)",
            font=("Arial", 8)
        )
        rodape.pack(side="bottom", pady=10)

# Criação da janela
root = tk.Tk()
root.geometry("800x600")
root.title("Tela Inicial")

# Criação da instância de TelaInicial
tela = TelaInicial(root)
tela.constroiLayout()  # Construa o layout

# Execute o mainloop na instância principal
root.mainloop()
