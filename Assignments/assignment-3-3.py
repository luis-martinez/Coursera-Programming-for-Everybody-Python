# 3.3 Write a program to prompt the user for a score using raw_input. Print out a letter grade based on the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

# Desired Output
# B

s = raw_input("What is your score: ")
score = float(s)


try:
	if score >= 0.9:
		print "A"
	elif score >= 0.8:
		print "B"
	elif score >= 0.7:
		print "C"
	elif score >= 0.6:
		print "D"
	elif score < 0.6:
		print "F"
	else:
		print "Error, value out of range"
except:
	print "Error, value out of rangeee"
