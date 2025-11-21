from colorama import Fore, Style, init
init(autoreset=True)

def print_info(msg):
    print(Fore.CYAN + msg + Style.RESET_ALL)

def print_success(msg):
    print(Fore.GREEN + msg + Style.RESET_ALL)

def print_error(msg):
    print(Fore.RED + msg + Style.RESET_ALL)

def print_warning(msg):
    print(Fore.YELLOW + msg + Style.RESET_ALL)

