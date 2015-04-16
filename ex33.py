#def for function using while block
def display_loop_contents(ctr, inr):
	i = 0
	numbers = [] 
	while i < ctr:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i = i + inr
		print "Numbers now: " , numbers
		print "At the bottom i is %d" % i 

	print "The numbers: "

	for num in numbers:
		print num
#def for checking StackSize
def sizeChk(ctr, inr):
	if ctr < 40:
		if inr < 10:
			display_loop_contents(ctr, inr)
		else:
			print "You entered a starting number that is out of range"	
	else:
		print "You entered a incrementer number that is out of range"

#def for take input from user
def TakeInputStr1():	
	print "Enter any number between less than 40 to start the Stack"
	counter = int(raw_input())
	return counter
#def for take input from user
def TakeInputStr2():	
	print "Enter any number between 1 to 10 for the incrementer"
	incr = int(raw_input())	
	return incr
ctr = TakeInputStr1()	
inr = TakeInputStr2()	
sizeChk(ctr, inr) 

