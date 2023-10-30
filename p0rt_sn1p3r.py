import nmap
import time
import json
import argparse
import intro
target = "127.0.0.1"
web_ports = [80, 8888, 8000, 8080, 443]
app_ports = [20, 21, 22, 25, 53, 587, 3306, 3389]
ports = []
open_ports = []

def argPort(ports):
    return_ports = []
    port_lenght = ports.split(",")
    for port in range(len(port_lenght)):
        try:
            if "-" in str(port_lenght[port]):
                port_range_lenght = port_lenght[port].split("-")
                port_range = abs(int(port_range_lenght[0]) - int(port_range_lenght[1]))
                port_range_lenght[0] = int(port_range_lenght[0])
                return_ports.append(port_range_lenght[0])
                for num in range(int(port_range)):
                    port_range_lenght[0] += 1
                    return_ports.append(port_range_lenght[0])
            else:
                return_ports.append(int(port_lenght[port]))
        except ValueError as e:
            print("port {} must be an intiger. Skipping...".format(port_lenght[port]))
    return list(set(return_ports))

def main(args):
    global ports, target
    intro.intro("\n ██▓███   ▒█████   ██▀███  ▄▄▄█████▓     ██████  ███▄    █  ██▓ ██▓███  ▓█████  ██▀███  \n▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒   ▒██    ▒  ██ ▀█   █ ▓██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒\n▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░   ░ ▓██▄   ▓██  ▀█ ██▒▒██▒▓██░ ██▓▒▒███   ▓██ ░▄█ ▒\n▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░      ▒   ██▒▓██▒  ▐▌██▒░██░▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  \n▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░    ▒██████▒▒▒██░   ▓██░░██░▒██▒ ░  ░░▒████▒░██▓ ▒██▒\n▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░      ▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒ ░▓  ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░\n░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░       ░ ░▒  ░ ░░ ░░   ░ ▒░ ▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░\n░░       ░ ░ ░ ▒    ░░   ░   ░         ░  ░  ░     ░   ░ ░  ▒ ░░░          ░     ░░   ░ \n             ░ ░     ░                       ░           ░  ░              ░  ░   ░     ")
    if args.target:
        target = args.target
    if args.port:
        ports = argPort(args.port)
    elif args.app_ports:
        ports = app_ports
    elif args.web_ports:
        ports = web_ports
    elif args.both_ports:
        ports = web_ports + app_ports
    else:
        ports = web_ports
    nm = nmap.PortScanner()
    timeout = 3
    if args.no_vpn_prot:
        vpn_protected = False
    elif args.vpn_prot:
        vpn_protected = True
    else:
        vpn_protected = isVpnProt()
    if vpn_protected:
        print("Prot")
        for port in ports: # This is for the timeout
            raw_scan_result = nm.scan(target, arguments=f'-p {port} -sV')
            if raw_scan_result["nmap"]["scanstats"]["downhosts"] == "1":
                print("{} is down or doesnt exist".format(target))
                return 1
            scan_result[target]["tcp"][port] = raw_scan_result['scan'][target]['tcp'][port]
            time.sleep(timeout)
    else:
        full_port = ','.join([str(port) for port in ports])
        scan_result = nm.scan(target, arguments=f'-p {full_port} --min-rate 1000 -sV')
    print("\nPORT      NAME    SERVICE\n")
    for port in ports:
            try:
                if scan_result['scan'][target]['tcp'][port]['state'] == "closed":
                    print("{} is closed".format(port))
                else:
                    product = scan_result['scan'][target]['tcp'][port]['product']
                    version = scan_result['scan'][target]['tcp'][port]['version']
                    name    = scan_result['scan'][target]['tcp'][port]['name']
                    if version == "":
                        version = "Not Found"
                    port = str(port)
                    if len(port) < 6:
                        port += " "*(6-len(port))
                    print("{}    {}    {} ({})".format(port, name, product, version))
                    open_ports.append(port)
            except Exception as e:
                print(e)
    if open_ports:
        return True
    return False

def isVpnProt():
    print("\nport scanning protection is a mechanism wich stop the user from scanning ports. (for example ProtonVPN)\nif you have one the you should use any port scanners with a timeout or you get false results")
    while True:
        vpn = input("Enter 'y' for Yes, 'n' for No, or '?' for Help\n$ ")
        
        if vpn in ['y', 'n', '?']:
            if vpn == 'y':
                return True
            elif vpn == 'n':
                return False
            elif vpn == '?':
                print("port scanning protection is a mechanism wich stop the user from scanning ports. (for example ProtonVPN)\nif you have one the you should use any port scanners with a timeout or you get false results")
        else:
            print("Invalid input. Please enter 'y', 'n', or '?'")
#nmapScanWeb()