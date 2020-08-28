#!/usr/bin/env python

import sys
import csv

if len(sys.argv) != 2:
    print('usage: script <filename>')
    sys.exit(1)

filename = sys.argv[1]

with open(sys.argv[1]) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(len(row))

