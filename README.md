# tweetschallenge
This is a README for solution to Coding Challange:

Problem statement is to implement codes for two features:
Calculate the total number of times each word has been tweeted.
Calculate the median number of unique words per tweet, and update this median as tweets come in.

Details of Solution:
Code is implemented in Unix using Python (version 2.6.4) as a Platform. Codes are named words_tweeted.py and median_unique.py and as required by the challenge a run file (run.sh) is provided to run the scripts.

Packages used are:
import re,
import os,
from os.path import isfile,isdir,
from pprint import pformat,
from sys import argv, exit,
from glob import glob

Both codes look at any number of *txt files in the tweet_output folder and summarizes results under the directory specified in run file. Result filenames are hard coded to ft1.txt and ft2.txt 

Main features of solutions

1. Total Word Count: 
Code read each text file inside the input folder line by line and store unique word in a dictionary as a key and number of times the word appear as it value. If the same word appear again, the value is updated. Dictionary is printed at the end with left justified words (based on the maximum word length) and right justified values.

2. Median of unique words for each line: 
To get the median out of a list of values, we need to have access to each values. However as the list grows, its difficult to store each value in the list. 
Therefore a frequency based system has been used to keep an account of values in the list. Assumptions here are: word count will only be integer and since a tweet can not have more than 140 characters, the directory size will never go beyond 140.  
Algorithm:
Code read each text file inside the input folder line by line and store count of unique word in each tweet in a dictionary as a key
Each time the same count appears value of the key is updated (+1). 
To calculate median first, check the first and last key for the dictionary and their values and start removing the keys from the dictionary until only 1 key or 2 keys (with value of 1 each) left. And calculate median from it

-----------------------------------------------------------------------
Created by Juhi Bansal, Dated 07/08/2015
