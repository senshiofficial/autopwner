# autopwner

autopwner is a tool made for automated hacking. Currently you can only use automated Privilege Escalations (for Linux) but i will add more in further versions
> [!WARNING]
> Dont use the script on your own Host machine since it might destroy your Privilege Separation

> [!NOTE]
> This script is still on a early phase and bugs are expected 

## Upcoming Updates
- [ ] privesc for temp use
- [ ] privesc in sh
- [ ] windows Privilege Escalations

## Download
```
git clone https://github.com/senshiofficial/autopwner.git
cd autopwner
pip install -r requirements.txt
python3 main.py
```

## Usage
```
python3 main.py [OPTION]
  -o, --option          Select option  
  
  Privilege Escalation    (1)
	-s, --su              Select only root Privilege Escalations
	-f, --file            Select only file Privilege Escalations
	-nc, --no-cve         Disable CVE exploiting

  Port Scanner            (2)
	-t, --target          Select a Target IP
	-app, --app-ports     Scan Common Application ports
	-wp, --web-ports      Scan common webapp ports
	-bp, --both-ports     Scan both webapp and Application ports
	-p, --port            Scan specified port (1-10,11,12.....)
	-alp, --all-ports     Scan all ports (1-65555)
	-nvp, --no-vpn-prot   Choose if your VPN doesnt block Port scanners
	-vp, --vpn-prot       Choose if your VPN does block Port scanners

  Web Spider             (3)
	-t, --target          Select a Target IP
	-sn, --spider-name    Change the Spiders Name

  General
	-c, --color           Choose output color (ANSI)
```

## Web
```
cd web/
python3 web.py
```
or
```
sudo cp web/ /srv/http # Arch
sudo cp web/ /var/www/html # Debian
```
## Versions
- #### 1.4.2
	- [+] Web support (Beta)
	- [+] autoremove duplicate urls 
	- [+] updated no-args version
- #### 1.3.2
	- [+] using Scrapy for p4g3_sn1p3r
	- [+]  new arguments
- #### 1.3.1 Alpha
	- [+] Scrape Websites (Beta)
	- [+] -c, --color to change intro's color (ANSI)
	- [+] Colorama no more needed 
- #### 1.2 Alpha
	- [+] Port scanner (Beta)
	- [+] better argument handling
- #### 1.1 - Alpha
	- [+] Windows Privilege Escalations (1 sample)
	- [+] OS Detection
	- [+] Uknown OS Detection 
	- [+] Linux CVE Privilege Escalations (3 samples)
	- [+] --no-cve arg 
- #### 1.0 - Beta
	- [+] Linux Privilege Escalations (over 300 samples)

## Tested
- #### Kali Linux Roling 2023.3
	- [+] everythings working fine
- #### Arch Linux x86_64
	- [-] p0rt_sn1p3r doesnt work due `nmap.nmap.PortScannerError`
	- [+] anything other works fine
- #### Mint
	- [+] everythings working fine