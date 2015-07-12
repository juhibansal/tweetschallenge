# $Id: median_unique.py,v 1.3 2015/07/08 jbansal $

"""
Script Usage: 
  median_unique.py tweet_input tweet_output
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
def median_unique(dir_input,dir_output):

	# get all txt files in input directory
	list_inputs=glob('%s/*.txt'%dir_input)
	# If no txt files in input directory, exit
	if not list_inputs: 
		print 'Error: Directory %s has no text files. '%dir_input
		exit (1)
	# Open output file to write 
	ft2out = open('%s/ft2.txt'%dir_output,'w')
	#create a dictionary to store number of unique words, number of times the same count of words has appeared
	dict_tweets  = {}
	# Read each input file line by line 
	for ifile in list_inputs:
		for line in file(ifile):
			line = line.strip()
			if not line: continue

			fields = line.split()
			#Count the number of unique words from a line
			fields = list(set(fields))
			#Store the word count as key and number of times the same key appear as value
			#Keep incrementing the value of the key in the dictionary if the same count appears
			#Storing frequency based dictionay is usedful to support of large amount of data, 
			#since twitter can have maximum 140 characters, in worst case size of directory will never be more than 140.
			#With every additional tweets only frequency will need to be incremented. Size of dictionary wont increase
			if not len(fields) in dict_tweets: dict_tweets[len(fields)] = 1
			else: dict_tweets[len(fields)] = dict_tweets[len(fields)] + 1
			# Call median function to calculate median and print with maximum 2 significant digits
			print >> ft2out, ('%.2f'%(median(dict_tweets))).rstrip('0').rstrip('.')
			continue
	
	return

# function to calculate median
def median(dict_tweets):
	flag = 0
	#recursive function to elimitate first or end key of dictionary based on the frequency of the key
	#Perform recursion only of dictionary has more than 1 key or more than 2 keys with different frequencies
	while (len(dict_tweets) > 1):
		if (len(dict_tweets) ==2 and dict_tweets.values()[0]==dict_tweets.values()[1]):
			flag = 1
			break
		dict_tweets = eliminate(dict_tweets)
	
	#calculate median, if two keys left then take median as addition of 2
	if flag == 1: median = (dict_tweets.keys()[0] + dict_tweets.keys()[1])/2.0
	#else take the only key left
	else: median = dict_tweets.keys()[0]
	return median

#elimiate the first or last end key of dictionary, if the first key value is larger then remove last key and vice versa and subtract the key value
# if first and last key value are same then remove both from dictionary
def eliminate(dict_tweets):
	#sorting dictionary by keys
	sorted_tweets = sorted(dict_tweets)
	dict_len = len(dict_tweets)
	#get first key and last key
	firstkey = sorted_tweets[0]
	lastkey = sorted_tweets[dict_len-1]
	#get first key value and last key value
	firstvalue = dict_tweets[firstkey]
	lastvalue = dict_tweets[lastkey]
	#if first key value is more remove last key and subtract last key value from first one, i.e. change the frequency of first key occurence
	if firstvalue > lastvalue:
		firstvalue = firstvalue - lastvalue
		dict_tweets[firstkey]=firstvalue
		if lastkey in dict_tweets: del dict_tweets[lastkey]
	#if first key value is less remove first key and subtract first key value from last key value
	elif firstvalue < lastvalue:
		lastvalue = lastvalue - firstvalue
		dict_tweets[lastkey]=lastvalue
		if firstkey in dict_tweets: del dict_tweets[firstkey]
	#if first key value = last key value remove both
	elif firstvalue == lastvalue:
		if firstkey in dict_tweets: del dict_tweets[firstkey]
		if lastkey in dict_tweets: del dict_tweets[lastkey]
	return(dict_tweets)
	
##############################
# Main
##############################
if len(argv) < 3:
	print __doc__
	
else:
	dir_input = argv[1]
	dir_output = argv[2]

	# check if input directory exists, if not exit 
	if not os.path.isdir(dir_input): 
		print 'Error: Directory %s is not found. '%dir_input
		exit (1)
	# check if onput directory exists, if not create one 
	if not os.path.isdir(dir_output): os.makedirs(dir_output)

	# call funtion to calculate median of line 
	median_unique(dir_input,dir_output)
