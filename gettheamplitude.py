import sys
from decimal import *
import time as t
import numpy as np


fout = open('outputdata.csv','w+')
fout.write('oscillation No,time,amplitude\n')
oscillation=0

naturallogampvalues=[] # 2d array containing the time at which a cycle started and the ln value of the amplitude

with open(sys.argv[1], 'r') as f:
    # get the amplitude value
    # find the time at which amplitude is at a maximum
    f.readline() # skip the column names
    line = f.readline()
    maxamp=Decimal(0)
    while line:
        amplitude=Decimal(line.split(",")[1])
        time=line.split(",")[0]
        if amplitude>maxamp:
            maxamp=Decimal(amplitude)
        line=f.readline()
        amplitude=Decimal(line.split(",")[1])
        if amplitude<maxamp:
            print(f'\n{time}  {maxamp}\n')
            oscillation+=1
            if maxamp<0:
                print('error')
            else:
                naturallogampvalues.append((time,maxamp.ln()))
                fout.write(f'{oscillation},{time},{maxamp}\n')

            minamp = amplitude
            while True:
                newamp = Decimal(f.readline().split(",")[1])
                if minamp<newamp:
                    maxamp=minamp
                    del minamp,newamp
                    line=f.readline()
                    break
                else:
                    minamp=newamp
                print(".",end='',flush=True)
                t.sleep(0.005)
    print(naturallogampvalues)    

fout.close()
