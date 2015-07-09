# $Id: median_unique.py,v 1.3 2015/07/08 jbansal $

"""
Creates a list of words tweeted and count the occurence

Script Usage: 
  median_unique.py tweet_input tweet_output
"""

# import python packages
import re
import os
from os.path import isfile,isdir
from pprint import pformat
from sys import argv, exit
from glob import glob

debug_print = 0

##############################
# Function
##############################
# --------------------------------------------------
def median_unique(dir_input,file_output):

	list_inputs=glob('%s/*.txt'%dir_input)
	if not list_inputs: 
		print 'Error: Directory %s has no text files. '%dir_input
		exit (1)
	ft2out = open('%s'%file_output,'w')
	list_tweets  = []
	for ifile in list_inputs:
		for line in file(ifile):
			line = line.strip()
			if not line: continue

			fields = line.split(' ')
			fields = list(set(fields))
			list_tweets.append(len(fields))
			print >> ft2out, ('%.2f'%(float(sum(list_tweets))/len(list_tweets))).rstrip('0').rstrip('.')
			continue
	
	return

##############################
# Main
##############################
if __name__ == "__main__":

	# read in configure info
	if len(argv) < 2:
		print __doc__
		exit (1)

	dir_input = argv[1]
	file_output = argv[2]

	if not os.path.isdir(dir_input): 
		print 'Error: Directory %s is not found. '%dir_input
		exit (1)
	loc = file_output.split('/')
	dir_output = '/'.join(loc[:len(loc)-1])
	if not os.path.isdir(dir_output): os.makedirs(dir_output)

	median_unique(dir_input,file_output)
