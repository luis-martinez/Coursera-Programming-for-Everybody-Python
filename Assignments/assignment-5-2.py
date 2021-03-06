# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter the numbers from the book for problem 5.1 and Match the desired output as shown.

# Desired Output

# Invalid input
# Maximum is 7
# Minimum is 4 

largest = None
smallest = None

while True:
	try:
		n = raw_input("Enter a number: ")
		num = int(n)
		if largest is None:
			largest = num
		if smallest is None:
			smallest = num
		if num < smallest:
			smallest = num
		if num > largest:
			largest = num
		#print "Minimum iss ", smallest
		#print "Maximum iss ", largest
	except ValueError:
		if n == "done":
			break
		else:
			print "Invalid input"	

print "Maximum is", largest    
print "Minimum is", smallest
