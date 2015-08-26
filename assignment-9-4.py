# 9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

# Desired Output
# cwen@iupui.edu 5

name = raw_input("Enter file: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
emails = list()

# Search at each line the email and put it in a list 'emails'
for line in handle:
	if not line.startswith('From ') : continue
	words = line.split()
	emails.append(words[1])

# Account emails
for email in emails:
	counts[email] = counts.get(email,0) + 1

# Get the email with the maximum number of times
email_value = 0
for key,value in counts.items():
	if value > email_value:
		email_key = key
		email_value = value

print email_key, email_value
