#####################################################
# how to use:
# python3 diff.py csv1 csv2 output

# where 1st column from csv1 not found in csv2
# should NOT go inside output file.

# contents from newcsv are the updated rows from csv1
#####################################################
import csv
import os
import sys

first_file = sys.argv[1]
second_file = sys.argv[2]
output_file = sys.argv[3]

data = {}  # creating dictionary to store the data

with open(first_file, 'r') as lookuplist:
  reader1 = csv.reader(lookuplist)
  for col in reader1:
    data[col[0]] = col[0]  # stores the data from column 0 to column 1 in the data list

with open(second_file, 'r') as csvinput, open(output_file, 'w', newline='') as f_output:
  reader2 = csv.reader(csvinput)
  csv_output = csv.writer(f_output)
  for col in reader2:
    # if the column 1 in csv1 does not match with column 0 in csv2 extract
    if col[0] in data:
      # col = [col[0]] # this only saves the first column
      csv_output.writerow(col)  # writes all the data that is matched in cmdb wlc extract



#####################################################
# how to use:
# python3 diff.py csv1 csv2 newcsv

# where 1st column from csv1 not found in csv2
# should NOT go inside newcsv file.

# contents from newcsv are the updated rows from csv1
#####################################################
# import sys
# import os

# checklist = []

# os.system('rm ' + sys.argv[3])

# with open(sys.argv[1], 'r') as t1, open(sys.argv[2], 'r') as t2:
#   fileOne = t1.readlines()
#   fileTwo = t2.readlines()

# with open(sys.argv[3], 'w') as outFile:
#   for line in fileOne:
#     checkTwo = line.split(",")
#     checklist.append(checkTwo[0])

#   for line in fileTwo:
#     checkOne = line.split(",")
#     if checkOne[0] not in checklist:
#       outFile.write(line)
