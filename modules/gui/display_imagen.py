"""
Manejador de imágenes para la interfaz gráfica
"""
import tkinter as tk
from PIL import Image, ImageTk
from pathlib import Path

class ImagenPremio:
    def __init__(self, parent: tk.Widget):
        """
        Inicializa el manejador de imágenes
        
        Args:
            parent: Widget padre donde se mostrará la imagen
        """
        self.parent = parent
        self.base_path = Path(__file__).parent.parent.parent
        self.ruta_imagen = self.base_path / "assets" / "MAYOR-16-MIL-MILLONES-1.png"
        self.imagen = None
        self.photo = None

    def mostrar(self) -> None:
        """Muestra la imagen del premio"""
        try:
            if self.ruta_imagen.exists():
                self.imagen = Image.open(self.ruta_imagen)
                # Redimensionar la imagen a un tamaño adecuado para la interfaz
                self.imagen = self.imagen.resize((500, 300), Image.Resampling.LANCZOS)
                self.photo = ImageTk.PhotoImage(self.imagen)
                label = tk.Label(self.parent, image=self.photo, bg='#F8F9FA')
                label.image = self.photo
                label.pack(pady=10)
            else:
                self.crear_placeholder()
        except Exception as e:
            print(f"Error al mostrar imagen: {str(e)}")
            self.crear_placeholder()

    def mostrar_centrado(self, ancho: int = 300, alto: int = 200) -> None:
        """
        Muestra la imagen centrada con dimensiones específicas
        
        Args:
            ancho: Ancho de la imagen
            alto: Alto de la imagen
        """
        try:
            if self.ruta_imagen.exists():
                self.imagen = Image.open(self.ruta_imagen)
                self.imagen = self.imagen.resize((ancho, alto), Image.Resampling.LANCZOS)
                self.photo = ImageTk.PhotoImage(self.imagen)
                label = tk.Label(self.parent, image=self.photo, bg='#F8F9FA')
                label.image = self.photo
                label.pack(pady=10)
            else:
                self.crear_placeholder()
        except Exception as e:
            print(f"Error al mostrar imagen centrada: {str(e)}")
            self.crear_placeholder()

    def crear_placeholder(self) -> None:
        """Crea una imagen placeholder si no se encuentra la imagen original"""
        try:
            # Crear imagen placeholder
            self.imagen = Image.new('RGB', (300, 200), color='#E5E7EB')
            self.photo = ImageTk.PhotoImage(self.imagen)
            label = tk.Label(self.parent, image=self.photo, bg='#F8F9FA')
            label.image = self.photo
            label.pack(pady=10)
        except Exception as e:
            print(f"Error al crear placeholder: {str(e)}") 