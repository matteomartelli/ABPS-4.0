#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import sys
import time

num=0
ntime=0
try:
	inputFile=sys.argv[1]
	tipo=int(sys.argv[2])
except:
	sys.exit("missing argument")

with open(inputFile) as data_file:    
    data = json.load(data_file)

for el in data["pacchetti"]:
	if el['type']==tipo:
		num=num+1
		if el['time']>150:
			ntime=ntime+1



avg=float(ntime)/float(num)
avg=avg*100
print(avg)
