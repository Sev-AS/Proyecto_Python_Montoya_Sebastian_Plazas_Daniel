"""
Manejador del historial de sorteos de la lotería
"""
import datetime
import json
from typing import List, Dict, Any
from pathlib import Path

class HistoryManager:
    def __init__(self):
        """Inicializa el manejador de historial"""
        self.historial = []
        self.base_path = Path(__file__).parent.parent.parent
        self.archivo_historial = self.base_path / "data" / "historial.json"
        self.cargar_historial()

    def cargar_historial(self) -> None:
        """Carga el historial desde el archivo JSON"""
        try:
            if self.archivo_historial.exists():
                with open(self.archivo_historial, 'r', encoding='utf-8') as f:
                    self.historial = json.load(f)
            else:
                self.historial = []
                self.guardar_historial()
        except Exception:
            self.historial = []

    def guardar_historial(self) -> None:
        """Guarda el historial en el archivo JSON"""
        try:
            # Asegurar que el directorio existe
            self.archivo_historial.parent.mkdir(parents=True, exist_ok=True)
            
            with open(self.archivo_historial, 'w', encoding='utf-8') as f:
                json.dump(self.historial, f, ensure_ascii=False, indent=2)
        except Exception:
            pass

    def agregar_sorteo(self, boletos: List[List[int]], numeros_ganadores: List[int], total_ganado: int) -> None:
        """
        Agrega un nuevo sorteo al historial
        
        Args:
            boletos: Lista de boletos jugados
            numeros_ganadores: Números ganadores del sorteo
            total_ganado: Monto total ganado
        """
        try:
            sorteo = {
                'fecha': datetime.datetime.now().strftime("%d/%m/%Y %H:%M"),
                'boletos': boletos,
                'numeros_ganadores': numeros_ganadores,
                'total_ganado': total_ganado
            }
            
            self.historial.append(sorteo)
            self.guardar_historial()
        except Exception:
            pass

    def obtener_estadisticas(self) -> Dict[str, Any]:
        """
        Calcula estadísticas del historial
        
        Returns:
            Dict con estadísticas calculadas
        """
        try:
            total_sorteos = len(self.historial)
            total_boletos = sum(len(s['boletos']) for s in self.historial)
            total_ganado = sum(s['total_ganado'] for s in self.historial)
            
            return {
                'total_sorteos': total_sorteos,
                'total_boletos': total_boletos,
                'total_ganado': total_ganado,
                'promedio_boletos': total_boletos / total_sorteos if total_sorteos > 0 else 0,
                'promedio_ganancia': total_ganado / total_sorteos if total_sorteos > 0 else 0
            }
        except Exception:
            return {
                'total_sorteos': 0,
                'total_boletos': 0,
                'total_ganado': 0,
                'promedio_boletos': 0,
                'promedio_ganancia': 0
            }

    def obtener_ultimos_sorteos(self, cantidad: int = 5) -> List[Dict]:
        """
        Obtiene los últimos sorteos del historial
        
        Args:
            cantidad: Número de sorteos a obtener
            
        Returns:
            Lista de los últimos sorteos
        """
        try:
            return self.historial[-cantidad:]
        except Exception:
            return []

    def limpiar_historial(self) -> None:
        """Limpia todo el historial"""
        try:
            self.historial = []
            self.guardar_historial()
        except Exception:
            pass 