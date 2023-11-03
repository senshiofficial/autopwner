from colorama import Fore
import time
import privesc
import nmap_scanner
import p4g3_sn1p3r

def intro(text, delay=0.003):
    print(Fore.RED, end='')
    for char in text:
        print(char, end='')
        time.sleep(delay)
    print(Fore.RESET, end="")

def main():
    intro(""" \n ██▓███   ██▀███   ██▓ ██▒   █▓▓█████   ██████  ▄████▄       ██████  ███▄    █  ██▓ ██▓███  ▓█████  ██▀███  \n▓██░  ██▒▓██ ▒ ██▒▓██▒▓██░   █▒▓█   ▀ ▒██    ▒ ▒██▀ ▀█     ▒██    ▒  ██ ▀█   █ ▓██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒\n▓██░ ██▓▒▓██ ░▄█ ▒▒██▒ ▓██  █▒░▒███   ░ ▓██▄   ▒▓█    ▄    ░ ▓██▄   ▓██  ▀█ ██▒▒██▒▓██░ ██▓▒▒███   ▓██ ░▄█ ▒\n▒██▄█▓▒ ▒▒██▀▀█▄  ░██░  ▒██ █░░▒▓█  ▄   ▒   ██▒▒▓▓▄ ▄██▒     ▒   ██▒▓██▒  ▐▌██▒░██░▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  \n▒██▒ ░  ░░██▓ ▒██▒░██░   ▒▀█░  ░▒████▒▒██████▒▒▒ ▓███▀ ░   ▒██████▒▒▒██░   ▓██░░██░▒██▒ ░  ░░▒████▒░██▓ ▒██▒\n▒▓▒░ ░  ░░ ▒▓ ░▒▓░░▓     ░ ▐░  ░░ ▒░ ░▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░   ▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒ ░▓  ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░\n░▒ ░       ░▒ ░ ▒░ ▒ ░   ░ ░░   ░ ░  ░░ ░▒  ░ ░  ░  ▒      ░ ░▒  ░ ░░ ░░   ░ ▒░ ▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░\n░░         ░░   ░  ▒ ░     ░░     ░   ░  ░  ░  ░           ░  ░  ░     ░   ░ ░  ▒ ░░░          ░     ░░   ░ \n            ░      ░        ░     ░  ░      ░  ░ ░               ░           ░  ░              ░  ░   ░     \n                           ░                   ░                                                            \nmade by Akuma""")
    print("\nover 200 - sudo PrivEscs\nover 100 - file PrivEscs")
    mode = int(input("\n1 - Check for open ports\n2 - Check for any SQLi able pages\n3 - check for Privilage escalations\n4 - Comming Soon....\n$ "))
    if mode == 1:
        nmap_scanner.nmapScanWeb()
    elif mode == 2:
        privesc.main()
    elif mode == 3:
        p4g3_sn1p3r.main()
    elif mode == 4:
        print("Comming Soon...")
        print("Its an Automated E-")

if __name__ == "__main__":
    main()
