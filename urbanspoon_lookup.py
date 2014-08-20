#************************************
# author: Jennifer Lam
# uni: jl3953
# Program: Pull.py
#
# Overview:...pulls stuff
#************************************

from urllib2 import Request, urlopen, URLError

location = raw_input('Please enter city: ' ) #location spaces must be typed with hyphens/lowercase
                                            # (morningside-heights)
food = raw_input('Please input food: ') 

url = 'http://www.urbanspoon.com/nf/3/200/253/NYC/'+location+'/'+food+'-Restaurants'

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
    outfile = open('urbanspoon_page.txt', 'w')
    outfile.write(line)
    outfile.close()

except URLError, e:
    return 'Company unfound'
