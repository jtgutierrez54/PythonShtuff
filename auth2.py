#import modules
import hmac
import sys

#open key and message files
keyFile = open("master.key")
dataFile = open("tags.txt")

def genTag(msg, key): #hmac hash function
    hm = hmac.new(key.encode())
    hm.update(msg.encode())
    return hm.hexdigest()
    
hmacs = {}
line = dataFile.readline()
masterKey = keyFile.read()

while line: #fills empty hmacs dictionary 
    (thisKey,thisValue) = line.split(":")
    hmacs[thisKey] = thisValue.rstrip()
    line = dataFile.readline()
    
msgs = []

for m in hmacs.keys(): #fills msgs list with the messages 
    msgs.append(m)
    
authent = []

for k in msgs: #fills top list with the hashes made from the function and messages
    authent.append(genTag(k, masterKey))
    
wrongHmacs = []
correct = []

for i in authent: #loop to send the correct hmacs to the correct list and vise versa
    if i in hmacs.values():
        correct.append(i)
    else:
        wrongHmacs.append(i) 

flip = dict(zip(authent, msgs)) #flipped dictionary that uses the hash as the key
                                #and message as the value
for x in wrongHmacs: #takes items from the wrong list and compares it with keys 
    if x in flip:    #from the flipped list and prints them out together.      
        print(x, flip[x])








