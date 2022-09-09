import sys
import os

''' Read input from STDIN. Print your output to STDOUT '''
#Use input() to read input from STDIN and use print to write your output to STDOUT
# write code here
T = int(input())
for i in range (0,T):
    N = int(input())
    txt=str(N)
    if(N==17):
        print("Panic Attack")
    elif(txt.count("17")>=1):
        print("Panic Attack")
    elif(N%17==0):
        print("Panic Attack")
    else:
        print("Happy Face")
