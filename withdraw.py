from colorama import Fore, Style

def withdraw(balance, amount):
    if 0 < amount <= balance:
        balance -= amount
        print(Fore.BLUE + f"Has retirado ${amount}. Tu nuevo saldo es: ${balance}" + Style.RESET_ALL)
    else:
        print(Fore.RED + "Monto de retiro inválido o fondos insuficientes." + Style.RESET_ALL)
    return balance
