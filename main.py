# user types in a specific neighborhood in nyc and food type, program will output a list of all that
import menupages_lookup as menupages
import retriever
import zipcode_converter as zc 

'''
def main(location, food):

	#parsing location and food strings
	location_list = location.split(' ')
	y_location = location_list[0]
	m_location = location_list[0]
	for i in range(1, len(location_list)):
		y_location += '+'+location_list[i]
		m_location += '-'+location_list[i]

	print 'y_location', y_location
	print 'm_location', m_location

	food_list = food.split(' ')
	y_food = food_list[0]
	m_food = food_list[0]
	for i in range(1, len(food_list)):
		y_food += '+'+food_list[i]
		m_food += '%20'+food_list[i]

	#will transfer website's data to textfiles to be parsed
	yelp.yelp(y_location, y_food)
	print 'yelp'
	menupages.menupages(m_location, m_food)
	print 'menupages'

	#parsing the textfiles into lists
	yelp_list = retriever.retrieve_yelp()
	print 'yelp_list', yelp_list
	menupages_list = retriever.retrieve_menupages()
	print 'menus list', menupages_list

	#returns one big list of both inputs
	final_list = yelp_list + menupages_list
'''
'''
def main(zipcode, food):

	while True:
		location = zc.main(zipcode)
		my_str = menupages.menupages(location, food)
		if my_str == 'Company unfound':
			zipcode += 1
			continue

	menupages_list = retriever.retrieve_menupages()

	return menupages_list
'''

def main(zipcode, food):
	location = zc.main(zipcode)

	my_str = menupages.menupages(location, food)
	i = 1
	boolean = True
	new_zip = zipcode
	while my_str == 'Company unfound':
		if boolean:
			new_zip = zipcode + i
			boolean = False
		else:
			new_zip = zipcode - i
			boolean = True
			i += 1

		print new_zip
		location = zc.main(new_zip)
		if location != '':
			my_str = menupages.menupages(location, food)

	menupages_list = retriever.retrieve_menupages()

	for i in range(len(menupages_list)):
		temp = menupages_list[i].split('\r\n')
		print temp
		menupages_list[i] = temp[0]

	for i in range(len(menupages_list)/2):
		a = 2*i+1
		temp = menupages_list[a].split('|')
		ave_list = temp[0].split(' ')
		street_list = temp[1].split(' ')
		
		#174 Avenue B | At 11th St

		address = ave_list[0]+' '+street_list[2]+' St, '+ave_list[1]+' '+ave_list[2]
		menupages_list[a] = address

	return menupages_list


print main(10002, 'burger')
