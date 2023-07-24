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
        countdown_string += 'z' * countdown_sec + 'zege' + ' ' * i
    return countdown_string


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        seconds = sys.argv[1]
    else:
        seconds = ('Seconds > ')
    
    try:
        run_zege_countdown(int(seconds))
    except ValueError as e:
        print('Requires a positive integer.')
