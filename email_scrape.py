def two():

	import urllib

	file = open('urls.txt', 'r')
	emails = open('cl_emails.txt', 'w')

	for url in file.readlines():
		if url.find("http://toronto") != -1:
			url = urllib.urlopen(url)
			for line in url.readlines():
				place = line.find("@")
				if place != -1:
						words = line.split(" ")
						for word in words:
							if word.find("@") != -1:
									emails.write(word + "\n")
      
            
            
            

	print "two"
