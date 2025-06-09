from PIL import Image, ImageTk, ImageDraw, ImageFont
import os

class ImageHandler:
    def __init__(self):
        self.rutas = [
            r"C:\\Users\\Sebas\\Desktop\\Python\\LoteriaA2Seb_Dan\\MAYOR-16-MIL-MILLONES-1.png",
            r"LoteriaA2Seb_Dan\\MAYOR-16-MIL-MILLONES-1.png",
            r"assets\\MAYOR-16-MIL-MILLONES-1.png"
        ]

    def cargar_imagen(self, size=(300, 180)):
        for ruta in self.rutas:
            if os.path.exists(ruta):
                try:
                    img = Image.open(ruta).convert('RGBA')
                    img = img.resize(size, Image.LANCZOS)
                    return ImageTk.PhotoImage(img)
                except Exception:
                    continue
        # Si no se encuentra, crear placeholder
        return self.placeholder(size)

    def placeholder(self, size):
        img = Image.new('RGBA', size, (220, 220, 220, 255))
        draw = ImageDraw.Draw(img)
        text = "Sin Imagen"
        font = None
        try:
            font = ImageFont.truetype("arial.ttf", 24)
        except Exception:
            font = ImageFont.load_default()
        w, h = draw.textsize(text, font=font)
        draw.text(((size[0]-w)//2, (size[1]-h)//2), text, fill=(180,0,0), font=font)
        return ImageTk.PhotoImage(img) 