#************************************
# author: Jennifer Lam
# uni: jl3953
# Program: Pull.py
#
# Overview:...pulls stuff
#************************************

from urllib2 import Request, urlopen, URLError

'''
location = raw_input('Please enter city: ' ) #location spaces must be typed with plus signs
food = raw_input('Please input food: ') 
'''

def yelp(location, food):

	url = 'http://www.yelp.com/search?find_desc='+food+'&find_loc='+location+'&ns=1&ls=083e80cdbf630160'

	request = Request(url)

	try:
		response = urlopen(request)
		read_buffer = ""
		line = response.read()

		outfile = open('yelp_page.txt', 'w')
		outfile.write(line)
		outfile.close()

	except URLError, e:
		print 'Company unfound'

#print yelp('East Village', 'korean bbq')