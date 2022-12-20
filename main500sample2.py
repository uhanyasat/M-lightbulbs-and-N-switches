# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 00:06:10 2021

@author: Sathish
"""

N=500
M=5000
conn=[]
file1 = open("500sample1.txt","a")#append mode


x=0
for i in range(11,21):
    for k in range(0,2):
        for j in range(21,N):
            if k==0:
               ii=str(i)
               jj=str(j)
               wr=ii+','+jj
               file1.write(wr)
               file1.write('\n')
               x=x+1
            elif k==1:
                ii1=str(i)
                jj1=str(-j)
                wr=ii1+','+jj1
                file1.write(wr)
                file1.write('\n')
                x=x+1
            if x > M:
                break
file1.close()