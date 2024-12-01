"""
Janela principal da aplicação
"""
import customtkinter as ctk
from .components import NumberDisplay, StatsDisplay
from .styles import COLORS, PADDING, FONTS
from ..generator import MegaSenaGenerator
from ..stats import MegaSenaStatistics

class MainWindow(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.generator = MegaSenaGenerator()
        self.statistics = MegaSenaStatistics()
        
        self._setup_window()
        self._create_widgets()
        self._update_statistics()
    
    def _setup_window(self):
        self.title("Gerador Mega-Sena")
        self.geometry("800x900")
        self.configure(fg_color=COLORS['background'])
        
        # Configura o tema do CustomTkinter
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
    
    def _create_widgets(self):
        # Título
        title = ctk.CTkLabel(
            self,
            text="Gerador Mega-Sena",
            font=FONTS['heading']
        )
        title.pack(pady=PADDING['large'])
        
        # Frame para controles
        controls_frame = ctk.CTkFrame(self)
        controls_frame.pack(pady=PADDING['medium'])
        
        # Label e Spinbox para quantidade de jogos
        qtd_label = ctk.CTkLabel(
            controls_frame,
            text="Quantidade de jogos:",
            font=FONTS['normal']
        )
        qtd_label.pack(side='left', padx=PADDING['medium'])
        
        self.qtd_jogos = ctk.CTkOptionMenu(
            controls_frame,
            values=[str(i) for i in range(1, 11)],
            font=FONTS['normal']
        )
        self.qtd_jogos.pack(side='left', padx=PADDING['medium'])
        
        # Botão gerar
        self.btn_gerar = ctk.CTkButton(
            self,
            text="Gerar Números",
            font=FONTS['normal'],
            command=self._gerar_numeros
        )
        self.btn_gerar.pack(pady=PADDING['medium'])
        
        # Display de números
        self.number_display = NumberDisplay(self)
        self.number_display.pack(pady=PADDING['medium'])
        
        # Display de estatísticas
        self.stats_display = StatsDisplay(self)
        self.stats_display.pack(pady=PADDING['medium'])
    
    def _gerar_numeros(self):
        try:
            qtd = int(self.qtd_jogos.get())
            jogos = []
            
            for i in range(qtd):
                numeros = self.generator.gerar_numeros()
                jogos.append(f"Jogo {i+1}: {' - '.join(f'{n:02d}' for n in numeros)}")
            
            self.number_display.update_text('\n'.join(jogos))
            
        except Exception as e:
            self.number_display.update_text(f"Erro ao gerar números: {str(e)}")
    
    def _update_statistics(self):
        stats = self.statistics.get_estatisticas()
        self.stats_display.update_stats(stats)