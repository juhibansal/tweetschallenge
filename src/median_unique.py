# $Id: median_unique.py,v 1.3 2015/07/08 jbansal $

"""
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
	#create a list to store number of unique words, number of times the same count of words has appeared
	#index of the list will be count of words and frequency of occurence pf the same count will be value of list at that count index
	#Assumption is tweet can not have more than 140 character, so list will not have length more than 140. Value can be any huge number 
	list_tweets  = [0]*140
	# Read each input file line by line 
	for ifile in list_inputs:
		for line in file(ifile):
			line = line.strip()
			if not line: continue
			fields = line.split()
			#Count the number of unique words from a line
			fields = list(set(fields))
			count = len(fields)
			#Increment the value in list if the same count occurs again
			list_tweets[count] = list_tweets[count] + 1
			# Call median function to calculate median and print with maximum 2 significant digits
			print >> ft2out, ('%.2f'%(median(list_tweets))).rstrip('0').rstrip('.')
			continue
	
	return

# function to calculate median
def median(list_tweets):
	#Total count of tweets is given by addition of all values in array.
	#Median will be 
		#list index at count/2 if count is odd and 
		#average of list indexs at int(count/2) and int(count/2)+1 if count it even
    
	total = sum(list_tweets)
	total_tillnow = 0
	median=0
	medianx=0
	mediany=0
	#Get list index at count/2 for odd number of tweets
	if (total%2!=0):
		for idx, val in enumerate(list_tweets):
			if val != 0:
				total_tillnow = total_tillnow + val
				if(total_tillnow >= int(total/2)+1):
					median = idx
					break
	#for Even count 2 possibilities
	    #list index at count/2 and count/2+1 is same then median will be index
	    #list index different at count/2 and count/2+1 then median will averages of 2 indexes
	if (total%2==0):
		for idx, val in enumerate(list_tweets):
			if val != 0:
				total_tillnow = total_tillnow + val
				if(total_tillnow >= int(total/2)):
					if(total_tillnow >= int(total/2)+1):
						median = idx
						break
					else:
						medianx = idx
						mediany = next((x for (x, y) in list(enumerate(list_tweets))[idx+1:] if y),idx)
						median = float(medianx+mediany)/2.0
						break
	return median
	
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
