from datetime import datetime
from config import settings  # Import absoluto
from chatbot.comandos import Comandos  # Import absoluto

class ChatBot:
    def __init__(self):
        self.nome = settings.NOME_ASSISTENTE
        self.historico = []
        self.comandos = settings.COMANDOS
        
    def processar_comando(self, entrada):
        entrada = entrada.lower().strip()
        self.historico.append(entrada)
        
        if entrada in self.comandos["SAIR"]:
            return "", True
            
        if entrada in self.comandos["AJUDA"]:
            return Comandos.ajuda(), False
            
        if entrada in self.comandos["HORA"]:
            return f"🕒 São {Comandos.obter_hora()}", False
            
        if entrada in self.comandos["DATA"]:
            return f"📅 Hoje é {Comandos.obter_data()}", False
            
        return f"❌ Comando não reconhecido: '{entrada}'", False