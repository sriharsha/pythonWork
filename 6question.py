#!/usr/bin/env python
import math

c=50
h=30


input=raw_input()
output=[]
inputList=input.split(",")

for i in inputList:
	output.append(str(int(round(math.sqrt((2*c*int(i))/h)))))
	
print ','.join(output)
