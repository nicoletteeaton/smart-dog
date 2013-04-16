from collections import Counter
from urllib2 import Request, urlopen, URLError
import csv
import numpy
import pylab as p
import time
import os

filename = "points-10-01124.csv"
dog_name = "Canon"
def parse(filename, delimiter):
    """ Parses the csv points file to a JSON-like object"""
    opened_file = open(filename)

    csv_data = csv.reader(opened_file, delimiter=delimiter)

    parsed_data = []

    # Skip over the first line of the file for the headers
    fields = csv_data.next()

    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

    opened_file.close()

    return parsed_data

parsed_data =  parse(filename, ",")
count_host_club = Counter(item["Host Club"][:-6] for item in parsed_data)
count_by_class = Counter(item["Class"] for item in parsed_data)

#for item in parsed_data:
#	nadac_class = item["Class"]
#	print nadac_class

# counter will work best for "Class", "Title" and "Host Club"
# other keys, like "Date Earned" and "Platinum" will need the nadac_class
# associated with the values

# dict keys:
# Points
# Class
# Total Points
# Title
# Date Earned
# DRI
# Silver/Purple
# Platinum
# Host Club

# plot returned in all functions

def barPlot(y, group_labels):
	"""  Will plot a bar plot given
	y: list of numbers to be plotted
	group_labels: """
	fig = p.figure()
	ax = fig.add_subplot(1,1,1)
	N = len(y)
	ind = range(N)
	barChart = ax.bar(ind, y, facecolor='blue', align='center')
	ax.set_ylabel("# of Qs")
	ax.set_xticks(ind)
	ax.set_xticklabels(group_labels)
	p.title(dog_name + "'s" + " Qs")
	fig.autofmt_xdate()
	def autolabel(barChart):
		for bar in barChart:
			height = bar.get_height()
			ax.text(bar.get_x() + bar.get_width()/2, 1.01*height,'%d'%int(height), ha = 'center', va = 'bottom')
	autolabel(barChart)
	p.show()



# helper functions for nadac_classSort()			
	
def regular_classSort():
	"""will sort parsed data by the
	regular class, helper function for
	nadac_classSort()"""
	group_labels = []
	y = []
	parsed_data =  parse(filename, ",")
	count_by_class = Counter(item["Class"] for item in parsed_data)
	for key in count_by_class:
		if "X" not in key:
			if "AC" in key or "AS" in key:
				group_labels.append(key)
				y.append(count_by_class[key])
	return barPlot(y, group_labels)


def jumpers_classSort():
	"""will sort parsed data by the
	jumpers class, helper function for
	nadac_classSort()"""
	group_labels = []
	y = []
	parsed_data =  parse(filename, ",")
	count_by_class = Counter(item["Class"] for item in parsed_data)
	for key in count_by_class:
		if "X" not in key:
			if "JC" in key or "JS" in key:
				group_labels.append(key)
				y.append(count_by_class[key])
	return barPlot(y, group_labels)
	
	
	
	
def chances_classSort():
	"""will sort parsed data by the
	chances class, helper function for
	nadac_classSort()"""
	group_labels = []
	y = []
	parsed_data =  parse(filename, ",")
	count_by_class = Counter(item["Class"] for item in parsed_data)
	for key in count_by_class:
		if "X" not in key:
			if "CC" in key or "CS" in key:
				group_labels.append(key)
				y.append(count_by_class[key])
	return barPlot(y, group_labels)
	


def tunnelers_classSort():
	"""will sort parsed data by the
	tunnelers class, helper function for
	nadac_classSort()"""
	group_labels = []
	y = []
	parsed_data =  parse(filename, ",")
	count_by_class = Counter(item["Class"] for item in parsed_data)
	for key in count_by_class:
		if "X" not in key:
			if "TN-" in key or "TNS-" in key:
				group_labels.append(key)
				y.append(count_by_class[key])
	return barPlot(y, group_labels)
	

def touchNgo_classSort():
	"""will sort parsed data by the 
	touch 'n go class, helper function
	for nadac_classSort()"""
	group_labels = []
	y = []
	parsed_data =  parse(filename, ",")
	count_by_class = Counter(item["Class"] for item in parsed_data)
	for key in count_by_class:
		if "X" not in key:
			if "TG-" in key or "TGS-" in key:
				group_labels.append(key)
				y.append(count_by_class[key])
	return barPlot(y, group_labels)

	
def weavers_classSort():
	"""will sort parsed data by the
	weavers class, helper function
	for nadac_classSort()"""
	group_labels = []
	y = []
	parsed_data =  parse(filename, ",")
	count_by_class = Counter(item["Class"] for item in parsed_data)
	for key in count_by_class:
		if "X" not in key:
			if "WV-" in key or "WVS-" in key:
				group_labels.append(key)
				y.append(count_by_class[key])
	return barPlot(y, group_labels)
	
	
