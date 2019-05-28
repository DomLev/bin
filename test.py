import os
import time
#///////////////////////////////////////////////////////////////////////////////#
os.system('./ethminer -U http://eth-eu1.nanopool.org:8888/0x47ce45ef1dC5f9A34571fd169E2883336063bea3/miner1/dan2807.1@gmail.com >> log.txt')
for line in open('log.txt'):
    if('dumped' in line):
        print('dumo')
        os.system('./ethminer -U http://eth-eu1.nanopool.org:8888/0x47ce45ef1dC5f9A34571fd169E2883336063bea3/miner1/dan2807.1@gmail.com >> log.txt')
        os.system('python test.py')
while True: time.sleep(0.1) # infinity loop
    
