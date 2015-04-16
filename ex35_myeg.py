import random

def Class_Genre():
	print "This is the eternal debenture of music."
	print " This has several divisions - Medieval, Renaissance, Baroque to name a few."
	print "Type any division that you like"
	choice = raw_input("> ") 
	if choice == "Medieval":
		print("Madrigals, Canons, Ballata fall into this unit.")
	elif choice =="Renaissance":
		print("Masses, motets, Operas are enjoyed popularly during this time.")
	elif choice =="Baroque":
		print("This phase has established opera, cantata, oratorio, concerto and sonata as musical genres.")
	else:
		print "I'd not know what you have entered! Please check!"
		
def Play_Game():
	print "You will now play a  game."
				
def roll_dice():
	min = 1
	max = 12
	
	roll_again ="yes"

	while roll_again == "yes":
		print "Rolling the dices..."
		print "The value is....."
		print random.randint(min, max)
		return random.randint(min, max)	
	
def dead(str):
		print str, "Good Job!"
		exit(0)
		
def start():
	print " This is the right thing you can do now!"
	print "Starting the game"
	print "Enter your response"
	select = raw_input("> ")
	
	print "Entering the Music-Disc"
	if select == "yes" or "ye" or "y" or "no" or "n":
		dice = roll_dice()
	else:
		dead("Type your response in simple language!")	

	if dice % 3 == 2 :
		Class_Genre()
	elif dice % 3 == 1:
		Play_Game()
	elif dice % 3 == 0:
		dead("You got unlucky this time! Try again")
	else:
		dead("You have entered an incorrect number.")
		
start()
		