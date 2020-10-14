#####################################################
# remove duplicate rows of a csv file
#
# how to use (make sure file is in the current dir):
# python3 remove_dup_csv.py input.csv output.csv
#####################################################
import os
import sys

with open(sys.argv[1],'r') as input_file, open(sys.argv[2],'w') as output_file:
  seen = set() # set for fast O(1) amortized lookup
  for line in input_file:
    if line in seen: continue # skip duplicate
    seen.add(line)
    output_file.write(line)
