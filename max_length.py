import msvcrt
from colorama import init, Fore, Style

def input_with_max_length(prompt, max_length):
    print(prompt, end='', flush=True)
    input_str = ''
    while True:
        char = msvcrt.getch()
        if char == b'\r':
            if len(input_str) == max_length:
                print() 
                break
            else:
                print(Fore.RED + "\nDebe ingresar exactamente 16 dígitos." + Style.RESET_ALL)
                print(prompt + input_str, end='', flush=True)
                continue
        elif char == b'\x08':
            if len(input_str) > 0:
                input_str = input_str[:-1]
                print('\b \b', end='', flush=True)
        elif char == b'\x1b':
            print(Fore.RED + "\nOperación cancelada. Saliendo del programa..." + Style.RESET_ALL)
            exit(0)
        elif char.isdigit():
            if len(input_str) < max_length:
                input_str += char.decode()
                print(char.decode(), end='', flush=True)
            else:
                print(Fore.RED + "\nNúmero de cuenta no puede tener más de 16 dígitos." + Style.RESET_ALL)
                print(prompt + input_str, end='', flush=True)
                continue
        else:
            print(Fore.RED + "\nSolo se permiten dígitos." + Style.RESET_ALL)
            print(prompt + input_str, end='', flush=True)
    return input_str
