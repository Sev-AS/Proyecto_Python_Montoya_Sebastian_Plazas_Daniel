# Lotería Virtual - El Hueso

## Descripción
Lotería Virtual es una aplicación de escritorio que simula un juego de lotería. Permite a los usuarios comprar boletos, realizar sorteos y mantener un registro de los resultados.

## Características
- Interfaz gráfica intuitiva
- Sistema de compra de boletos
- Sorteos automáticos
- Historial de juegos
- Estadísticas de resultados
- Simulador de juegos
- Tabla de premios

## Requisitos
- Python 3.8 o superior
- Tkinter (incluido en Python)
- Pillow (PIL)

## Instalación
1. Clonar el repositorio:
```bash
git clone https://github.com/Sev-AS
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Uso
1. Ejecutar la aplicación:
```bash
python main.py
```

2. En la ventana principal:
   - Ingresar números o generar aleatorios
   - Comprar boletos
   - Realizar sorteos
   - Ver resultados y estadísticas

## Estructura del Proyecto
```
loteria-virtual/
├── main.py                 # Punto de entrada de la aplicación
├── requirements.txt        # Dependencias del proyecto
├── data/                  # Datos de la aplicación
│   └── historial.json     # Historial de sorteos
├── modules/               # Módulos principales
│   ├── gui/              # Componentes de interfaz
│   ├── logic/            # Lógica de negocio
│   └── data/             # Manejo de datos
└── assets/               # Recursos estáticos
    └── images/          # Imágenes de la aplicación
```

