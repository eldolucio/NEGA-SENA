import random
from megasena.stats import MegaSenaStatistics

class MegaSenaGenerator:
    def __init__(self):
        self.statistics = MegaSenaStatistics()
    
    def gerar_numeros(self):
        """Gera 6 números únicos entre 1 e 60 baseado nas estatísticas."""
        numeros = set()
        stats = self.statistics.get_frequencias()
        
        while len(numeros) < 6:
            numero = self._selecionar_numero(stats)
            numeros.add(numero)
        
        return sorted(list(numeros))
    
    def _selecionar_numero(self, frequencias):
        """Seleciona um número baseado nas frequências históricas."""
        numeros = list(range(1, 61))
        pesos = [frequencias.get(num, 1) for num in numeros]
        return random.choices(numeros, weights=pesos, k=1)[0]