# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 23:18:54 2021

@author: Sathish
"""

N=500
M=5000
conn=[]
file1 = open("500sample2.txt","a")#append mode


x=0
for i in range(1,11):
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