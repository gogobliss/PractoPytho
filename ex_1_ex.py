
def add(a, b):
	return a + b;

def divide(a, b):
	return a / b;

from sys import argv
script, user_name = argv
prompt = ' > '

print "Hi %s, I'm the  %s script." %(user_name, script)
print "I would like to ask few questions."
print "Enter two numbers for Numerator" 
nr1 = float( raw_input(prompt) )
nr2 = float( raw_input(prompt) )

nr = add(nr1, nr2)

print "Enter two numbers for Denominator" 
dr1 = float( raw_input(prompt) )
dr2 = float( raw_input(prompt) )

dr = add(dr1, dr2)
fr = divide(nr, dr)

print "You have given this data  - as Nr : %s and %s , as Dr : %s and %s" %(nr1, nr2, dr1, dr2)
print " This is the value after the computation %s" %(fr)


