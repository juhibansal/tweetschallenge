# $Id: words_tweeted.py,v 1.3 2015/07/08 jbansal $

"""
Creates a list of words tweeted and count the occurence

Script Usage: 
  words_tweeted.py tweet_input tweet_output
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
def words_tweeted(dir_input,file_output):

	list_inputs=glob('%s/*.txt'%dir_input)
	if not list_inputs: 
		print 'Error: Directory %s has no text files. '%dir_input
		exit (1)
	ft1out = open('%s'%file_output,'w')
	dict_tweets  = {}
	k = 0
	for ifile in list_inputs:
		for line in file(ifile):
			line = line.strip()
			if not line: continue

			fields = line.split(' ')

			for x in fields:
				if not x in dict_tweets: dict_tweets[x] = 1
				else: dict_tweets[x] = dict_tweets[x] + 1
				if len(x) > k: k = len(x)
				continue
	
	
	for x in sorted(dict_tweets):
		print >> ft1out, x.ljust(k+2, ) + '%5g'%dict_tweets[x] 
	if debug_print: print pformat(dict_tweets)

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

	words_tweeted(dir_input,file_output)
