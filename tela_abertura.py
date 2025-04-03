import tkinter as tk

class TelaInicial:
    def __init__(self, window):
        self.janela = window


    def constroiLayout(self):

        rodape = tk.Label(
            self.janela,
            text ="Desenvolvido por kucetinha.com (Senai Betim 2025)",

            font=("Arial", 8)
        )
        rodape.pack(side="bottom", pady=10)

        self.janela.mainloop()