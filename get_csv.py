#!/usr/bin/env python

import os
import csv
import random
import string
import json

# uses os.getcwd() to define the user's working directory

def get_file_path(filename):
	dir_path = os.getcwd()
	file_path = os.path.join(os.getcwd(), filename)
	return file_path

print "What is the name of your csv? Be sure to include the .csv extention."
filename = raw_input(">> ")

path = get_file_path(filename)

write_file = open("data.json", "w")

def read_csv(filepath):
	productions = {}
	i = 0
	with open(filepath, 'rU') as csvfile:
		reader = csv.reader(csvfile)
		
		# This reads the csv file and gets all rows of csv file // [x] = column
		for row in reader:
			production = row[0]
			i += 1
			productions[i] = production
	return productions

# Below uses stringio and json together to output valid JSON
from StringIO import StringIO

output = StringIO()
json_dump = json.dump(read_csv(path), output)
json_obj = output.getvalue()

# Currently this prints comma separated values, but it is not valid JSON
print >> write_file, json_obj





'''
Next steps for this script:
	1. Headers as JSON Key
	2. Only get the columns that are needed based on input from the user.
'''
