import sys
import os
import platform
import hashlib
import shutil

print('-' * 50)
print('File Hash Checking Tool')
print('-' * 50)
		

dirPath = input('Directory Path: ')
dirs = os.listdirs(dirPath)
for i in dirs:
	if os.path.isfile(i) == True:

		

