#!/usr/bin/env python

import argparse
import os
import wikipedia
import time

from duckduckpy import query


def generateDataset(pageName):
    names = wikipedia.page(pageName).links
    datasetFile = open("char-rnn-tensorflow/dataset/input.txt", "w")
    datasetFile.truncate(0)
    for name in names:
        if maxNameLength >= len(name) > minNameLength:
           datasetFile.write(f"{name}\n")
    datasetFile.close()


def filterResults(names):
    outputFile = open("results.txt", 'a')
    for name in names:
        response = query(name, container='dict')
        time.sleep(0.2)
        if not response['heading'] and not response['results']:
            outputFile.write(f"{name}\n")


def trainOnDataset():
    os.chdir("char-rnn-tensorflow")
    if not os.path.isfile(os.path.join("save", "config.pkl")):
        os.system(f"python3 train.py --seq_length={minNameLength} --batch_size=128")


parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('--page', type=str, default='List of legendary creatures from Japan,',
                    help='wikipedia page to use as inspiration for name generating')

args = parser.parse_args()
maxNameLength = 10
minNameLength = 3

generateDataset(args.page)
trainOnDataset()

names = os.popen('python3 sample.py').read().split()

filterResults(names)