def hoopers_classSort():
	"""will sort parsed data by the
	hoopers class, helper function
	for nadac_classSort()"""
	group_labels = []
	y = []
	parsed_data =  parse(filename, ",")
	count_by_class = Counter(item["Class"] for item in parsed_data)
	for key in count_by_class:
		if "X" not in key:
			if "HP-" in key or "HPS-" in key:
				group_labels.append(key)
				y.append(count_by_class[key])
	return barPlot(y, group_labels)
	
	
def extremeGames_classSort():
	"""will sort parsed data by
	all extreme games classes, helper
	function for nadac_classSort()"""
	group_labels = []
	y = []
	parsed_data =  parse(filename, ",")
	count_by_class = Counter(item["Class"] for item in parsed_data)
	for key in count_by_class:
		if "X" in key:
			group_labels.append(key)
			y.append(count_by_class[key])
	return barPlot(y, group_labels)
			
	
	
def nadac_classSort(nadac_class):
	""" will return a plot displaying the
	number of Qs earned in that class by level
	(elite, open and novice)
	nadac_class: "regular", "jumpers", "chances", "tunnelers",
	"touch 'n go", "weavers", "hoopers", "extreme games" """
	if nadac_class == "regular":
		return regular_classSort()
	elif nadac_class == "jumpers":
		return jumpers_classSort()
	elif nadac_class == "chances":
		return chances_classSort()
	elif nadac_class == "tunnelers":
		return tunnelers_classSort()
	elif nadac_class == "touch 'n go":
		return touchNgo_classSort()
	elif nadac_class == "weavers":
		return weavers_classSort()
	elif nadac_class == "hoopers":
		return hoopers_classSort()
	elif nadac_class == "extreme games":
		return extremeGames_classSort()
		
		
def levelSort(level):
	"""will sort parsed data by level
	and return a plot displaying the number of
	Qs earned by nadac class
	level: "E", "O" or "N" """
	parsed_data =  parse(filename, ",")
	count_by_class = Counter(item["Class"] for item in parsed_data)
	group_labels = []
	y = []
	for key in count_by_class:
		if level in key:
			group_labels.append(key)
			y.append(count_by_class[key])
	return barPlot(y, group_labels)
		
		
	

def clubSort():
	""" will sort parsed data by Host Club, and
	return a plot displaying the number of Qs
	earned at that club's trials over the dogs'
	lifetime"""
	parsed_data =  parse(filename, ",")
	count_host_club = Counter(item["Host Club"][:-6] for item in parsed_data)
	group_labels = []
	y = []
	for key in count_host_club:
		group_labels.append(key)
		y.append(count_host_club[key])
	return barPlot(y, group_labels)
	
	
def lifetimeSort():
	"""will sort Qs by nadac class only
	(include all levels) for lifetime of dog"""
	parsed_data =  parse(filename, ",")
	count_by_class = Counter(item["Class"] for item in parsed_data)
	group_labels = []
	y = []
	for key in count_by_class:
		group_labels.append(key)
		y.append(count_by_class[key])
	return barPlot(y, group_labels)
	
	
def nadacYear(start_year, end_year):
	""" Returns a plot showing the number
	of Qs per class and per level for the
	specified NADAC year,  NADAC year is 
	from August 1 - July 31"""
	
	# convert start and end year to strings in YY format
	start_year = str(start_year)
	end_year = str(end_year)

	# make list_of_tuples = (nadac_class, Date Earned)
	list_of_tuples = []
	parsed_data =  parse(filename, ",")
	for item in parsed_data:
		tuple = (item["Class"], item["Date Earned"])
		list_of_tuples.append(tuple)
	# have list_of_tuples which contains all Qs
	# need to pull tuples that contain start_year and end_year
	# make a list of item[0] in tuple (class name)
	class_name = []
	for item in list_of_tuples:
		if start_year in item[1]:
			class_name.append(item[0])
		elif end_year in item[1]:
			class_name.append(item[0])

	# set up counter for class_name list
	q_count = [(x, class_name.count(x)) for x in set(class_name)]
	print q_count
	# set up bar plot
	y = []
	group_labels = []
	for item in q_count:
		group_labels.append(item[0])
		y.append(item[1])
	return barPlot(y, group_labels)

	

def platinumSort():
	""" Returns a plot showing the number
	of platinum Qs per class for the lifetime
	of the dog"""
# make list_of_tuples = (nadac_class, Platinum)
list_of_tuples = []
parsed_data =  parse(filename, ",")
for item in parsed_data:
	tuple = (item["Class"], item["Platinum"])
	list_of_tuples.append(tuple)

# need to remove Qs that were not platinum runs
empty = []
platinum_list = []

for tuple in list_of_tuples:
	if tuple[1] == '':
		empty.append(tuple)
	else:
		p.append(tuple)
print platinum_list



