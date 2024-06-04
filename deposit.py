from colorama import Fore, Style

def deposit(balance, amount):
    if amount > 0:
        balance += amount
        print(Fore.GREEN + f"Has depositado ${amount}. Tu nuevo saldo es: ${balance}" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Monto de depósito inválido." + Style.RESET_ALL)
    return balance
