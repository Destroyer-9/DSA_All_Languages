from os import *
from sys import *
from collections import *
from math import *

def findMajorityElement(arr, n):
	# Write your code here.
    dt = dict()
    
    for e in arr:
        if e in dt:
            dt[e] += 1
            if dt[e] > n//2:
                return e
        else:
            dt[e] = 1
        print(dt)
    return -1

ip = list(map(int,input().split()))
print(findMajorityElement(ip,len(ip)))

# Just Testing