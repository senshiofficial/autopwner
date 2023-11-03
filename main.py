from colorama import Fore
import argparse
import intro
import pr1v3sc_sn1p3r as privesc
import p0rt_sn1p3r
import p4g3_sn1p3r
file_esc = None
cve = True
modes = "\n1 - Check for PrivEscs (pr1v3sc_sn1p3r)\n2 - Check open Ports (p0rt_sn1p3r)\n3 - Scrape a Website (r3q_sn1p3r)\n4 - Comming Soon...\n$ "
def main():
    global mode
    intro.intro(args,"\n ▄▄▄       █    ██ ▄▄▄█████▓ ▒█████   ██▓███   █     █░███▄    █ ▓█████  ██▀███  \n▒████▄     ██  ▓██▒▓  ██▒ ▓▒▒██▒  ██▒▓██░  ██▒▓█░ █ ░█░██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒\n▒██  ▀█▄  ▓██  ▒██░▒ ▓██░ ▒░▒██░  ██▒▓██░ ██▓▒▒█░ █ ░█▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒\n░██▄▄▄▄██ ▓▓█  ░██░░ ▓██▓ ░ ▒██   ██░▒██▄█▓▒ ▒░█░ █ ░█▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  \n ▓█   ▓██▒▒▒█████▓   ▒██▒ ░ ░ ████▓▒░▒██▒ ░  ░░░██▒██▓▒██░   ▓██░░▒████▒░██▓ ▒██▒\n ▒▒   ▓▒█░░▒▓▒ ▒ ▒   ▒ ░░   ░ ▒░▒░▒░ ▒▓▒░ ░  ░░ ▓░▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░\n  ▒   ▒▒ ░░░▒░ ░ ░     ░      ░ ▒ ▒░ ░▒ ░       ▒ ░ ░ ░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░\n  ░   ▒    ░░░ ░ ░   ░      ░ ░ ░ ▒  ░░         ░   ░    ░   ░ ░    ░     ░░   ░ \n      ░  ░   ░                  ░ ░               ░            ░    ░  ░   ░     \nmade by Senshi")
    print("\n\nover 200 - sudo PrivEscs\nover 100 - file PrivEscs")
    if mode == 0:
        mode = int(input(modes))
    match int(mode):
        case 1:
            privesc.main(args)

        case 2:
            p0rt_sn1p3r.main(args)

        case 3:
            p4g3_sn1p3r.main(args)
            pass
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
    parser.add_argument("-app", "--app-ports", help="scan for application ports (SMTP, SSH...)", action="store_true", required=False)
    parser.add_argument("-wp", "--web-ports", help="scan for web ports", action="store_true", required=False)
    parser.add_argument("-bp", "--both-ports", help="scan both", action="store_true", required=False)
    parser.add_argument("-alp", "--all-ports", help="scan all ports 1-65555", action="store_true", required=False)
    parser.add_argument("-p", "--port", help="specify ports (standard nmap usage)", required=False)
    parser.add_argument("-nvp", "--no-vpn-prot", help="Use if your VPN doesnt blocks port scanners", action="store_true",required=False)
    parser.add_argument("-vp", "--vpn-prot", help="Use if your VPN blocks port scanners", action="store_true",required=False)
    parser.add_argument("-t", "--target", help="IP of target you want to port scan",required=False)
    parser.add_argument("-c", "--color", help="output color",required=False, type=int)
    parser.add_argument("-st", "--scrape_thread", help="How many Threads for scraping do you wanna use", required=False, type=int)
    args = parser.parse_args()
    
    if args.option:
        try:
            mode = int(args.option)
        except ValueError as e:
            print("option -o/--option has to be an intiger")
            exit(0)
    main()