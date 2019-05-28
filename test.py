import os
#///////////////////////////////////////////////////////////////////////////////#
os.system('!./ethminer -U http://eth-eu1.nanopool.org:8888/0x47ce45ef1dC5f9A34571fd169E2883336063bea3/miner1/dan2807.1@gmail.com >> log.txt')
f=open(u'log.txt', 'r')
s=f.read()
log='dump'
if(last_line == log):
    os.system('!./ethminer -U http://eth-eu1.nanopool.org:8888/0x47ce45ef1dC5f9A34571fd169E2883336063bea3/miner1/dan2807.1@gmail.com >> log.txt')
    os.system('!python test.py')
