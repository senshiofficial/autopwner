from colorama import Fore
import time
import argparse
import pr1v3sc_sn1p3r as privesc
#import ???     Will be comming soon...
#import ???     Will be comming soon...
file_esc = None
cve = True
def intro(text, delay=0.003):
    print(Fore.RED, end='')
    for char in text:
        print(char, end='')
        time.sleep(delay)
    print(Fore.RESET, end="")
modes = "\n1 - Check for PrivEscs (pr1v3sc_sn1p3r)\n2 - Comming Soon...\n3 - Comming Soon...\n4 - Comming Soon...\n$ "
def main():
    global mode
    intro(""" ▄▄▄       █    ██ ▄▄▄█████▓ ▒█████   ██▓███   █     █░███▄    █ ▓█████  ██▀███  
▒████▄     ██  ▓██▒▓  ██▒ ▓▒▒██▒  ██▒▓██░  ██▒▓█░ █ ░█░██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
▒██  ▀█▄  ▓██  ▒██░▒ ▓██░ ▒░▒██░  ██▒▓██░ ██▓▒▒█░ █ ░█▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
░██▄▄▄▄██ ▓▓█  ░██░░ ▓██▓ ░ ▒██   ██░▒██▄█▓▒ ▒░█░ █ ░█▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
 ▓█   ▓██▒▒▒█████▓   ▒██▒ ░ ░ ████▓▒░▒██▒ ░  ░░░██▒██▓▒██░   ▓██░░▒████▒░██▓ ▒██▒
 ▒▒   ▓▒█░░▒▓▒ ▒ ▒   ▒ ░░   ░ ▒░▒░▒░ ▒▓▒░ ░  ░░ ▓░▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
  ▒   ▒▒ ░░░▒░ ░ ░     ░      ░ ▒ ▒░ ░▒ ░       ▒ ░ ░ ░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
  ░   ▒    ░░░ ░ ░   ░      ░ ░ ░ ▒  ░░         ░   ░    ░   ░ ░    ░     ░░   ░ 
      ░  ░   ░                  ░ ░               ░            ░    ░  ░   ░     
                                                                                 \nmade by Senshi""")
    print("\n\nover 200 - sudo PrivEscs\nover 100 - file PrivEscs")
    if mode == 0:
        mode = int(input(modes))
    match int(mode):
        case 1:
            privesc.main(file_esc, cve)

        case 2:
            print("Comming Soon...")
            print("Its an Automated nma-")
        case 3:
            print("Comming Soon...")
            print("Its an Automated SQL-")
        case 4:
            print("Comming Soon...")
            print("Its an Automated web-")
        case _:
            print("no such option")
if __name__ == "__main__":
    mode = 0
    parser = argparse.ArgumentParser(description="Automated pwner tool")
    parser.add_argument("-o", "--option", help="option", required=False)
    parser.add_argument("-s", "--su", help="su Privilege Escalation", action="store_true", required=False)
    parser.add_argument("-f", "--file", help="file Privilege Escalation", action="store_true", required=False)
    parser.add_argument("-nc", "--no-cve", help="dont use CVEs for Privescs", action="store_true", required=False)
    args = parser.parse_args()
    if args.option:
        try:
            mode = int(args.option)
        except ValueError as e:
            print("option -o/--option has to be an intiger")
    if args.su:
        file_esc = False
    if args.file:
        file_esc = True
    if args.no_cve:
        cve = False
    main()