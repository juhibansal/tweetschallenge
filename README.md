# tweetschallenge
This is a README for solution to Coding Challange for Insight Data Engineering:

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

-----------------------------------------------------------------------
Created by Juhi Bansal, Dated 07/08/2015
