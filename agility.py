import csv
import numpy
import pylab as p
import time
from urllib2 import Request, urlopen, URLError
import os

dog_name = raw_input("Good Day!, please enter your dog's name?" + " ")
nadacnum = raw_input("Please enter " + dog_name + "'s" + " NADAC number:" + " ")

while True:

	request= Request("http://www.nadac.com/afrm/ph-to-csv.asp?regnum=" + nadacnum)

	try:
		print "Retrieving " + dog_name + "'s" + " records..."
		response = urlopen(request)
		points = response.read()
		f = open('points.csv', 'w+')
		f.write(points)
		f.close()


	except URLError, e:
		print "Got and error code:", e

	b = os.path.getsize('points.csv')
	if b >0:
		break
	else:
		nadacnum = raw_input("That was not a valid NADAC number, please try again")
	




#for row in reader:
	#points_earned = row[0]
	#class_level = row[1]
	#totalpts = row[2]
	#title = row[3]
	#date_earned = row[4]
	#trial = row[8]
filename = "points.csv"
#dog_name = "Canon"
	

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
	


def levelSort(filename,level):
	""" Enter a level, "E", "O" or "N" and will sort data by class at that level
	will then be used for plotting purposes """
	f = open(filename, 'rb')
	reader = csv.reader(f)
	regular = []
	jumpers = []
	chances = []
	tunnelers = []
	tnG = []
	weavers = []
	for row in reader:
		class_level = row[1]

		if level + "AC" in class_level:
			regular.append(class_level)
		elif level + "AS" in class_level:
			regular.append(class_level)
		elif level + "JC" in class_level:
			jumpers.append(class_level)
		elif level + "JS" in class_level:
			jumpers.append(class_level)
		elif level + "CC" in class_level:
			chances.append(class_level)
		elif level + "CS" in class_level:
			chances.append(class_level)
		elif "TN-" + level in class_level:
			tunnelers.append(class_level)
		elif "TNS-" + level in class_level:
			tunnelers.append(class_level)
		elif "TG-" + level in class_level:
			tnG.append(class_level)
		elif "TGS-" + level in class_level:
			tnG.append(class_level)
		elif "WV-" + level in class_level:
			weavers.append(class_level)
		elif "WVS-" + level in class_level:
			weavers.append(class_level)
	if level == "E":
		prefix = "Elite"
	elif level == "O":
		prefix = "Open"
	elif level == "N":
		prefix = "Novice"
	y = len(regular), len(jumpers), len(chances), len(tunnelers), len(tnG), len(weavers)
	group_labels = [prefix + " Regular", prefix +' Jumpers', prefix + ' Chances', prefix + ' Tunnelers', prefix + " Touch 'n Go", prefix + ' Weavers']
	return barPlot(y, group_labels)


#levelSort(filename, "E")



def classSort(filename, class_type):
    """ class_type: 'regular', 'jumpers', 'chances', 'tunnelers', 'touch 'n go', 'weavers', 'hoopers'
    Will sort and plot data by class type, all levels"""
    f = open(filename, 'rb')
    reader = csv.reader(f)
    Elite = []
    Open = []
    Novice = []
    if class_type == 'regular':
    	p,s = "AC","AS"
    elif class_type == 'jumpers':
    	p,s = "JC","JS"
    elif class_type == 'chances':
    	p,s = "CC","CS"
    elif class_type == 'tunnelers':
    	p,s = "TN-","TNS-"
    elif class_type == "touch 'n go":
    	p,s = "TG-","TGS-"
    elif class_type == 'weavers':
    	p,s = "WV-","WVS-"
    elif class_type == 'hoopers':
    	p,s = "HP-","HPS-"
    for row in reader:
    	class_level = row[1]
    	if s in class_level or p in class_level and "X" not in class_level:
    		if "E" in class_level:
    			Elite.append(class_level)
    		elif "O" in class_level:
    			Open.append(class_level)
    		elif "N" in class_level:
    			Novice.append(class_level)
    y = len(Novice), len(Open), len(Elite)
    group_labels = ['Novice ' + class_type.title(), 'Open ' + class_type.title(), 'Elite ' + class_type.title()]
    return barPlot (y, group_labels)


