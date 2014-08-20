from urllib2 import Request, urlopen, URLError

import re

def pull():
	''' Pulls the data from the site.'''

	url = 'http://www.health.ny.gov/statistics/cancer/registry/appendix/neighborhoods.htm'
	request = Request(url)
	response = urlopen(request)

	buff = response.read()
	buff_list = buff.split('\n')

	table = analyze(buff_list)

	new_table = hash_converter(table)

	return new_table

def analyze(buff_list):
	''' returns a hashtable of neighborhoods and zipcodes'''

	keyword = '</tr><tr>\r'
	a = dict()

	for i in range(len(buff_list)):

		if buff_list[i] == keyword:
			n = neighborhood(buff_list[i+1])

			if n[0] == 'Bronx' or n[0] == 'Brooklyn' or n[0] == 'Queens' or n[0] == 'Staten Isl and ' or n[0] == 'Manhattan':
				i = i+1
				n = neighborhood(buff_list[i+1])

			'''
			#Bronx
			if n[0] == 'Central Bronx' or n[0] == 'Bronx Park and Fordham' or n[0] == 'High Bridge and Morrisania' or \
			n[0] == 'Hunts Point and Mott Haven' or n[0] == 'Kingsbridge and Riverdale' or n[0] == 'Northeast Bronx' or \
			n[0] == 'Southeast Bronx' :
				n = 'Uptown'
			
			#Brooklyn
			if (n[0] == 'Central Brooklyn' or n[0] == 'Southwest Brooklyn' or n[0] == 'Borough Park' or \
			n[0] == 'Canarsie and Flatlands' or n[0]== 'Southern Brooklyn' or n[0] == 'Northwest Brooklyn' \
			or n[0] == 'Flatbush' or n[0] == 'East New York and New Lots' or n[0] == 'Greenpoint' or \
			n[0] == 'Sunset Park' or n[0] == 'Bushwick and Williamsburg'):
				n = 'Brooklyn'

			# Queens
			if (n[0] == 'Northeast Queens' or n[0] == 'North Queens' or n[0] == 'Central Queens' or n[0] == 'Jamaica')
				or n[0] == 'Northwest Queens' or n[0] == 'West Central Queens' or n[0] == 'Rockaways' or \
				n[0] == 'Southeast Queens' or n[0] == 'Southwest Queens' or n[0] == 'West Queens'):
				n == 'Queens'
			'''
	
			z = zipcode(buff_list[i+2])
			add(a, n, z)

	return a

#MidIslands
#Canarsie

def neighborhood(my_str):
	'''  returns list of neighborhoods.'''

	temp = my_str.split('<td')
	temp = temp[1].split('<')
	temp = temp[0].split('>')
	temp = temp[1].split('and')

	for i in range(len(temp)):
		temp[i] = temp[i].strip(' ')

	final = temp[0]
	for i in range(1, len(temp)):
		final += ' and '+temp[i]

	temp = [final]

	return temp

def zipcode(my_str):

	''' returns a list of zipcodes'''

	temp = my_str.split('<td headers="header3">')
	temp = temp[1].split('</td>\r')
	temp = temp[0].split(',')

	for i in range(len(temp)):
		temp[i] = temp[i].strip(' ')
	return temp

def add(table, key, value):
	''' takes in a table, key (in list form), and value (in list form) to add'''

	for i in range(len(key)):
		table[key[i].strip(' ')] = value

	return table

def hash_converter(table):
	''' converts keys and values.'''

	new_table = dict()

	#gets keys
	key_list = table.keys()

	for element in key_list:
		value_list = table[element] # list of zipcodes

		n_element = element
		for code in value_list:
			if element == 'Bronx Park and Fordham' or element == 'High Bridge and Morrisania' or \
			element == 'Hunts Point and Mott Haven' or element == 'Kingsbridge and Riverdale' or element == 'Northeast Bronx' or \
			element == 'Southeast Bronx' or element == 'Central Bronx':
				n_element = 'Uptown'

			if (element == 'Central Brooklyn' or element == 'Southwest Brooklyn' or element == 'Borough Park' or \
			element == 'Canarsie and Flatl and s' or element== 'Southern Brooklyn' or element == 'Northwest Brooklyn' \
			or element == 'Flatbush' or element == 'East New York and New Lots' or element == 'Greenpoint' or \
			element == 'Sunset Park' or element == 'Bushwick and Williamsburg'):
				n_element = 'Brooklyn'

			if (element== 'Northeast Queens' or element == 'North Queens' or element == 'Central Queens' \
				or element == 'Jamaica' or element == 'Northwest Queens' or element == 'West Central Queens' \
				or element == 'Rockaways' or element == 'Southeast Queens' or element == 'Southwest Queens' \
				or element == 'West Queens'):
				n_element = 'Queens'

			if (element == 'Port Richmond' or element == 'South Shore' or \
				element == 'Stapleton and St.George' or element == 'Mid-Isl and'):
				n_element = 'Soho Trbca FinDist'

			if (element == 'Central Harlem' or element == 'East Harlem' or element == 'Inwood and Washington Heights'):
				n_element = 'Uptown'

			if (element == 'Chelsea and Clinton'):
				n_element = 'Midtown South Chelsea'

			if (element == 'Gramercy Park and Murray Hill'):
				n_element = 'Murray Hill Gramercy'

			if (element == 'Greenwich Village and Soho' or element == 'Lower Manhattan'):
				n_element = 'Soho Trbca FinDist'

			if (element == 'Lower East Side'):
				n_element = 'East Village LES'

			new_table[int(code.strip(' '))] = n_element

	infile = open('table.txt', 'w')
	infile.write(str(new_table))
	infile.close()

	return new_table

def search(zipcode, table):
	''' searches the table for a zipcode (five digit int)'''

	if zipcode in table:
		return table[zipcode]
	else:
		return ''

def main(zipcode):

	table = pull()

	print search(zipcode, table)

	return search(zipcode, table)

