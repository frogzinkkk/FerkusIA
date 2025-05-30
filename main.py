import sys
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from chatbot.core import ChatBot  # Agora usando import absoluto

def main():
    console = Console()
    bot = ChatBot()
    
    console.print(Panel.fit(
        f"[bold green]🤖 {bot.nome} - Seu Assistente Pessoal[/]",
        subtitle="Digite 'ajuda' para comandos disponíveis",
        border_style="blue"
    ))
    
    while True:
        try:
            user_input = Prompt.ask("[bold cyan]Você[/]")
            response, should_exit = bot.processar_comando(user_input)
            
            if response:
                console.print(Panel.fit(
                    f"[bold yellow]{bot.nome}[/]: {response}",
                    border_style="green"
                ))
            
            if should_exit:
                console.print("[bold red]Encerrando... Até logo![/]")
                sys.exit(0)
                
        except KeyboardInterrupt:
            console.print("[bold red]Encerrando... Até logo![/]")
            sys.exit(0)

if __name__ == "__main__":
    main()