#************************************
# author: Jennifer Lam
# uni: jl3953
# Program: Pull.py
#
# Overview:...pulls stuff
#************************************

from urllib2 import Request, urlopen, URLError

#WHATT???
location = raw_input('Please enter city: ' )
food = raw_input('Please input food: ')

#url = 'https://www.grubhub.com/search/'+location+'/?searchTerm='+food+'&filters=openNow'
url = 'http://www.yelp.com/search?find_desc='+food+'&find_loc='+location+'&ns=1&ls=083e80cdbf630160'

request = Request(url)

try:
    response = urlopen(request)
    read_buffer = ""
    line = response.read()
    '''
    while line != None:
        line = response.readline()
        read_buffer = read_buffer + line + '\n'
    '''
    outfile = open('htmlpage.txt', 'w')
    outfile.write(line)
    outfile.close()

except URLError, e:
    print 'Company unfound'
