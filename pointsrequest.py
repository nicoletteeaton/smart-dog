from urllib2 import Request, urlopen, URLError

request= Request("http://www.nadac.com/afrm/ph-to-csv.asp?regnum=10-01124")
try:
	response = urlopen(request)
	points = response.read()
	f = open('points.csv', 'r+')
	f.write(points)
	f.close()
	
	
except URLError, e:
	print "Got and error code:", e