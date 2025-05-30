import datetime

class Comandos:
    @staticmethod
    def obter_hora():
        return datetime.datetime.now().strftime("%H:%M:%S")
    
    @staticmethod
    def obter_data():
        return datetime.datetime.now().strftime("%d/%m/%Y")
    
    @staticmethod
    def ajuda():
        return """Comandos disponíveis:
        - hora: Mostra a hora atual
        - data: Mostra a data atual
        - sair: Encerra o chatbot
        - ajuda: Mostra esta mensagem"""