#!/usr/bin/env python

import argparse
import os
import wikipedia
import time

from duckduckpy import query

maxNameLength = 10
minNameLength = 3

def generate_dataset(page_name):
    names = wikipedia.page(page_name).links
    dataset_file = open("char-rnn-tensorflow/dataset/input.txt", "w")
    dataset_file.truncate(0)
    for name in names:
        if maxNameLength >= len(name) > minNameLength:
           dataset_file.write(f"{name}\n")
    dataset_file.close()


def filter_results(names):
    filtered_names = []
    for name in names:
        response = query(name, container='dict')
        time.sleep(0.2)
        if not response['heading'] and not response['results']:
            filtered_names.append(name)
    return filtered_names


def train_on_dataset():
    os.chdir("char-rnn-tensorflow")
    if not os.path.isfile(os.path.join("save", "config.pkl")):
        os.system(f"python3 train.py --seq_length={minNameLength} --num_epochs=2000 --batch_size=128")


def write_results(names):
    for name in names:
        output_file = open("../results.txt", 'a')
        output_file.write(f"{name}\n")


def main(page_name, apply_filter:bool):
    if page_name is not None:
        generate_dataset(page_name)
    train_on_dataset()

    names = os.popen('python3 sample.py').read().split()

    if apply_filter:
        names = filter_results(names)

    print(names)
    write_results(names)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--page', type=str, default=None,
                        help='wikipedia page to use as inspiration for name generating. If left empty, you have to'
                             ' provide training text data in char-rnn-tensorflow/dataset/input.txt')
    parser.add_argument('--apply_filter', type=bool, default=False,
                        help='use DuckDuckGo to filter out names that already exist.')

    args = parser.parse_args()

    main(args.page, args.apply_filter)
