file = open('cl.txt', 'r')
emails = open('email.txt', 'w')

for line in file.readlines():
    number = line.find('href="')
    if (number != -1):
        part=line.split('"')
        emails.write(part[1]+"\n")

