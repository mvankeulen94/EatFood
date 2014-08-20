#************************************
# author: Jennifer Lam
# uni: jl3953
# Program: Pull.py
#
# Overview:...pulls stuff
#************************************

from urllib2 import Request, urlopen, URLError

'''
location = raw_input('Please enter city: ' ) #location spaces must be typed with hyphens/lowercase
                                            # (morningside-heights)
food = raw_input('Please input food: ') 
'''

def menupages(m_location, food):

    location_list = m_location.split(' ')
    location = location_list[0]
    for i in range(1, len(location_list)):
        location += '-'+location_list[i]

    url = 'http://www.menupages.com/restaurants/food/'+food+'/'+location+'/all-neighborhoods/all-cuisines/'

    request = Request(url)

    try:
        response = urlopen(request)
        read_buffer = ""
        line = response.read()
    
        outfile = open('menupages_page.txt', 'w')
        outfile.write(line)
        outfile.close()
        return 'nothing'

    except URLError, e:
        return 'Company unfound'

#print menupages('East Village LES', 'sushi')
