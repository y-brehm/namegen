#!/usr/bin/env python

from __future__ import print_function

import argparse
import os
import wikipedia

parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--page', type=str, default='List of legendary creatures from Japan',
                    help='wikipedia page to use as inspiration for name generating')

args = parser.parse_args()

maxNameLength = 10
minNameLength = 3

names = wikipedia.page(args.page).links

datasetFile = open("char-rnn-tensorflow/data/tinyshakespeare/input.txt", "w")
datasetFile.truncate(0)
for name in names:
    if maxNameLength >= len(name) > minNameLength:
       datasetFile.write(f"{name}\n")
datasetFile.close()

os.chdir("char-rnn-tensorflow")
os.system(f"python3 train.py --seq_length={minNameLength} --batch_size=128")

output = os.popen('python3 sample.py').read().split()
