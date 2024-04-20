import warnings
from colorama import Fore, Style

warnings.filterwarnings("ignore")

module_description = "Arsen: Find profiles in popular websites"
__version__ = "1.0.0"




def info():
    print(
        '     ___      .______          _______. _______ .__   __. \n' +
        '    /   \     |   _  \        /       ||   ____||  \ |  | \n' +
        '   /  ^  \    |  |_)  |      |   (----`|  |__   |   \|  | \n' +
        '  /  /_\  \   |      /        \   \    |   __|  |  . `  | \n' +
        ' /  _____  \  |  |\  \----.----)   |   |  |____ |  |\   | \n' +
        '/__/     \__\ | _| `._____|_______/    |_______||__| \__| \n'

    )
    print(f"Arsen {__version__}\n{module_description}")
    print(f"{Fore.CYAN}{Fore.YELLOW}Warning : Removed websites has their own protection(scripts to avoid cyber threads){Fore.YELLOW}{Fore.RESET}")
