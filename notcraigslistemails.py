file = open('ncl.txt', 'w')
emails = open('final_emails.txt', 'r')

for line in emails.readlines():
    number = line.find('@craigslist')
    if (number == -1):
        file.write(line)
