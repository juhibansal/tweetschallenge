# $Id: words_tweeted.py,v 1.3 2015/07/08 jbansal $

"""
Script Usage: 
  words_tweeted.py tweet_input tweet_output
######Missing some inputs##########
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
def words_tweeted(dir_input,dir_output):

	# get all txt files in input directory
	list_inputs=glob('%s/*.txt'%dir_input)
	# If no txt files in input directory, exit
	if not list_inputs: 
		print 'Error: Directory %s has no text files. '%dir_input
		exit (1)
	# Open output file to write 
	ft1out = open('%s/ft1.txt'%dir_output,'w')
	dict_tweets  = {}
	k = 0
	# Read each input file line by line 
	for ifile in list_inputs:
		for line in file(ifile):
			line = line.strip()
			if not line: continue
			# Split line by space
			fields = line.split()
			
			# Create dictionary with words and number of occurences
			for x in fields:
				if not x in dict_tweets: dict_tweets[x] = 1
				else: dict_tweets[x] = dict_tweets[x] + 1
				if len(x) > k: k = len(x)
				continue
	
	
	# Sort and print the list 
	for x in sorted(dict_tweets):
		# List is printed with words bein left justified using length of the longest string as spacing
		print >> ft1out, x.ljust(k+2, ) + '%5g'%dict_tweets[x] 
	if debug_print: print pformat(dict_tweets)

	return

##############################
# Main
##############################
if __name__ == "__main__":

	# read in configure info
	if len(argv) < 3:
		print __doc__
		exit (1)

	dir_input = argv[1]
	dir_output = argv[2]

	# check if input directory exists, if not exit 
	if not os.path.isdir(dir_input): 
		print 'Error: Directory %s is not found. '%dir_input
		exit (1)
	# check if onput directory exists, if not create one 
	if not os.path.isdir(dir_output): os.makedirs(dir_output)

	# call funtion to get frequency of words being tweeted 
	words_tweeted(dir_input,dir_output)
