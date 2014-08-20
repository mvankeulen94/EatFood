import re
#returns the names from yelp and menupages and returns the location

#STUFF THAT COULD GO WRONG
#what if menupages doesn't have shit
#what if they both have the same restaurants?
	# then move it up on the list


top_number = 3 #top number of restaurants

def retrieve_yelp():
	''' retrieves top restaurants from yelp text file.'''

	global top_number

	infile = open('yelp_page.txt', 'r')

	word = 'Reviews on '

	answer = []

	for line in infile:
		if word in line:
			line_list = line.split("   ")
			line_list = line_list[1] #this is the actual list of restaurants
			restaurants = line_list.split(",")

			#getting top restaurants
			for i in range(top_number):
				answer.append(restaurants[i])

	infile.close()

	for i in range(len(answer)):
		answer[i] = answer[i].strip(' ')


	#try to optimize this--no I/O twice
	infile = open('yelp_page.txt', 'r')


	address_list = []
	# obtaining addresses
	for elements in answer:
		elements_list = elements.split(' ')
		keyword = '<img alt="'+elements[0]+elements[1] # used to search for address
		#print keyword

		#finding the right line
		line = infile.readline()
		while re.search(keyword, line) == None:
			line = infile.readline()

		#finding the line of the address
		while re.search('<address>', line) == None:
			line = infile.readline()

		#reformatting address
		address = infile.readline().strip('\t')
		address_list2 = address.split('<br>')
		address = ""
		for item in address_list2:
			address += item + ', '
		#print 'address:', address
		address_list.append(address)
		#print 'address_list0', address_list

	infile.close()
	#print 'address_list', address_list


	#inserting addresses back into original list
	for i in range(len(answer)):
		answer.insert(2*(i)+1, address_list[i])
		
	return answer

def retrieve_menupages():
	''' retrieves top restaurants from menupages textfile.'''

	infile = open('menupages_page.txt', 'r')

	global top_number

	answer = []

	for i in range(top_number):
		#search keywords for restaurants
		word = "marker1['"+str(i+1)+"']"

		go_on = True #whether or not to break for loop

		#searching the file
		line = infile.readline()
		while (word not in line):
			if "</html>" in line:
				go_on = False
				break
			line = infile.readline()
		if go_on == False:
			break

		#skip to the actual title
		word = "title"
		while word not in line:
			if "</html>" in line:
				go_on == False
				break
			line = infile.readline() #actual line

		if go_on == False:
			break

		line_list = line.split(":")
		answer.append(line_list[1].strip('\n').strip("'"))

	infile.close()

	# looking for address
	infile = open('menupages_page.txt', 'r')
	address_list = []
	for elements in answer:
		keyword = "</span>"+elements[0]+elements[1]

		#finding correct line
		line = infile.readline()
		while re.search(keyword, line) == None:
			line = infile.readline()

		line_list = line.split('</a>')
		address = line_list[1]
		address_list.append(address)

	#inserting addresses back in to answer list
	for i in range(len(answer)):
		answer.insert(2*i+1, address_list[i])

	infile.close()
	return answer

#print retrieve_menupages()
