def one():
        import urllib
        emails = open('urls.txt', 'w')

        for i in range(21):
                if (i == 0):
                        content = urllib.urlopen("http://toronto.en.craigslist.ca/mar/")
                else:
                        content = urllib.urlopen("http://toronto.en.craigslist.ca/mar/index"+str(i)+"00.html")
                        print i
                for line in content.readlines():
                        number = line.find('href="')
                        if (number != -1):
                                part=line.split('"')
#                                print (part[1] + "\n")
                                emails.write(part[1]+"\n")
		print "one"