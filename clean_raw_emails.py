def three():
	file = open('cl_emails.txt', 'r')
	clean = open('clean_emails.txt', 'w')

	for line in file.readlines():
		if line.find(":") != -1:
			segment = line.split(":")
			part = segment[1]
			if part.find("?subject") != -1:
				s1 = part.split("?subject")
				email = s1[0]
				clean.write(email + "\n")
		elif line.find("<br>"):
			cleaner = line.split("<br>")
			clean.write(cleaner[0] + "\n")
		else :
			clean.write(line + "\n")
	print "three"