import tkinter as tk
from tkinter import ttk
from generator import MegaSenaGenerator
from statistics import MegaSenaStatistics

class MegaSenaGUI:
    def __init__(self, root):
        self.root = root
        self.generator = MegaSenaGenerator()
        self.statistics = MegaSenaStatistics()
        
        self.root.geometry("600x800")
        self.root.configure(padx=20, pady=20)
        
        self._setup_ui()
    
    def _setup_ui(self):
        # Número de jogos
        frame_jogos = ttk.Frame(self.root)
        frame_jogos.pack(fill='x', pady=10)
        
        ttk.Label(frame_jogos, text="Quantidade de jogos:").pack(side='left')
        self.num_jogos = ttk.Spinbox(frame_jogos, from_=1, to=10, width=5)
        self.num_jogos.set(1)
        self.num_jogos.pack(side='left', padx=10)
        
        # Botão gerar
        ttk.Button(self.root, text="Gerar Números", command=self._gerar_numeros).pack(pady=10)
        
        # Área para números gerados
        frame_numeros = ttk.LabelFrame(self.root, text="Números Gerados")
        frame_numeros.pack(fill='x', pady=10)
        self.numeros_text = tk.Text(frame_numeros, height=10, width=50)
        self.numeros_text.pack(padx=10, pady=10)
        
        # Área para estatísticas
        frame_stats = ttk.LabelFrame(self.root, text="Estatísticas")
        frame_stats.pack(fill='x', pady=10)
        self.stats_text = tk.Text(frame_stats, height=15, width=50)
        self.stats_text.pack(padx=10, pady=10)
        
        self._atualizar_estatisticas()
    
    def _gerar_numeros(self):
        self.numeros_text.delete(1.0, tk.END)
        qtd_jogos = int(self.num_jogos.get())
        
        for i in range(qtd_jogos):
            numeros = self.generator.gerar_numeros()
            numeros_formatados = ' - '.join(map(str, sorted(numeros)))
            self.numeros_text.insert(tk.END, f"Jogo {i+1}: {numeros_formatados}\n")
    
    def _atualizar_estatisticas(self):
        self.stats_text.delete(1.0, tk.END)
        stats = self.statistics.get_estatisticas()
        
        self.stats_text.insert(tk.END, "Números mais sorteados:\n")
        for num, freq in stats['mais_sorteados']:
            self.stats_text.insert(tk.END, f"Número {num}: {freq} vezes\n")
        
        self.stats_text.insert(tk.END, "\nNúmeros menos sorteados:\n")
        for num, freq in stats['menos_sorteados']:
            self.stats_text.insert(tk.END, f"Número {num}: {freq} vezes\n")