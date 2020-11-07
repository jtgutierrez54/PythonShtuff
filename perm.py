
#Gather Text and Key from user
#establish a couple lists for the data
#setup loop to parse the data
#rearrange the indicies to match the key
#print out the ciphertext

ptext = input('Enter your text: ').upper()
key = input('Enter your key: ')

klist = []
tlist = []
str1 = ''

if len(ptext) == len(key):
    for l in ptext:
        tlist.append(l)
        
    for n in key:
        klist.append(int(n))
        
    tlist = [tlist[i] for i in klist]
    
    print(str1.join(tlist))
    
else:
    print('HEY! you are wrong!')
    
