import random
from collections import defaultdict

class MegaSenaStatistics:
    def __init__(self):
        self.frequencias = self._carregar_frequencias()
    
    def _carregar_frequencias(self):
        """
        Simula dados de frequência dos últimos 100 sorteios.
        Em um ambiente real, estes dados viriam de uma API ou banco de dados.
        """
        frequencias = defaultdict(int)
        # Simula 100 sorteios
        for _ in range(100):
            numeros = random.sample(range(1, 61), 6)
            for num in numeros:
                frequencias[num] += 1
        return dict(frequencias)
    
    def get_frequencias(self):
        """Retorna o dicionário de frequências."""
        return self.frequencias
    
    def get_estatisticas(self):
        """Retorna as estatísticas dos números mais e menos sorteados."""
        freq_ordenada = sorted(self.frequencias.items(), key=lambda x: x[1], reverse=True)
        
        return {
            'mais_sorteados': freq_ordenada[:10],
            'menos_sorteados': freq_ordenada[-10:]
        }