from utils import *
from rich.console import Console
import os

console = Console()


def start():
	os.system("clear")
	console.print("[bold red] Ultimate Automated Website Traffic Booster [/bold red]\n", justify="center")
	
	console.print("[bold red]███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗    ██╗   ██╗██╗███████╗██╗████████╗ ██████╗ ██████╗[/bold red]", justify="center")
	console.print("[bold red]██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║    ██║   ██║██║██╔════╝██║╚══██╔══╝██╔═══██╗██╔══██╗[/bold red]", justify="center")
	console.print("[bold red]███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║    ██║   ██║██║███████╗██║   ██║   ██║   ██║██████╔╝[/bold red]", justify="center")
	console.print("[bold red]╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║    ╚██╗ ██╔╝██║╚════██║██║   ██║   ██║   ██║██╔══██╗[/bold red]", justify="center")
	console.print("[bold red]███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝     ╚████╔╝ ██║███████║██║   ██║   ╚██████╔╝██║  ██║[/bold red]", justify="center")
	console.print("[bold red]╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝       ╚═══╝  ╚═╝╚══════╝╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝[/bold red]\n", justify="center")
	                                                                                                
	console.print("[bold cyan] Coded By: Madhav Bhardwaj [/bold cyan]", justify="center")


if __name__ == "__main__":
    start()
    website_url = console.input("[bold yellow]Enter The Website URL To Visit:[/bold yellow] ")
    visit_count = get_amount()
    use_vpn = console.input("[bold yellow]Use VPN? (yes/no):[/bold yellow] ").strip().lower() == "yes"
    
    for _ in range(visit_count):
        if use_vpn:
            change_ip()
        try:
            open_browser(website_url)
        except Exception as e:
            print(f"Error visiting {website_url}: {e}")
        time.sleep(random.choice([1, 2, 3, 4]))
