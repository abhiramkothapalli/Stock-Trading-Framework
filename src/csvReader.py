#returns an array of stock quotes read from a csv list

import sys
sys.dont_write_bytecode = True

import csv
import subprocess
import urllib
import variables


def csvReader(strategy):

	if strategy == None:
		return None
	
	list = []
	
	r = csv.reader(urllib.urlopen(strategy), delimiter=",")
	for row in r:
		list.append(row)
	if not variables.forex:	
		list.remove(list[0])
		
	return list