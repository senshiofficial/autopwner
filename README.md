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
python3 main.py (-o/--option int, -s/--su, -f/--file)
option = choose mode directly without input
su, file = choose between root (su) and File Privescs (only with -o/--option)
```
