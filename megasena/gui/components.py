"""
Componentes reutilizáveis da interface
"""
import customtkinter as ctk
from .styles import COLORS, PADDING, FONTS

class NumberDisplay(ctk.CTkTextbox):
    def __init__(self, master, **kwargs):
        super().__init__(
            master,
            height=150,
            width=400,
            font=FONTS['normal'],
            border_width=2,
            border_color=COLORS['secondary'],
            **kwargs
        )
        self.configure(state='disabled')
    
    def update_text(self, text):
        self.configure(state='normal')
        self.delete('1.0', 'end')
        self.insert('1.0', text)
        self.configure(state='disabled')

class StatsDisplay(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.title = ctk.CTkLabel(
            self,
            text="Estatísticas",
            font=FONTS['subheading']
        )
        self.title.pack(pady=PADDING['small'])
        
        self.stats_text = ctk.CTkTextbox(
            self,
            height=200,
            width=400,
            font=FONTS['normal']
        )
        self.stats_text.pack(padx=PADDING['medium'], pady=PADDING['small'])
        self.stats_text.configure(state='disabled')
    
    def update_stats(self, stats):
        self.stats_text.configure(state='normal')
        self.stats_text.delete('1.0', 'end')
        
        self.stats_text.insert('end', "🔥 Números mais sorteados:\n\n")
        for num, freq in stats['mais_sorteados']:
            self.stats_text.insert('end', f"Número {num:02d}: {freq:3d} vezes\n")
        
        self.stats_text.insert('end', "\n📉 Números menos sorteados:\n\n")
        for num, freq in stats['menos_sorteados']:
            self.stats_text.insert('end', f"Número {num:02d}: {freq:3d} vezes\n")
        
        self.stats_text.configure(state='disabled')