"""
Motor principal de la lotería que maneja la lógica del juego
"""
import random
from typing import List, Dict, Tuple

class LotteryEngine:
    def __init__(self):
        pass

    def comparar_numeros(self, boleto_usuario: List[int], numeros_ganadores: List[int]) -> Tuple[int, List[int]]:
        if len(boleto_usuario) != len(numeros_ganadores):
            return 0, []
            
        aciertos = 0
        posiciones_acertadas = []
        
        for i, (boleto, ganador) in enumerate(zip(boleto_usuario, numeros_ganadores)):
            if boleto == ganador:
                aciertos += 1
                posiciones_acertadas.append(i)
        
        return aciertos, posiciones_acertadas

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

    def verificar_boleto(self, numeros: List[int], numeros_ganadores: List[int]) -> Tuple[int, int, List[int]]:
        aciertos, posiciones = self.comparar_numeros(numeros, numeros_ganadores)
        premio = self.calcular_premio(aciertos)
        return aciertos, premio, posiciones

    def verificar_boletos(self, boletos: List[List[int]], numeros_ganadores: List[int]) -> List[Dict]:
        resultados = []
        for i, boleto in enumerate(boletos, 1):
            aciertos, premio, posiciones = self.verificar_boleto(boleto, numeros_ganadores)
            resultados.append({
                'boleto': i,
                'numeros': boleto,
                'aciertos': aciertos,
                'premio': premio,
                'posiciones_acertadas': posiciones
            })
        return resultados 