import tkinter as tk
import random

class EntradaNumeros:
    def __init__(self, parent):
        self.parent = parent
        self.numero_var = tk.StringVar()
        self.crear_campo_entrada()

    def crear_campo_entrada(self):
        frame = tk.Frame(self.parent, bg='#F8F9FA')
        frame.pack(pady=10)
        
        tk.Label(frame, text="Ingrese 6 números (1-9):", 
                font=('Arial', 12), bg='#F8F9FA').pack(side=tk.LEFT, padx=5)
        
        self.campo = tk.Entry(frame, textvariable=self.numero_var,
                            font=('Courier', 16, 'bold'),
                            width=8, justify='center')
        self.campo.pack(side=tk.LEFT, padx=5)
        
        self.registro_validacion = self.parent.register(self.validar_entrada)
        self.campo.config(validate='key', validatecommand=(self.registro_validacion, '%P'))

    def validar_entrada(self, valor):
        if valor == "":
            return True
        if len(valor) > 6:
            return False
        return valor.isdigit() and all('1' <= c <= '9' for c in valor)

    def validar_entrada_completa(self):
        valor = self.numero_var.get()
        if len(valor) != 6:
            return False, "Debe ingresar exactamente 6 números"
        if not all('1' <= c <= '9' for c in valor):
            return False, "Los números deben estar entre 1 y 9"
        return True, [int(c) for c in valor]

    def generar_numeros_aleatorios(self):
        numeros_seleccionados = random.sample(range(1, 10), 6)
        self.numero_var.set(''.join(map(str, numeros_seleccionados)))
        self.campo.focus_set()

    def limpiar(self):
        self.numero_var.set('')
        self.campo.focus_set()

    def obtener_numero(self):
        valor = self.numero_var.get()
        return [int(c) for c in valor] if valor else [] 