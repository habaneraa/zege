"""ZEGE countdown"""
import time
from colorama import Fore


colors = [
    # Fore.BLACK          ,
    Fore.RED            ,
    Fore.GREEN          ,
    Fore.YELLOW         ,
    Fore.BLUE           ,
    Fore.MAGENTA        ,
    Fore.CYAN           ,
    Fore.WHITE          ,
    # Fore.RESET          ,
    Fore.LIGHTBLACK_EX  ,
    Fore.LIGHTRED_EX    ,
    Fore.LIGHTGREEN_EX  ,
    Fore.LIGHTYELLOW_EX ,
    Fore.LIGHTBLUE_EX   ,
    Fore.LIGHTMAGENTA_EX,
    Fore.LIGHTCYAN_EX   ,
    Fore.LIGHTWHITE_EX  ,
]


def run_zege_countdown(secs: int) -> str:
    countdown_string = ''
    for i in range(secs + 1):
        countdown_sec = secs - i
        time.sleep(1.0)
        countdown_string += '\r' + 'z' * countdown_sec + 'zege' + ' ' * i

    try:
        while True:
            for color in colors:
                countdown_string += color + 'ZEGE! ' * 10
    except KeyboardInterrupt:
        countdown_string += Fore.RESET + 'zzzzzzzzzzzzz zzzzzz zzzz zzz  zz   z    z...'
        return countdown_string
