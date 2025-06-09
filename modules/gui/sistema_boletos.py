import tkinter as tk
from typing import List
import datetime

class SistemaBoletos:
    def __init__(self):
        self.boletos_comprados: List[List[int]] = []
        self.frame_lista = None
        self.label_contador = None
        self.label_fecha = None
    
    def agregar_boleto(self, numeros: List[int]) -> bool:
        if len(numeros) == 6 and all(isinstance(n, int) and 1 <= n <= 9 for n in numeros):
            self.boletos_comprados.append(numeros)
            self.actualizar_lista_visual()
            return True
        return False
    
    def crear_panel_boletos(self, parent: tk.Frame) -> tk.Frame:
        panel = tk.Frame(parent, bg='#E5E7EB', relief='ridge', bd=2)
        
        titulo = tk.Label(panel, 
                         text="BOLETOS COMPRADOS",
                         font=('Arial', 12, 'bold'),
                         bg='#E5E7EB',
                         fg='#1F2937')
        titulo.pack(pady=10)
        
        self.label_fecha = tk.Label(panel,
                                  text="",
                                  font=('Arial', 10),
                                  bg='#E5E7EB',
                                  fg='#6B7280')
        self.label_fecha.pack(pady=5)
        self.actualizar_fecha()
        
        self.frame_lista = tk.Frame(panel, bg='#E5E7EB')
        self.frame_lista.pack(fill='both', expand=True, padx=10)
        
        self.label_contador = tk.Label(panel,
                                      text="Total: 0 boletos",
                                      font=('Arial', 10),
                                      bg='#E5E7EB',
                                      fg='#6B7280')
        self.label_contador.pack(pady=5)
        
        boton_limpiar = tk.Button(panel,
                                 text="Limpiar Lista",
                                 command=self.limpiar_lista,
                                 font=('Arial', 9),
                                 bg='#DC2626',
                                 fg='white',
                                 width=12)
        boton_limpiar.pack(pady=10)
        
        return panel
    
    def actualizar_lista_visual(self) -> None:
        """Actualizar la visualización de boletos"""
        # Limpiar lista actual
        for widget in self.frame_lista.winfo_children():
            widget.destroy()
        
        # Mostrar cada boleto
        for i, boleto in enumerate(self.boletos_comprados, 1):
            boleto_str = ''.join(map(str, boleto))
            texto_boleto = f"{i}. {boleto_str}"
            
            label_boleto = tk.Label(self.frame_lista,
                                   text=texto_boleto,
                                   font=('Courier', 12, 'bold'),
                                   bg='#F3F4F6',
                                   fg='#1F2937',
                                   relief='solid',
                                   bd=1)
            label_boleto.pack(fill='x', pady=2)
        
        # Actualizar contador
        self.label_contador.config(text=f"Total: {len(self.boletos_comprados)} boletos")
    
    def actualizar_fecha(self) -> None:
        """Actualizar la fecha y hora mostrada"""
        fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y - %H:%M")
        self.label_fecha.config(text=fecha_actual)
        # Actualizar cada minuto
        self.label_fecha.after(60000, self.actualizar_fecha)
    
    def limpiar_lista(self) -> None:
        """Limpiar la lista de boletos"""
        self.boletos_comprados.clear()
        self.actualizar_lista_visual()
    
    def obtener_boletos(self) -> List[List[int]]:
        """Obtener la lista de boletos comprados"""
        return self.boletos_comprados.copy() 