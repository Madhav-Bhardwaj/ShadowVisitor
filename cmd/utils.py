import os
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from rich.console import Console

console = Console()

def get_amount():

    os.system("clear")
    console.print("[bold red] Ultimate Automated Website Traffic Booster [/bold red]\n", justify="center")
    
    console.print("[bold red]███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗    ██╗   ██╗██╗███████╗██╗████████╗ ██████╗ ██████╗[/bold red]", justify="center")
    console.print("[bold red]██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║    ██║   ██║██║██╔════╝██║╚══██╔══╝██╔═══██╗██╔══██╗[/bold red]", justify="center")
    console.print("[bold red]███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║    ██║   ██║██║███████╗██║   ██║   ██║   ██║██████╔╝[/bold red]", justify="center")
    console.print("[bold red]╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║    ╚██╗ ██╔╝██║╚════██║██║   ██║   ██║   ██║██╔══██╗[/bold red]", justify="center")
    console.print("[bold red]███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝     ╚████╔╝ ██║███████║██║   ██║   ╚██████╔╝██║  ██║[/bold red]", justify="center")
    console.print("[bold red]╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝       ╚═══╝  ╚═╝╚══════╝╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝[/bold red]\n", justify="center")
                                                                                                    
    console.print("[bold cyan] Coded By: Madhav Bhardwaj [/bold cyan]", justify="center")


    try:
        amount = int(console.input("[bold yellow][#]Enter The Number of Visits: [/bold yellow]"))
    except ValueError:
        print("\n\nERROR 0x02: Please enter a valid number\n\n")
        exit()
    return amount

def change_ip():
    os.system("windscribe disconnect")
    time.sleep(2)
    server_list = ["US", "CA", "DE", "FR", "NL", "GB", "HK", "SG"]
    random_server = random.choice(server_list)
    os.system(f"windscribe connect {random_server}")
    time.sleep(5)

def open_browser(url):
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    try:
        driver.get(url)
        print(f"Visited {url}")
        time.sleep(10)
    except Exception as e:
        print(f"Error visiting {url}: {e}")
    driver.quit()