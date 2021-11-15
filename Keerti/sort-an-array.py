#!/usr/bin/env python3

import sys

try:
    file = sys.argv[1]
except IndexError:
    file = input("~% ")

# Read the file
with open(file, 'r') as f:
    lines = f.readlines()
    print(*lines, sep='\n')
