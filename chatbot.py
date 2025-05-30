from .chatbot.comandos import Comandos
from .config import settings
import re

class ChatBot:
    def __init__(self):
        self.nome = settings.CONFIG["nome"]
        self.historico = []
        self.comandos = settings.CONFIG["comandos"]
    
    def processar_comando(self, entrada):
        entrada = entrada.lower().strip()
        
        # Verifica comandos de saída
        if entrada in self.comandos["sair"]:
            return None, True  # None indica para não responder, True para sair
        
        # Verifica comando de ajuda
        if entrada in self.comandos["ajuda"]:
            return Comandos.ajuda(), False
        
        # Verifica comando de hora
        if entrada in self.comandos["hora"]:
            return f"Agora são {Comandos.obter_hora()}", False
        
        # Verifica comando de data
        if entrada in self.comandos["data"]:
            return f"Hoje é {Comandos.obter_data()}", False
        
        # Padrão não reconhecido
        return f"Desculpe, não entendi '{entrada}'. Digite 'ajuda' para ver os comandos.", False