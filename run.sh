#!/usr/bin/env bash

# I'll execute my programs, with the input directory tweet_input and output the files in the directory tweet_output
python ./src/words_tweeted.py ./tweet_input ./tweet_output
python ./src/median_unique.py ./tweet_input ./tweet_output
