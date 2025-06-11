"""
Ventana principal de la aplicación de Lotería Virtual
"""
import tkinter as tk
from tkinter import ttk, messagebox
import datetime
from PIL import Image, ImageTk
from typing import List, Dict
from pathlib import Path
from ..logic.lottery_engine import LotteryEngine
from ..logic.simulador import Simulador
from ..data.history_manager import HistoryManager
from modules.gui.entrada_numeros import EntradaNumeros
from modules.gui.display_imagen import ImagenPremio
from modules.gui.sistema_boletos import SistemaBoletos
import random

class MainWindow:
    def __init__(self, root: tk.Tk):
        """
        Inicializa la ventana principal
        
        Args:
            root: Ventana raíz de tkinter
        """
        self.root = root
        self.root.title("Lotería Virtual - El Hueso")
        self.root.geometry("1000x800")
        self.root.configure(bg='#F8F9FA')
        self.root.state('zoomed')  # Ejecutar en pantalla completa

        # Obtener ruta base de la aplicación
        self.base_path = Path(__file__).parent.parent.parent

        # Inicializar componentes
        self.lottery_engine = LotteryEngine()
        self.history_manager = HistoryManager()
        self.sistema_boletos = SistemaBoletos()
        self.simulador = Simulador()
        
        # Variables de control
        self.boletos_comprados = []
        self.juego_en_progreso = False
        
        # Variables para simulación
        self.num_juegos_var = tk.StringVar(value="100")
        self.num_boletos_sim_var = tk.StringVar(value="1")

        # Crear Notebook como contenedor principal
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)

        # Crear pestañas
        self.tab_principal = tk.Frame(self.notebook, bg='#F8F9FA')
        self.tab_historial = tk.Frame(self.notebook, bg='white')
        self.tab_estadisticas = tk.Frame(self.notebook, bg='white')
        self.tab_premios = tk.Frame(self.notebook, bg='white')
        self.tab_simulacion = tk.Frame(self.notebook, bg='white')

        self.notebook.add(self.tab_principal, text='Principal')
        self.notebook.add(self.tab_historial, text='Historial')
        self.notebook.add(self.tab_estadisticas, text='Estadísticas')
        self.notebook.add(self.tab_premios, text='Premios')
        self.notebook.add(self.tab_simulacion, text='Simulación')

        # Configurar cada pestaña
        self.configurar_tab_principal()
        self.configurar_tab_historial()
        self.configurar_tab_estadisticas()
        self.configurar_tab_premios()
        self.configurar_tab_simulacion()

        # Iniciar actualización de fecha/hora en todas las pestañas
        self.actualizar_fecha_hora()

        # Forzar actualización de pestañas al iniciar
        self.actualizar_historial()
        self.actualizar_estadisticas()
        self.actualizar_premios()

    def configurar_tab_principal(self):
        # Título y fecha
        tk.Label(self.tab_principal,
                text="LOTERÍA VIRTUAL EL HUESO",
                font=('Arial', 20, 'bold'),
                bg='#F8F9FA',
                fg='#1F2937').pack(pady=5)
        self.label_fecha = tk.Label(self.tab_principal,
                                  text="",
                                  font=('Arial', 10),
                                  bg='#F8F9FA',
                                  fg='#4B5563')
        self.label_fecha.pack()

        # Imagen del premio
        self.imagen_premio = ImagenPremio(self.tab_principal)
        self.imagen_premio.mostrar()

        # Frame principal para dividir en dos columnas
        main_frame = tk.Frame(self.tab_principal, bg='#F8F9FA')
        main_frame.pack(fill='both', expand=True, padx=5, pady=5)

        # Frame izquierdo: boletos y controles
        left_frame = tk.Frame(main_frame, bg='#F8F9FA')
        left_frame.pack(side=tk.LEFT, fill='both', expand=True)

        # Frame derecho: resultados
        right_frame = tk.Frame(main_frame, bg='#F8F9FA')
        right_frame.pack(side=tk.RIGHT, fill='both', expand=True)

        # Frame para entrada de números (izquierda)
        entrada_frame = tk.Frame(left_frame, bg='#F8F9FA')
        entrada_frame.pack(pady=10)
        self.entrada_numeros = EntradaNumeros(entrada_frame)

        # Frame para botones de compra (izquierda)
        botones_compra_frame = tk.Frame(left_frame, bg='#F8F9FA')
        botones_compra_frame.pack(pady=5)

        tk.Button(botones_compra_frame,
                 text="Generar Números",
                 command=self.entrada_numeros.generar_numeros_aleatorios,
                 font=('Arial', 10, 'bold'),
                 bg='#4CAF50',
                 fg='white',
                 padx=10,
                 pady=3).pack(side=tk.LEFT, padx=3)

        tk.Button(botones_compra_frame,
                 text="Comprar Boleto",
                 command=self.comprar_boleto,
                 font=('Arial', 10, 'bold'),
                 bg='#2563EB',
                 fg='white',
                 padx=10,
                 pady=3).pack(side=tk.LEFT, padx=3)

        # Frame para lista de boletos (izquierda)
        boletos_frame = tk.Frame(left_frame, bg='#F8F9FA')
        boletos_frame.pack(fill='both', expand=True, pady=5)
        tk.Label(boletos_frame,
                text="BOLETOS COMPRADOS:",
                font=('Arial', 12, 'bold'),
                bg='#F8F9FA',
                fg='#1F2937').pack(pady=3)
        self.lista_boletos = tk.Text(boletos_frame,
                                   height=4,
                                   font=('Courier', 10),
                                   bg='white',
                                   fg='black')
        self.lista_boletos.pack(fill='both', expand=True, padx=5)

        # Frame para botones de juego (izquierda)
        botones_juego_frame = tk.Frame(left_frame, bg='#F8F9FA')
        botones_juego_frame.pack(pady=5)
        self.boton_jugar = tk.Button(botones_juego_frame,
                                   text="¡JUGAR!",
                                   command=self.jugar,
                                   font=('Arial', 12, 'bold'),
                                   bg='#DC2626',
                                   fg='white',
                                   padx=15,
                                   pady=3,
                                   state='disabled')
        self.boton_jugar.pack(side=tk.LEFT, padx=3)
        tk.Button(botones_juego_frame,
                 text="Limpiar Lista",
                 command=self.limpiar_lista,
                 font=('Arial', 10, 'bold'),
                 bg='#6B7280',
                 fg='white',
                 padx=10,
                 pady=3).pack(side=tk.LEFT, padx=3)

        # Frame para resultados (derecha)
        self.resultado_frame = tk.Frame(right_frame, bg='#F8F9FA')
        self.resultado_frame.pack(fill='both', expand=True, pady=5)
        self.label_resultado = tk.Label(self.resultado_frame,
                                      text="",
                                      font=('Arial', 10),
                                      bg='white',
                                      fg='black',
                                      justify=tk.LEFT,
                                      wraplength=250,
                                      anchor='n')
        self.label_resultado.pack(fill='both', expand=True, padx=5, pady=3)

    def configurar_tab_simulacion(self) -> None:
        """Configura el contenido de la pestaña de simulación"""
        # Frame principal centrado
        main_frame = tk.Frame(self.tab_simulacion, bg='white')
        main_frame.pack(fill='both', expand=True)
        
        # Frame para controles (centrado)
        controles_frame = tk.Frame(main_frame, bg='white')
        controles_frame.pack(pady=20)
        
        # Título
        tk.Label(controles_frame,
                text="SIMULADOR DE LOTERÍA",
                font=('Arial', 16, 'bold'),
                bg='white',
                fg='black').pack(pady=(0, 20))
        
        # Frame para entradas
        entradas_frame = tk.Frame(controles_frame, bg='white')
        entradas_frame.pack(pady=10)
        
        # Entrada para número de juegos
        tk.Label(entradas_frame,
                text="Número de Juegos:",
                font=('Arial', 12),
                bg='white',
                fg='black').pack(side=tk.LEFT, padx=5)
                
        tk.Entry(entradas_frame,
                textvariable=self.num_juegos_var,
                width=10,
                font=('Arial', 12),
                fg='black',
                justify='center').pack(side=tk.LEFT, padx=5)
        
        # Entrada para número de boletos por juego
        tk.Label(entradas_frame,
                text="Boletos por Juego:",
                font=('Arial', 12),
                bg='white',
                fg='black').pack(side=tk.LEFT, padx=5)
                
        tk.Entry(entradas_frame,
                textvariable=self.num_boletos_sim_var,
                width=10,
                font=('Arial', 12),
                fg='black',
                justify='center').pack(side=tk.LEFT, padx=5)
        
        # Botón de simulación
        tk.Button(controles_frame,
                 text="SIMULAR",
                 command=self.ejecutar_simulacion,
                 font=('Arial', 12, 'bold'),
                 bg='#2563EB',
                 fg='white',
                 padx=20,
                 pady=5).pack(pady=20)
        
        # Separador
        tk.Frame(main_frame, height=2, bg='#E5E7EB').pack(fill='x', padx=50)
        
        # Frame para resultados con scrollbar
        frame_resultados = tk.Frame(main_frame, bg='white')
        frame_resultados.pack(fill='both', expand=True, padx=50, pady=20)
        
        # Scrollbar
        scrollbar = tk.Scrollbar(frame_resultados)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Texto para mostrar resultados
        self.texto_resultados = tk.Text(frame_resultados,
                                      font=('Courier', 12),
                                      bg='white',
                                      fg='black',
                                      wrap=tk.WORD,
                                      padx=20,
                                      pady=20,
                                      yscrollcommand=scrollbar.set)
        self.texto_resultados.pack(fill='both', expand=True)
        scrollbar.config(command=self.texto_resultados.yview)
        
        # Configurar el texto para que esté centrado
        self.texto_resultados.tag_configure("center", justify='center')

    def ejecutar_simulacion(self) -> None:
        """Ejecuta la simulación de juegos"""
        try:
            # Obtener parámetros
            num_juegos = int(self.num_juegos_var.get())
            num_boletos = int(self.num_boletos_sim_var.get())
            
            if num_juegos <= 0 or num_boletos <= 0:
                messagebox.showerror("Error", "Los números deben ser positivos")
                return
            
            # Limpiar resultados anteriores
            self.texto_resultados.delete(1.0, tk.END)
            
            # Ejecutar simulación
            resultados = self.simulador.simular_juegos(num_juegos, num_boletos)
            
            # Mostrar resultados centrados
            self.texto_resultados.insert(tk.END, resultados, "center")
            
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese números válidos")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error durante la simulación: {str(e)}")

    def configurar_tab_historial(self) -> None:
        """Configura el contenido de la pestaña de historial"""
        # Área de texto con scroll
        frame = tk.Frame(self.tab_historial, bg='white')
        frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.texto_historial = tk.Text(frame,
                                     height=10,
                                     font=('Arial', 12),
                                     bg='white',
                                     fg='black',
                                     yscrollcommand=scrollbar.set)
        self.texto_historial.pack(fill='both', expand=True)
        scrollbar.config(command=self.texto_historial.yview)
        
        # Botón de eliminar
        tk.Button(self.tab_historial,
                 text="Eliminar Historial",
                 command=self.eliminar_historial,
                 font=('Arial', 12, 'bold'),
                 bg='#DC2626',
                 fg='white',
                 padx=15,
                 pady=5).pack(pady=5)

    def eliminar_historial(self) -> None:
        """Elimina todo el historial de sorteos"""
        if messagebox.askyesno("Confirmar", "¿Está seguro que desea eliminar todo el historial?"):
            self.history_manager.limpiar_historial()
            self.actualizar_premios()

    def configurar_tab_estadisticas(self) -> None:
        """Configura el contenido de la pestaña de estadísticas"""
        # Área de texto con scroll
        frame = tk.Frame(self.tab_estadisticas, bg='white')
        frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.texto_estadisticas = tk.Text(frame,
                                        height=10,
                                        font=('Arial', 12),
                                        bg='white',
                                        fg='black',
                                        yscrollcommand=scrollbar.set)
        self.texto_estadisticas.pack(fill='both', expand=True)
        scrollbar.config(command=self.texto_estadisticas.yview)
        
    def configurar_tab_premios(self) -> None:
        """Configura el contenido de la pestaña de premios"""
        # Área de texto con scroll
        frame = tk.Frame(self.tab_premios, bg='white')
        frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.texto_premios = tk.Text(frame,
                                   height=10,
                                   font=('Arial', 12),
                                   bg='white',
                                   fg='black',
                                   yscrollcommand=scrollbar.set)
        self.texto_premios.pack(fill='both', expand=True)
        scrollbar.config(command=self.texto_premios.yview)
        
        # Mostrar tabla de premios
        self.actualizar_premios()

    def actualizar_fecha_hora(self) -> None:
        """Actualiza la fecha y hora en la interfaz"""
        now = datetime.datetime.now()
        fecha_hora = now.strftime("%d/%m/%Y - %H:%M")
        self.label_fecha.config(text=f"Fecha: {fecha_hora}")
        self.root.after(60000, self.actualizar_fecha_hora)  # Actualizar cada minuto

    def comprar_boleto(self) -> None:
        """Agrega un boleto a la lista de comprados"""
        if self.juego_en_progreso:
            messagebox.showwarning("Aviso", "No se pueden comprar boletos durante un juego en progreso")
            return

        es_valido, numeros = self.entrada_numeros.validar_entrada_completa()
        if not es_valido:
            messagebox.showerror("Error", numeros)
            return

        self.boletos_comprados.append(numeros)
        self.actualizar_lista_boletos()
        self.entrada_numeros.limpiar()
        self.boton_jugar.config(state='normal')

    def actualizar_lista_boletos(self) -> None:
        """Actualiza la lista de boletos en la interfaz"""
        self.lista_boletos.delete(1.0, tk.END)
        for i, boleto in enumerate(self.boletos_comprados, 1):
            self.lista_boletos.insert(tk.END, f"{i}. {' - '.join(map(str, boleto))}\n")

    def limpiar_lista(self) -> None:
        """Limpia la lista de boletos"""
        if self.juego_en_progreso:
            messagebox.showwarning("Aviso", "No se puede limpiar la lista durante un juego en progreso")
            return

        self.boletos_comprados = []
        self.actualizar_lista_boletos()
        self.boton_jugar.config(state='disabled')

    def jugar(self) -> None:
        """Ejecuta el juego con los boletos comprados"""
        if not self.boletos_comprados:
            self.label_resultado.config(text="Debes comprar al menos un boleto para jugar")
            messagebox.showwarning("Aviso", "Debes comprar al menos un boleto para jugar")
            return

        try:
            self.juego_en_progreso = True
            self.boton_jugar.config(state='disabled')
            self.label_resultado.config(text="Juego en progreso...")
            
            # Generar número aleatorio como ganador (1-9)
            numeros_ganadores = random.sample(range(1, 10), 6)
            self.label_resultado.config(text=f"Juego en progreso...\nNúmeros ganadores: {' - '.join(map(str, numeros_ganadores))}")
            
            # Verificar boletos
            resultados = self.lottery_engine.verificar_boletos(self.boletos_comprados, numeros_ganadores)
            
            # Mostrar resultados
            self.mostrar_resultados(numeros_ganadores, resultados)
            
            # Actualizar historial
            self.history_manager.agregar_sorteo(
                self.boletos_comprados,
                numeros_ganadores,
                sum(r['premio'] for r in resultados)
            )
            
            # Actualizar pestañas
            self.actualizar_historial()
            self.actualizar_estadisticas()
            
        except Exception as e:
            self.label_resultado.config(text=f"Error durante el juego: {str(e)}")
            messagebox.showerror("Error", f"Ocurrió un error durante el juego: {str(e)}")
        finally:
            self.juego_en_progreso = False
            self.boton_jugar.config(state='normal')
            self.limpiar_lista()

    def mostrar_resultados(self, numeros_ganadores: List[int], resultados: List[Dict]) -> None:
        """Muestra los resultados del sorteo en la ventana principal"""
        texto = f"NÚMERO GANADOR: {' - '.join(map(str, numeros_ganadores))}\n\n"
        
        for resultado in resultados:
            texto += f"Boleto {resultado['boleto']}: {' - '.join(map(str, resultado['numeros']))} → "
            texto += f"{resultado['aciertos']} aciertos"
            if resultado['premio'] > 0:
                texto += f" → Premio: ${resultado['premio']:,}\n"
            else:
                texto += "\n"
        
        self.label_resultado.config(text=texto)
        self.label_resultado.update_idletasks()

    def actualizar_historial(self) -> None:
        """Actualiza el contenido de la pestaña de historial"""
        self.texto_historial.delete(1.0, tk.END)
        self.texto_historial.insert(tk.END, "HISTORIAL DE SORTEOS\n\n")
        
        if not self.history_manager.historial:
            self.texto_historial.insert(tk.END, "No hay sorteos registrados\n")
            return
            
        for sorteo in self.history_manager.historial:
            self.texto_historial.insert(tk.END, f"Fecha: {sorteo['fecha']}\n")
            self.texto_historial.insert(tk.END, f"Ganadores: {' - '.join(map(str, sorteo['numeros_ganadores']))}\n")
            self.texto_historial.insert(tk.END, f"Total Ganado: ${sorteo['total_ganado']:,}\n\n")

    def actualizar_estadisticas(self) -> None:
        """Actualiza el contenido de la pestaña de estadísticas"""
        self.texto_estadisticas.delete(1.0, tk.END)
        self.texto_estadisticas.insert(tk.END, "ESTADÍSTICAS\n\n")
        
        estadisticas = self.history_manager.obtener_estadisticas()
        
        if estadisticas['total_sorteos'] == 0:
            self.texto_estadisticas.insert(tk.END, "No hay datos estadísticos disponibles\n")
            return
            
        self.texto_estadisticas.insert(tk.END, f"Total de Sorteos: {estadisticas['total_sorteos']}\n")
        self.texto_estadisticas.insert(tk.END, f"Total de Boletos: {estadisticas['total_boletos']}\n")
        self.texto_estadisticas.insert(tk.END, f"Total Ganado: ${estadisticas['total_ganado']:,}\n")
        self.texto_estadisticas.insert(tk.END, f"Promedio de Boletos por Sorteo: {estadisticas['promedio_boletos']:.1f}\n")
        self.texto_estadisticas.insert(tk.END, f"Promedio de Ganancia por Sorteo: ${estadisticas['promedio_ganancia']:,.2f}\n")

    def actualizar_premios(self) -> None:
        """Actualiza el contenido de la pestaña de premios"""
        self.texto_premios.delete(1.0, tk.END)
        self.texto_premios.insert(tk.END, "TABLA DE PREMIOS\n\n")
        
        premios = [
            (6, "$16,000,000,000", "Premio Mayor"),
            (5, "$10,000,000", "Premio Grande"),
            (4, "$3,750,000", "Premio Mediano"),
            (3, "$200,000", "Premio Pequeño"),
            (2, "Sin premio", "Sin premio"),
            (1, "Sin premio", "Sin premio"),
            (0, "Sin premio", "Sin premio")
        ]
        
        for aciertos, premio, descripcion in premios:
            self.texto_premios.insert(tk.END, f"{aciertos} aciertos: {premio} - {descripcion}\n") 