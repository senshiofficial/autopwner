import time
def intro(args, text, delay=0.003):
    color = 35
    if args != None and args.color:
        color=args.color
    for char in text:
        print(f"\033[{color}m{char}\033[0m", end='')
        time.sleep(delay)