#classSort(filename, 'regular')   

    	
	
		

	
	
	
def clubSort(filename):
	"""  Will sort data by trial club name in order to plot number of Qs by club """
	f = open(filename, 'rb')
	reader = csv.reader(f)
	clubs = []
	split_list = []
	next = 0
	totals = []
	group_labels = []
	for row in reader:
		trial = row[8]
		clubs.append(trial)
	sorted_list = sorted(clubs[1:])   ##  Removes the column label "Host Club" from list
	for e in sorted_list:
		split = e.split(' ')
		split_list.append(split)
	while next <= len(split_list):
		if next >= len(split_list):
			break
		comp = [x for x in split_list if split_list[next][0] in x]
		totals.append(len(comp))
		labels = ' '.join(comp[0][0:-1])
		group_labels.append(labels)
		next += len(comp)
	y = totals
	return barPlot(y, group_labels)
	
#clubSort('points.csv')



	



def nadacYear(filename, start_year, end_year):
	""" Returns a chart showing the number of Qs per class and per level for the specified NADAC year"""
	f = open(filename, 'rb')
	reader = csv.reader(f)
	year1 = str(start_year)[2:]
	year2 = str(end_year)[2:]
	month1 = ["Aug", "Sep", "Oct", "Nov", "Dec"]
	month2 = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"]
	dates = []
	nyear1 = []
	nyear2 = []
	regular = []
	jumpers = []
	chances = []
	tunnelers = []
	tnG = []
	weavers = []
	for row in reader:
		date = row[8][-6:]
		class_level = row[1]
		dates.append(class_level +  ' ' + date)
		#print dates
	for e in dates:
		if year1 in e:
			for m in month1:
				if m in e:
					nyear1.append(e)
		elif year2 in e:
			for m in month2:
				if m in e:
					nyear2.append(e)
	class_date = nyear1 + nyear2
	for e in class_date:
		class_level = e[0:-6]

		if "A" in class_level:
			regular.append(class_level)
		elif "J" in class_level:
			jumpers.append(class_level)
		elif "CC" in class_level:
			chances.append(class_level)
		elif "CS" in class_level:
			chances.append(class_level)
		elif "TN" in class_level:
			tunnelers.append(class_level)
		elif "TG" in class_level:
			tnG.append(class_level)
		elif "WV" in class_level:
			weavers.append(class_level)
	eRegular = []
	oRegular = []
	nRegular = []
	eJumpers = []
	oJumpers = []
	nJumpers = []
	eChances = []
	oChances = []
	nChances = []
	eTunnelers = []
	oTunnelers = []
	nTunnelers = []
	etnG = []
	otnG = []
	ntnG = []
	eWeavers = []
	oWeavers = []
	nWeavers = []
	for i in regular:
		if i[0] == "E":
			eRegular.append(i)
		elif i[0] == "O":
			oRegular.append(i)
		elif i[0] == "N":
			nRegular.append(i)
	for i in jumpers:
		if i[0] == "E":
			eJumpers.append(i)
		elif i[0] == "O":
			oJumpers.append(i)
		elif i[0] == "N":
			nJumpers.append(i)
	for i in chances:
		if i[0] == "E":
			eChances.append(i)
		elif i[0] == "O":
			oChances.append(i)
		elif i[0] == "N":
			nChances.append(i)
	for i in tunnelers:
		if i[-2] == "E":
			eTunnelers.append(i)
		elif i[-2] == "O":
			oTunnelers.append(i)
		elif i[-2] == "N":
			nTunnelers.append(i)
	for i in tnG:
		if i[-2] == "E":
			etnG.append(i)
		elif i[-2] == "O":
			otnG.append(i)
		elif i[-2] == "N":
			ntnG.append(i)
	for i in weavers:
		if i[-2] == "E":
			eWeavers.append(i)
		elif i[-2] == "O":
			oWeavers.append(i)
		elif i[-2] == "N":
			nWeavers.append(i)
	

	y = len(eRegular), len(oRegular), len(nRegular),len(eJumpers), len(oJumpers), len(nJumpers),len(eChances), len(oChances), len(nChances),len(eTunnelers), len(oTunnelers), len(nTunnelers),len(etnG), len(otnG), len(ntnG),len(eWeavers), len(oWeavers), len(nWeavers)
	group_labels = [ "Elite Regular", "Open Regular", "Novice Regular", 
					"Elite Jumpers", "Open Jumpers", "Novice Jumpers",
					"Elite Chances", "Open Chances", "Novice Chances",
					"Elite Tunnelers", "Open Tunnelers", "Novice Tunnelers",
					"Elite Touch 'n Go", "Open Touch 'n Go", "Novice Touch 'n Go",
					"Elite Weavers", "Open Weavers", "Novice Weavers"]
	return barPlot(y, group_labels)
	
	
	
	

