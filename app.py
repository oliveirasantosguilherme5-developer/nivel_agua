def exibir_nivel(nivel):
    from colorama import Fore, Style
    
    niveis = [
        Fore.RED + "Nível 1: Muito Baixo",
        Fore.YELLOW + "Nível 2: Baixo",
        Fore.GREEN + "Nível 3: Médio",
        Fore.CYAN + "Nível 4: Alto",
        Fore.BLUE + "Nível 5: Muito Alto (alerta)"]
    
    if nivel == 1:
        print(niveis[0] + Style.RESET_ALL)
    elif nivel == 2:
        print(niveis[1] + Style.RESET_ALL)
    elif nivel == 3:
        print(niveis[2] + Style.RESET_ALL)
    elif nivel == 4:
        print(niveis[3] + Style.RESET_ALL)
    elif nivel == 5:
        print(niveis[4] + Style.RESET_ALL)
    else:
        print("Nível inválido. Por favor, insira um nível entre 1 e 5.")

exibir_nivel(1)
