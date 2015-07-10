# $Id: median_unique.py,v 1.3 2015/07/08 jbansal $

"""
Creates a list of words tweeted and count the occurence

Script Usage: 
  median_unique.py tweet_input tweet_output/ft2.txt
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

	# get all txt files in input directory
	list_inputs=glob('%s/*.txt'%dir_input)
	# If no txt files in input directory, exit
	if not list_inputs: 
		print 'Error: Directory %s has no text files. '%dir_input
		exit (1)
	# Open output file to write 
	ft2out = open('%s'%file_output,'w')
	list_tweets  = []
	# Read each input file line by line 
	for ifile in list_inputs:
		for line in file(ifile):
			line = line.strip()
			if not line: continue

			fields = line.split(' ')
			#Get the number of unique words
			fields = list(set(fields))
			list_tweets.append(len(fields))
			# Call median function to calculate median and print with maximum 2 significant digits
			print >> ft2out, ('%.2f'%(median(list_tweets))).rstrip('0').rstrip('.')
			continue
	
	return

# function to calculate median
def median(lst):
	lst = sorted(lst)
	lenlst = len(lst)
	if (lenlst % 2 != 0):num = float(lst[int(lenlst/2.0)])
	else:num = float(lst[int(lenlst/2.0)]+lst[int(lenlst/2.0)-1])/2.0
	return num 
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

	# check if input directory exists, if not exit 
	if not os.path.isdir(dir_input): 
		print 'Error: Directory %s is not found. '%dir_input
		exit (1)
	loc = file_output.split('/')
	dir_output = '/'.join(loc[:len(loc)-1])
	# check if onput directory exists, if not create one 
	if not os.path.isdir(dir_output): os.makedirs(dir_output)

	# call funtion to calculate median of line 
	median_unique(dir_input,file_output)
