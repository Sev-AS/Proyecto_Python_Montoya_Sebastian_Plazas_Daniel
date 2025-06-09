"""
Simulador de lotería para análisis estadístico
"""
import random
from typing import List, Dict, Any
from .lottery_engine import LotteryEngine

class Simulador:
    def __init__(self):
        """Inicializa el simulador de lotería"""
        self.lottery_engine = LotteryEngine()
        
    def generar_numeros_ganadores_aleatorios(self) -> List[int]:
        """Genera números ganadores aleatorios para la simulación"""
        return random.sample(range(1, 10), 6)
        
    def simular_juegos(self, num_juegos: int, num_boletos: int = 1) -> str:
        """
        Simula múltiples juegos de lotería
        
        Args:
            num_juegos: Número de juegos a simular
            num_boletos: Número de boletos por juego
            
        Returns:
            str: Texto formateado con los resultados de la simulación
        """
        resultados = {
            'total_juegos': num_juegos,
            'total_boletos': num_juegos * num_boletos,
            'aciertos': [0] * 7,  # 0-6 aciertos
            'premios': [0] * 7,   # 0-6 aciertos
            'total_ganado': 0,
            'boletos_ganadores': [],
            'boletos_perdedores': [],
            'numeros_ganadores': []
        }
        
        for juego in range(num_juegos):
            # Generar boletos aleatorios
            boletos = [random.sample(range(1, 10), 6) for _ in range(num_boletos)]
            
            # Generar números ganadores aleatorios para este juego
            numeros_ganadores = self.generar_numeros_ganadores_aleatorios()
            resultados['numeros_ganadores'].append(numeros_ganadores)
            
            # Verificar boletos
            for boleto in boletos:
                aciertos, premio, _ = self.lottery_engine.verificar_boleto(boleto, numeros_ganadores)
                
                resultados['aciertos'][aciertos] += 1
                resultados['premios'][aciertos] += premio
                resultados['total_ganado'] += premio
                
                # Guardar boleto como ganador o perdedor
                if premio > 0:
                    resultados['boletos_ganadores'].append({
                        'juego': juego + 1,
                        'boleto': boleto,
                        'numeros_ganadores': numeros_ganadores,
                        'aciertos': aciertos,
                        'premio': premio
                    })
                else:
                    resultados['boletos_perdedores'].append({
                        'juego': juego + 1,
                        'boleto': boleto,
                        'numeros_ganadores': numeros_ganadores,
                        'aciertos': aciertos
                    })
        
        # Calcular probabilidades
        total_boletos = resultados['total_boletos']
        resultados['probabilidades'] = [
            (resultados['aciertos'][i] / total_boletos) * 100 
            for i in range(7)
        ]
        
        # Formatear resultados para mostrar
        texto_resultados = f"""
RESULTADOS DE LA SIMULACIÓN
---------------------------
Total de juegos: {resultados['total_juegos']:,}
Total de boletos: {resultados['total_boletos']:,}
Total ganado: ${resultados['total_ganado']:,}

ESTADÍSTICAS GENERALES
---------------------
Boletos ganadores: {len(resultados['boletos_ganadores']):,}
Boletos perdedores: {len(resultados['boletos_perdedores']):,}
Porcentaje de ganancia: {(len(resultados['boletos_ganadores']) / total_boletos * 100):.2f}%

DISTRIBUCIÓN DE ACIERTOS
------------------------
0 aciertos: {resultados['aciertos'][0]:,} boletos (${resultados['premios'][0]:,})
1 acierto:  {resultados['aciertos'][1]:,} boletos (${resultados['premios'][1]:,})
2 aciertos: {resultados['aciertos'][2]:,} boletos (${resultados['premios'][2]:,})
3 aciertos: {resultados['aciertos'][3]:,} boletos (${resultados['premios'][3]:,})
4 aciertos: {resultados['aciertos'][4]:,} boletos (${resultados['premios'][4]:,})
5 aciertos: {resultados['aciertos'][5]:,} boletos (${resultados['premios'][5]:,})
6 aciertos: {resultados['aciertos'][6]:,} boletos (${resultados['premios'][6]:,})

PROBABILIDADES
-------------
0 aciertos: {resultados['probabilidades'][0]:.2f}%
1 acierto:  {resultados['probabilidades'][1]:.2f}%
2 aciertos: {resultados['probabilidades'][2]:.2f}%
3 aciertos: {resultados['probabilidades'][3]:.2f}%
4 aciertos: {resultados['probabilidades'][4]:.2f}%
5 aciertos: {resultados['probabilidades'][5]:.2f}%
6 aciertos: {resultados['probabilidades'][6]:.2f}%

BOLETOS GANADORES
----------------
"""
        # Agregar detalles de boletos ganadores
        for boleto in resultados['boletos_ganadores']:
            texto_resultados += f"""
Juego #{boleto['juego']}
Boleto: {' - '.join(map(str, boleto['boleto']))}
Números ganadores: {' - '.join(map(str, boleto['numeros_ganadores']))}
Aciertos: {boleto['aciertos']}
Premio: ${boleto['premio']:,}
"""

        texto_resultados += "\nNÚMEROS GANADORES POR JUEGO\n-------------------------\n"
        for i, numeros in enumerate(resultados['numeros_ganadores'], 1):
            texto_resultados += f"Juego #{i}: {' - '.join(map(str, numeros))}\n"
        
        return texto_resultados 