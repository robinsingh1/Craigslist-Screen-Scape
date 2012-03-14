def four():

	file = open('clean_emails.txt', 'r')
	final = open('final_emails.txt', 'w')
	emails = []


	for line in file.readlines():
		x = 1
		
		if line != "":
			for email in emails:
				if line == email:
					x = 0
					break
			if x:
				final.write(line+"\n")
				emails.append(line)
			
		
	print "four"