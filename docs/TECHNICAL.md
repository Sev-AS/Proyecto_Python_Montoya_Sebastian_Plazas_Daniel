# Documentación Técnica - Lotería Virtual

## Estructura del Proyecto

### Módulos Principales

#### 1. GUI (`modules/gui/`)
- **main_window.py**: Ventana principal de la aplicación
  - Maneja la interfaz principal
  - Coordina las diferentes pestañas
  - Gestiona eventos de usuario

- **entrada_numeros.py**: Componente de entrada de números
  - Validación en tiempo real
  - Generación de números aleatorios
  - Interfaz de usuario para selección

#### 2. Lógica (`modules/logic/`)
- **lottery_engine.py**: Motor principal de la lotería
  ```python
  class LotteryEngine:
      def verificar_boleto(self, numeros: List[int], numeros_ganadores: List[int]) -> Tuple[int, int, List[int]]:
          """Verifica un boleto contra números ganadores"""
          
      def calcular_premio(self, aciertos: int) -> int:
          """Calcula el premio según aciertos"""
  ```

- **simulador.py**: Simulador de juegos
  ```python
  class Simulador:
      def simular_juegos(self, num_juegos: int, num_boletos: int = 1) -> str:
          """Simula múltiples juegos y retorna estadísticas"""
  ```

### Flujo de Datos

1. **Entrada de Usuario**
   ```mermaid
   graph LR
   A[Usuario] --> B[Entrada de Números]
   B --> C[Validación]
   C --> D[Generación de Boletos]
   ```

2. **Proceso de Juego**
   ```mermaid
   graph LR
   A[Boletos] --> B[Generación Números Ganadores]
   B --> C[Verificación]
   C --> D[Cálculo Premios]
   D --> E[Actualización Historial]
   ```

## Componentes Técnicos

### Sistema de Premios

```python
class LotteryEngine:
    def calcular_premio(self, aciertos: int) -> int:
        premios = {
            6: 16000000000,
            5: 10000000,
            4: 3750000,
            3: 200000,
            2: 0,
            1: 0,
            0: 0
        }
        return premios.get(aciertos, 0)
```

### Almacenamiento de Datos

- **Formato JSON**
  ```json
  {
    "fecha": "DD/MM/YYYY HH:MM",
    "boletos": [[1,2,3,4,5,6], ...],
    "numeros_ganadores": [1,2,3,4,5,6],
    "total_ganado": 1000000
  }
  ```

## Guía de Desarrollo

### 1. Configuración del Entorno
```bash
pip install -r requirements.txt
```

### 2. Estructura de Código
- Usar docstrings para documentación
- Seguir PEP 8 para estilo de código
- Manejar excepciones apropiadamente

### 3. Testing
- [ ] Implementar tests unitarios

## Mejoras Futuras

### 1. Prioridad Alta
- [ ] Implementar tests unitarios
- [ ] Mejorar manejo de errores
- [ ] Optimizar rendimiento

### 2. Prioridad Media
- [ ] Añadir más estadísticas
- [ ] Mejorar interfaz gráfica
- [ ] Implementar base de datos

### 3. Prioridad Baja
- [ ] Soporte multiidioma
- [ ] Temas personalizables
- [ ] Exportación a más formatos

## Referencias

- [Documentación de Python](https://docs.python.org/3/)
- [Documentación de Tkinter](https://docs.python.org/3/library/tkinter.html)
- [PEP 8 - Guía de Estilo](https://www.python.org/dev/peps/pep-0008/) 