#nadacYear(filename, 2012, 2013)


	

	
def lifetimeSort(filename):
	""" Will sort Qs by class only (include all levels) for lifetime of dog"""
	f = open(filename, 'rb')
	reader = csv.reader(f)
	regular = []
	jumpers = []
	chances = []
	tunnelers = []
	tnG = []
	weavers = []
	for row in reader:
		class_level = row[1]
		if "A" in class_level:
			regular.append(class_level)
		elif "J" in class_level:
			jumpers.append(class_level)
		elif "CC" in class_level:
			chances.append(class_level)
		elif "CS" in class_level:
			chances.append(class_level)
		elif "TN" in class_level:
			tunnelers.append(class_level)
		elif "TG" in class_level:
			tnG.append(class_level)
		elif "WV" in class_level:
			weavers.append(class_level)
	eRegular = []
	oRegular = []
	nRegular = []
	eJumpers = []
	oJumpers = []
	nJumpers = []
	eChances = []
	oChances = []
	nChances = []
	eTunnelers = []
	oTunnelers = []
	nTunnelers = []
	etnG = []
	otnG = []
	ntnG = []
	eWeavers = []
	oWeavers = []
	nWeavers = []
	for i in regular:
		if i[0] == "E":
			eRegular.append(i)
		elif i[0] == "O":
			oRegular.append(i)
		elif i[0] == "N":
			nRegular.append(i)
	for i in jumpers:
		if i[0] == "E":
			eJumpers.append(i)
		elif i[0] == "O":
			oJumpers.append(i)
		elif i[0] == "N":
			nJumpers.append(i)
	for i in chances:
		if i[0] == "E":
			eChances.append(i)
		elif i[0] == "O":
			oChances.append(i)
		elif i[0] == "N":
			nChances.append(i)
	for i in tunnelers:
		if i[-1] == "E":
			eTunnelers.append(i)
		elif i[-1] == "O":
			oTunnelers.append(i)
		elif i[-1] == "N":
			nTunnelers.append(i)
	for i in tnG:
		if i[-1] == "E":
			etnG.append(i)
		elif i[-1] == "O":
			otnG.append(i)
		elif i[-1] == "N":
			ntnG.append(i)
	for i in weavers:
		if i[-1] == "E":
			eWeavers.append(i)
		elif i[-1] == "O":
			oWeavers.append(i)
		elif i[-1] == "N":
			nWeavers.append(i)
	
	y = len(eRegular), len(oRegular), len(nRegular),len(eJumpers), len(oJumpers), len(nJumpers),len(eChances), len(oChances), len(nChances), len(eTunnelers), len(oTunnelers), len(nTunnelers),len(etnG), len(otnG), len(ntnG), len(eWeavers), len(oWeavers), len(nWeavers)
	
	group_labels = [ "Elite Regular", "Open Regular", "Novice Regular", 
					"Elite Jumpers", "Open Jumpers", "Novice Jumpers",
					"Elite Chances", "Open Chances", "Novice Chances",
					"Elite Tunnelers", "Open Tunnelers", "Novice Tunnelers",
					"Elite Touch 'n Go", "Open Touch 'n Go", "Novice Touch 'n Go",
					"Elite Weavers", "Open Weavers", "Novice Weavers"]
	return barPlot(y, group_labels)
	

#lifetimeSort(filename)

	

	
	
