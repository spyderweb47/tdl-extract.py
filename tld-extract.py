#!/usr/bin/env python3

import sys
import argparse

def get_args():
	parser = argparse.ArgumentParser("cat unsorted-subdomains.txt| tld-extract.py, tld-extract.py will extract top level domains from list of subdomain,\nwhich can help you in working with large list of \nsubdomains to extract its tld and can be modified in future for extra analysis\n")
	parser.add_argument('-l','--level',dest='index',help="degree of level in domain",default="False")
	args = parser.parse_args()
	return args

options = get_args()

if (options.index != "False"):
	index=int(options.index)
else:
	index = 2


# try:
# 	index = int(sys.argv[1])
# except:
# 	index = 2

def reverse(s):
	#reversing
	str = ""
	rev = ""
	for i in s:
		str = i + str

	j=0
	for i in str:
		if i==".":
			j=j+1
			if j>=index:
				break
			else:
				pass
		else:
			pass 
		rev = i + rev
	print(rev)

for line in sys.stdin:
	line= line.rstrip()
	reverse(line)

