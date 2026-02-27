########################################################
#### Innovation.py                                  ####
#### Program to play the game Innovation in Python. ####
#### Started 05/08/19 by Alex Spacek                ####
#### Last edited 02/23/26 by Alex Spacek            ####
########################################################

#############
## IMPORTS ##
#############

## RANDOM
# Used to make random choices
import random
## SHUFFLE
# Also used to "shuffle" the cards
# > shuffle(array)
from random import shuffle

###########
## NOTES ##
###########

## For now, playing with a simple deck.
## For Age 1, it is 3 copies of 3 cards.
# Age 1 - Archery
# Age 1 - ArcheryX
# Age 1 - ArcheryXX
# Age 1 - Metalworking
# Age 1 - MetalworkingX
# Age 1 - MetalworkingXX
# Age 1 - Oars
# Age 1 - OarsX
# Age 1 - OarsXX
## For Ages 2-4, it is 2 copies of the above cards.
# Age 2 - Archery2
# Age 2 - Archery2X
# Age 2 - Metalworking2
# Age 2 - Metalworking2X
# Age 2 - Oars2
# Age 2 - Oars2X
# Age 3 - Archery3
# Age 3 - Archery3X
# Age 3 - Metalworking3
# Age 3 - Metalworking3X
# Age 3 - Oars3
# Age 3 - Oars3X
# Age 4 - Archery4
# Age 4 - Archery4X
# Age 4 - Metalworking4
# Age 4 - Metalworking4X
# Age 4 - Oars4
# Age 4 - Oars4X

## The overall multi-dimensional array is thedeck
## The cards are located at:
# thedeck.a1[0-8].name = ["Archery","ArcheryX","ArcheryXX",...,"OarsX","OarsXX"]
# thedeck.a2[0-5].name = ["Archery2","Archery2X","Metalworking2",...,"Oars2","Oars2X"]
# thedeck.a3[0-5].name = ["Archery3","Archery3X","Metalworking3",...,"Oars3","Oars3X"]
# thedeck.a4[0-5].name = ["Archery4","Archery4X","Metalworking4",...,"Oars4","Oars4X"]

###############
## FUNCTIONS ##
###############

###########
## ACTIVATE
###########
# Function to play a card.
# Input:
#   thedeck (arr) - the multi-dimensional array of all deck info
#   who (str) - "p1", "p2"
#     p1 - Player 1
#     p2 - Player 2
# Output:
#   nothing (null)
# Possible ways to call this function:
#   activate(thedeck,"p1") - will ask Player 1 to pick a card from their field to activate
#   activate(thedeck,"p2") - will pick a random card from Player 2's field to activate
##########################
def activate(thedeck,who):
	# Count the total symbols for each player:
	# Call "symbolcount" to do it:
	symbolarr = symbolcount(thedeck)
	# Organize the output:
	p1bulb = symbolarr[0]
	p2bulb = symbolarr[1]
	p1castle = symbolarr[2]
	p2castle = symbolarr[3]
	p1crown = symbolarr[4]
	p2crown = symbolarr[5]
	# Print results:
	print("\np1bulb = "+str(p1bulb))
	print("p2bulb = "+str(p2bulb))
	print("\np1castle = "+str(p1castle))
	print("p2castle = "+str(p2castle))
	print("\np1crown = "+str(p1crown))
	print("p2crown = "+str(p2crown))
	# If Player 1 is activating:
	if who == "p1":
		# Get the length of the Age arrays:
		# Call "lengths" to do it:
		# 0 = don't print the info
		lengtharr = lengths(thedeck,0)
		# Organize the output:
		tota1len = lengtharr[0]
		tota2len = lengtharr[1]
		tota3len = lengtharr[2]
		tota4len = lengtharr[3]
		# Grab the locations of Player 1's cards:
		# Initialize the arrays:
		p1a1fieldloc = []
		p1a2fieldloc = []
		p1a3fieldloc = []
		p1a4fieldloc = []
		agearr = []
		# Run through Age 1
		for i in range(tota1len):
			# If the card is on top of Player 1 field pile:
			if thedeck.a1[i].location == "p1field" and thedeck.a1[i].place == 1:
				# Record the location:
				p1a1fieldloc = p1a1fieldloc+[i]
				# Record the Age:
				agearr = agearr+[1]
		# Run through Age 2
		for i in range(tota2len):
			# If the card is on top of Player 1 field pile:
			if thedeck.a2[i].location == "p1field" and thedeck.a2[i].place == 1:
				# Record the location:
				p1a2fieldloc = p1a2fieldloc+[i]
				# Record the Age:
				agearr = agearr+[2]
		# Run through Age 3
		for i in range(tota3len):
			# If the card is on top of Player 1 field pile:
			if thedeck.a3[i].location == "p1field" and thedeck.a3[i].place == 1:
				# Record the location:
				p1a3fieldloc = p1a3fieldloc+[i]
				# Record the Age:
				agearr = agearr+[3]
		# Run through Age 4
		for i in range(tota4len):
			# If the card is on top of Player 1 field pile:
			if thedeck.a4[i].location == "p1field" and thedeck.a4[i].place == 1:
				# Record the location:
				p1a4fieldloc = p1a4fieldloc+[i]
				# Record the Age:
				agearr = agearr+[4]
		# Ask for choice:
		flag = 0
		while flag == 0:
			print("\nPlayer 1 field:")
			n = 1
			print("Red")
			# Age 1
			for i in range(len(p1a1fieldloc)):
				if thedeck.a1[p1a1fieldloc[i]].color == "red":
					print(str(n)+" - "+thedeck.a1[p1a1fieldloc[i]].name)
					n = n+1
			# Age 2
			for i in range(len(p1a2fieldloc)):
				if thedeck.a2[p1a2fieldloc[i]].color == "red":
					print(str(n)+" - "+thedeck.a2[p1a2fieldloc[i]].name)
					n = n+1
			# Age 3
			for i in range(len(p1a3fieldloc)):
				if thedeck.a3[p1a3fieldloc[i]].color == "red":
					print(str(n)+" - "+thedeck.a3[p1a3fieldloc[i]].name)
					n = n+1
			# Age 4
			for i in range(len(p1a4fieldloc)):
				if thedeck.a4[p1a4fieldloc[i]].color == "red":
					print(str(n)+" - "+thedeck.a4[p1a4fieldloc[i]].name)
					n = n+1
			p1choice = input("\nChoose a card to activate, or enter 0 to check game info: ")
			if p1choice == "0":
				print("\n0 - Hand info")
				print("1 - Field info")
				p1infochoice = input("\n")
				if p1infochoice == "0":
					cardinfo(thedeck,"p1hand")
				elif p1infochoice == "1":
					print("\nPlayer 1 field:")
					cardinfo(thedeck,"p1field")
					print("\nPlayer 2 field:")
					cardinfo(thedeck,"p2field")
					print("\nAvailable age piles:")
					cardinfo(thedeck,"deck")
			elif int(p1choice) < n:
				flag = 1
				a1count = 0
				a2count = 0
				a3count = 0
				a4count = 0
				for i in range(len(agearr)):
					if agearr[i] == 1:
						a1count = a1count + 1
					elif agearr[i] == 2:
						a2count = a2count + 1
					elif agearr[i] == 3:
						a3count = a3count + 1
					elif agearr[i] == 4:
						a4count = a4count + 1
				if agearr[int(p1choice)-1] == 1:
					print("\nYou have chosen to activate "+thedeck.a1[p1a1fieldloc[int(p1choice)-1]].name)
				elif agearr[int(p1choice)-1] == 2:
					print("\nYou have chosen to activate "+thedeck.a2[p1a2fieldloc[int(p1choice)-1-a1count]].name)
				elif agearr[int(p1choice)-1] == 3:
					print("\nYou have chosen to activate "+thedeck.a3[p1a3fieldloc[int(p1choice)-1-a1count-a2count]].name)
				elif agearr[int(p1choice)-1] == 4:
					print("\nYou have chosen to activate "+thedeck.a4[p1a4fieldloc[int(p1choice)-1-a1count-a2count-a3count]].name)
			else:
				print("\nNot a valid choice.")
	# If Player 2 is activating:
	elif who == "p2":
		# Get the length of the Age arrays:
		# Call "lengths" to do it:
		# 0 = don't print the info
		lengtharr = lengths(thedeck,0)
		# Organize the output:
		tota1len = lengtharr[0]
		tota2len = lengtharr[1]
		tota3len = lengtharr[2]
		tota4len = lengtharr[3]
		# Grab the locations of Player 2's cards:
		# Initialize the arrays:
		p2a1fieldloc = []
		p2a2fieldloc = []
		p2a3fieldloc = []
		p2a4fieldloc = []
		agearr = []
		# Run through Age 1
		for i in range(tota1len):
			# If the card is on top of Player 2 field pile:
			if thedeck.a1[i].location == "p2field" and thedeck.a1[i].place == 1:
				# Record the location:
				p2a1fieldloc = p2a1fieldloc+[i]
				# Record the Age:
				agearr = agearr+[1]
		# Run through Age 2
		for i in range(tota2len):
			# If the card is on top of Player 2 field pile:
			if thedeck.a2[i].location == "p2field" and thedeck.a1[i].place == 1:
				# Record the location:
				p2a2fieldloc = p2a2fieldloc+[i]
				# Record the Age:
				agearr = agearr+[2]
		# Run through Age 3
		for i in range(tota3len):
			# If the card is on top of Player 2 field pile:
			if thedeck.a3[i].location == "p2field" and thedeck.a1[i].place == 1:
				# Record the location:
				p2a3fieldloc = p2a3fieldloc+[i]
				# Record the Age:
				agearr = agearr+[3]
		# Run through Age 4
		for i in range(tota4len):
			# If the card is on top of Player 2 field pile:
			if thedeck.a4[i].location == "p2field" and thedeck.a1[i].place == 1:
				# Record the location:
				p2a4fieldloc = p2a4fieldloc+[i]
				# Record the Age:
				agearr = agearr+[4]
		# Pick a random card from field to play:
		flag = 0
		while flag == 0:
			n = 1
			for i in range(len(p2a1fieldloc)):
				n = n+1
			for i in range(len(p2a2fieldloc)):
				n = n+1
			for i in range(len(p2a3fieldloc)):
				n = n+1
			for i in range(len(p2a4fieldloc)):
				n = n+1
			randarray = []
			for i in range(n-1):
				randarray = randarray+[i+1]
			p2choice = random.choice(randarray)
			if int(p2choice) < n:
				flag = 1
				a1count = 0
				a2count = 0
				a3count = 0
				a4count = 0
				for i in range(len(agearr)):
					if agearr[i] == 1:
						a1count = a1count + 1
					elif agearr[i] == 2:
						a2count = a2count + 1
					elif agearr[i] == 3:
						a3count = a3count + 1
					elif agearr[i] == 4:
						a4count = a4count + 1
				if agearr[int(p2choice)-1] == 1:
					print("\nPlayer 2 has chosen to activate "+thedeck.a1[p2a1fieldloc[int(p2choice)-1]].name)
				elif agearr[int(p2choice)-1] == 2:
					print("\nPlayer 2 has chosen to activate "+thedeck.a2[p2a2fieldloc[int(p2choice)-1-a1count]].name)
				elif agearr[int(p2choice)-1] == 3:
					print("\nPlayer 2 has chosen to activate "+thedeck.a3[p2a3fieldloc[int(p2choice)-1-a1count-a2count]].name)
				elif agearr[int(p2choice)-1] == 4:
					print("\nPlayer 2 has chosen to activate "+thedeck.a4[p2a4fieldloc[int(p2choice)-1-a1count-a2count-a3count]].name)
			else:
				print("\nNot a valid choice.")

##############
## CARDEFFECTS
##############
# Function to activate the effects of a specific card.
# Input:
#   thedeck (arr) - the multi-dimensional array of all deck info
#   who (str) - "p1", "p2"
#     p1 - Player 1
#     p2 - Player 2
#   cardname (str) - "Archery", "Metalworking", "Oars"
# Output:
#   nothing (null)
# Possible ways to call this function:
#   cardeffects(thedeck,"p1","Archery") - Player 1 is activating Archery
#   cardeffects(thedeck,"p2","Archery") - Player 2 is activating Archery
#   etc.
######################################
def cardeffects(thedeck,who,cardname):
	# Count the total symbols for each player:
	# Call "symbolcount" to do it:
	symbolarr = symbolcount(thedeck)
	# Organize the output:
	p1bulb = symbolarr[0]
	p2bulb = symbolarr[1]
	p1castle = symbolarr[2]
	p2castle = symbolarr[3]
	p1crown = symbolarr[4]
	p2crown = symbolarr[5]
	# Archery - Red
	# Demand - Castle - "I demand you draw a [1], then transfer the highest card in your hand to my hand!"
	if cardname == "Archery":
		if who == "p1":
			if p2castle >= p1castle:
				print("\nPlayer 2 does not have less Castle than Player 1, so the Archery Demand does not apply.")
			else:
				print("\nPlayer 1 demands Player 2 draws a [1], then transfers the highest card from their hand to Player 1's hand.")
		elif who == "p2":
			if p1castle >= p2castle:
				print("\nPlayer 1 does not have less Castle than Player 2, so the Archery Demand does not apply.")
			else:
				print("\nPlayer 2 demands Player 1 draws a [1], then transfers the highest card from their hand to Player 2's hand.")
	# Metalworking - Red
	# Coop - Castle - "Draw and reveal a [1]. If it has a [castle], score it and repeat this dogma effect. Otherwise, keep it."
	elif cardname == "Metalworking":
	
	# Oars - Red
	# Demand - Castle - "I demand you transfer a card with a [crown] from your hand to my score pile! If you do, draw a [1]."
	# Coop - Castle - "If no cards were transferred due to this demand, draw a [1]."
	elif cardname == "Oars":


## CARDINFO
# Function to show card info
# Input:
#   thedeck (arr) - the multi-dimensional array of all deck info
#   what (str) - "p1hand", "p1field", "p2field", "deck"
#     p1hand (str) - Player 1 (p1) hand
#     p1field (str) - Player 1 (p1) field (cards in play)
#     p2field (str) - Player 2 (p2) field (cards in play)
#     deck (str) - show info about available Age piles
# Output:
#   nothing (null) - print out requested info
def cardinfo(thedeck,what):
	if what == "p1hand":
		# Get then length of each Age array:
		a1len = len(thedeck.a1)
		a2len = len(thedeck.a2)
		a3len = len(thedeck.a3)
		a4len = len(thedeck.a4)
		# Show the info of the p1hand cards:
		for i in range(a1len):
			if thedeck.a1[i].location == "p1hand":
				print("\n***********************")
				print(thedeck.a1[i].name)
				print("Age = "+str(thedeck.a1[i].age))
				print("Color = "+thedeck.a1[i].color)
				print("-----")
				print("|"+thedeck.a1[i].syms.ul)
				print("|"+thedeck.a1[i].syms.dl+"   "+thedeck.a1[i].syms.dm+"   "+thedeck.a1[i].syms.dr)
				print("-----")
				print(thedeck.a1[i].effect1.cost+" - "+thedeck.a1[i].effect1.type+" - "+thedeck.a1[i].effect1.text)
				if thedeck.a1[i].effect2.text != "":
					print(thedeck.a1[i].effect2.cost+" - "+thedeck.a1[i].effect2.type+" - "+thedeck.a1[i].effect2.text)
				print("***********************")
		for i in range(a2len):
			if thedeck.a2[i].location == "p1hand":
				print("\n***********************")
				print(thedeck.a2[i].name)
				print("Age = "+str(thedeck.a2[i].age))
				print("Color = "+thedeck.a2[i].color)
				print(thedeck.a2[i].syms.ul)
				print(thedeck.a2[i].syms.dl+"   "+thedeck.a2[i].syms.dm+"   "+thedeck.a2[i].syms.dr)
				print(thedeck.a2[i].effect1.cost+" - "+thedeck.a2[i].effect1.type+" - "+thedeck.a2[i].effect1.text)
				if thedeck.a2[i].effect2.text != "":
					print(thedeck.a2[i].effect2.cost+" - "+thedeck.a2[i].effect2.type+" - "+thedeck.a2[i].effect2.text)
				print("***********************")
		for i in range(a3len):
			if thedeck.a3[i].location == "p1hand":
				print("\n***********************")
				print(thedeck.a3[i].name)
				print("Age = "+str(thedeck.a3[i].age))
				print("Color = "+thedeck.a3[i].color)
				print(thedeck.a3[i].syms.ul)
				print(thedeck.a3[i].syms.dl+"   "+thedeck.a3[i].syms.dm+"   "+thedeck.a3[i].syms.dr)
				print(thedeck.a3[i].effect1.cost+" - "+thedeck.a3[i].effect1.type+" - "+thedeck.a3[i].effect1.text)
				if thedeck.a3[i].effect2.text != "":
					print(thedeck.a2[i].effect2.cost+" - "+thedeck.a2[i].effect2.type+" - "+thedeck.a2[i].effect2.text)
				print("***********************")
		for i in range(a4len):
			if thedeck.a4[i].location == "p1hand":
				print("\n***********************")
				print(thedeck.a4[i].name)
				print("Age = "+str(thedeck.a4[i].age))
				print("Color = "+thedeck.a4[i].color)
				print(thedeck.a4[i].syms.ul)
				print(thedeck.a4[i].syms.dl+"   "+thedeck.a4[i].syms.dm+"   "+thedeck.a4[i].syms.dr)
				print(thedeck.a4[i].effect1.cost+" - "+thedeck.a4[i].effect1.type+" - "+thedeck.a4[i].effect1.text)
				if thedeck.a4[i].effect2.text != "":
					print(thedeck.a2[i].effect2.cost+" - "+thedeck.a2[i].effect2.type+" - "+thedeck.a2[i].effect2.text)
				print("***********************")
	elif what == "p1field":
		# Get then length of each Age array:
		a1len = len(thedeck.a1)
		a2len = len(thedeck.a2)
		a3len = len(thedeck.a3)
		a4len = len(thedeck.a4)
		# Show the info of the p1field cards:
		for i in range(a1len):
			if thedeck.a1[i].location == "p1field" and thedeck.a1[i].place == 1:
				print("\n***********************")
				print(thedeck.a1[i].name)
				print("Age = "+str(thedeck.a1[i].age))
				print("Color = "+thedeck.a1[i].color)
				print("-----")
				print("|"+thedeck.a1[i].syms.ul)
				print("|"+thedeck.a1[i].syms.dl+"   "+thedeck.a1[i].syms.dm+"   "+thedeck.a1[i].syms.dr)
				print("-----")
				print(thedeck.a1[i].effect1.cost+" - "+thedeck.a1[i].effect1.type+" - "+thedeck.a1[i].effect1.text)
				if thedeck.a1[i].effect2.text != "":
					print(thedeck.a1[i].effect2.cost+" - "+thedeck.a1[i].effect2.type+" - "+thedeck.a1[i].effect2.text)
				print("***********************")
		for i in range(a2len):
			if thedeck.a2[i].location == "p1field" and thedeck.a2[i].place == 1:
				print("\n***********************")
				print(thedeck.a2[i].name)
				print("Age = "+str(thedeck.a2[i].age))
				print("Color = "+thedeck.a2[i].color)
				print(thedeck.a2[i].syms.ul)
				print(thedeck.a2[i].syms.dl+"   "+thedeck.a2[i].syms.dm+"   "+thedeck.a2[i].syms.dr)
				print(thedeck.a2[i].effect1.cost+" - "+thedeck.a2[i].effect1.type+" - "+thedeck.a2[i].effect1.text)
				if thedeck.a2[i].effect2.text != "":
					print(thedeck.a2[i].effect2.cost+" - "+thedeck.a2[i].effect2.type+" - "+thedeck.a2[i].effect2.text)
				print("***********************")
		for i in range(a3len):
			if thedeck.a3[i].location == "p1field" and thedeck.a3[i].place == 1:
				print("\n***********************")
				print(thedeck.a3[i].name)
				print("Age = "+str(thedeck.a3[i].age))
				print("Color = "+thedeck.a3[i].color)
				print(thedeck.a3[i].syms.ul)
				print(thedeck.a3[i].syms.dl+"   "+thedeck.a3[i].syms.dm+"   "+thedeck.a3[i].syms.dr)
				print(thedeck.a3[i].effect1.cost+" - "+thedeck.a3[i].effect1.type+" - "+thedeck.a3[i].effect1.text)
				if thedeck.a3[i].effect2.text != "":
					print(thedeck.a2[i].effect2.cost+" - "+thedeck.a2[i].effect2.type+" - "+thedeck.a2[i].effect2.text)
				print("***********************")
		for i in range(a4len):
			if thedeck.a4[i].location == "p1field" and thedeck.a4[i].place == 1:
				print("\n***********************")
				print(thedeck.a4[i].name)
				print("Age = "+str(thedeck.a4[i].age))
				print("Color = "+thedeck.a4[i].color)
				print(thedeck.a4[i].syms.ul)
				print(thedeck.a4[i].syms.dl+"   "+thedeck.a4[i].syms.dm+"   "+thedeck.a4[i].syms.dr)
				print(thedeck.a4[i].effect1.cost+" - "+thedeck.a4[i].effect1.type+" - "+thedeck.a4[i].effect1.text)
				if thedeck.a4[i].effect2.text != "":
					print(thedeck.a2[i].effect2.cost+" - "+thedeck.a2[i].effect2.type+" - "+thedeck.a2[i].effect2.text)
				print("***********************")
	elif what == "p2field":
		# Get then length of each Age array:
		a1len = len(thedeck.a1)
		a2len = len(thedeck.a2)
		a3len = len(thedeck.a3)
		a4len = len(thedeck.a4)
		# Show the info of the p1field cards:
		for i in range(a1len):
			if thedeck.a1[i].location == "p2field" and thedeck.a1[i].place == 1:
				print("\n***********************")
				print(thedeck.a1[i].name)
				print("Age = "+str(thedeck.a1[i].age))
				print("Color = "+thedeck.a1[i].color)
				print("-----")
				print("|"+thedeck.a1[i].syms.ul)
				print("|"+thedeck.a1[i].syms.dl+"   "+thedeck.a1[i].syms.dm+"   "+thedeck.a1[i].syms.dr)
				print("-----")
				print(thedeck.a1[i].effect1.cost+" - "+thedeck.a1[i].effect1.type+" - "+thedeck.a1[i].effect1.text)
				if thedeck.a1[i].effect2.text != "":
					print(thedeck.a1[i].effect2.cost+" - "+thedeck.a1[i].effect2.type+" - "+thedeck.a1[i].effect2.text)
				print("***********************")
		for i in range(a2len):
			if thedeck.a2[i].location == "p2field" and thedeck.a2[i].place == 1:
				print("\n***********************")
				print(thedeck.a2[i].name)
				print("Age = "+str(thedeck.a2[i].age))
				print("Color = "+thedeck.a2[i].color)
				print(thedeck.a2[i].syms.ul)
				print(thedeck.a2[i].syms.dl+"   "+thedeck.a2[i].syms.dm+"   "+thedeck.a2[i].syms.dr)
				print(thedeck.a2[i].effect1.cost+" - "+thedeck.a2[i].effect1.type+" - "+thedeck.a2[i].effect1.text)
				if thedeck.a2[i].effect2.text != "":
					print(thedeck.a2[i].effect2.cost+" - "+thedeck.a2[i].effect2.type+" - "+thedeck.a2[i].effect2.text)
				print("***********************")
		for i in range(a3len):
			if thedeck.a3[i].location == "p2field" and thedeck.a3[i].place == 1:
				print("\n***********************")
				print(thedeck.a3[i].name)
				print("Age = "+str(thedeck.a3[i].age))
				print("Color = "+thedeck.a3[i].color)
				print(thedeck.a3[i].syms.ul)
				print(thedeck.a3[i].syms.dl+"   "+thedeck.a3[i].syms.dm+"   "+thedeck.a3[i].syms.dr)
				print(thedeck.a3[i].effect1.cost+" - "+thedeck.a3[i].effect1.type+" - "+thedeck.a3[i].effect1.text)
				if thedeck.a3[i].effect2.text != "":
					print(thedeck.a2[i].effect2.cost+" - "+thedeck.a2[i].effect2.type+" - "+thedeck.a2[i].effect2.text)
				print("***********************")
		for i in range(a4len):
			if thedeck.a4[i].location == "p2field" and thedeck.a4[i].place == 1:
				print("\n***********************")
				print(thedeck.a4[i].name)
				print("Age = "+str(thedeck.a4[i].age))
				print("Color = "+thedeck.a4[i].color)
				print(thedeck.a4[i].syms.ul)
				print(thedeck.a4[i].syms.dl+"   "+thedeck.a4[i].syms.dm+"   "+thedeck.a4[i].syms.dr)
				print(thedeck.a4[i].effect1.cost+" - "+thedeck.a4[i].effect1.type+" - "+thedeck.a4[i].effect1.text)
				if thedeck.a4[i].effect2.text != "":
					print(thedeck.a2[i].effect2.cost+" - "+thedeck.a2[i].effect2.type+" - "+thedeck.a2[i].effect2.text)
				print("***********************")
	elif what == "deck":
		# Get then length of each Age array:
		a1len = len(thedeck.a1)
		a2len = len(thedeck.a2)
		a3len = len(thedeck.a3)
		a4len = len(thedeck.a4)
		# Show the available deck piles:
		piles = ""
		flag = 0
		for i in range(a1len):
			if thedeck.a1[i].location == "deck":
				piles = piles+"1 "
				flag = 1
		if flag == 0:
			piles = piles+"- "
		flag = 0
		for i in range(a2len):
			if thedeck.a2[i].location == "deck":
				piles = piles+"2 "
				flag = 1
		if flag == 0:
			piles = piles+"- "
		flag = 0
		for i in range(a3len):
			if thedeck.a3[i].location == "deck":
				piles = piles+"3 "
				flag = 1
		if flag == 0:
			piles = piles+"- "
		flag = 0
		for i in range(a4len):
			if thedeck.a4[i].location == "deck":
				piles = piles+"4 "
				flag = 1
		if flag == 0:
			piles = piles+"- "

## DRAW
# Function to draw a card
# Input:
#   thedeck (arr) - the multi-dimensional array of all deck info
#   who (str) - "p1", "p2"
#     p1 - Player 1
#     p2 - Player 2
# Output:
#   nothing (null)
def draw(thedeck,who):
	# End of game flag:
	gameover = 0
	# Check the highest age in both fields:
	lengtharr = lengths(thedeck,0)
	tota1len = lengtharr[0]
	tota2len = lengtharr[1]
	tota3len = lengtharr[2]
	tota4len = lengtharr[3]
	a1decklen = lengtharr[13]
	a2decklen = lengtharr[14]
	a3decklen = lengtharr[15]
	a4decklen = lengtharr[16]
	p1max = 1
	p2max = 1
	for i in range(tota4len):
		if thedeck.a4[i].place == 1:
			if thedeck.a4[i].location == "p1field":
				p1max = 4
			if thedeck.a4[i].location == "p2field":
				p2max = 4
	for i in range(tota3len):
		if thedeck.a3[i].place == 1:
			if thedeck.a3[i].location == "p1field" and p1max < 3:
				p1max = 3
			if thedeck.a3[i].location == "p2field" and p2max < 3:
				p2max = 3
	for i in range(tota2len):
		if thedeck.a2[i].place == 1:
			if thedeck.a2[i].location == "p1field" and p1max < 2:
				p1max = 2
			if thedeck.a2[i].location == "p2field" and p2max < 2:
				p2max = 2
	if who == "p1":
		print("\nPlayer 1 gets to draw from Age "+str(p1max))
		# Draw from p1max, if empty go to higher age piles
		agetodraw = p1max
		if p1max == 4 and a4decklen == 0:
			gameover = 1
			print("\nDRAWING FROM HIGHEST AGE PILE, WHICH IS EMPTY. GAME OVER!")
		elif p1max == 3:
			if a3decklen == 0:
				agetodraw = 4
				if a4decklen == 0:
					gameover = 1
					print("\nDRAWING FROM HIGHEST AGE PILE, WHICH IS EMPTY. GAME OVER!")
		elif p1max == 2:
			if a2decklen == 0:
				agetodraw = 3
				if a3decklen == 0:
					agetodraw = 4
					if a4decklen == 0:
						gameover = 1
						print("\nDRAWING FROM HIGHEST AGE PILE, WHICH IS EMPTY. GAME OVER!")
		elif p1max == 1:
			if a1decklen == 0:
				agetodraw = 2
				if a2decklen == 0:
					agetodraw = 3
					if a3decklen == 0:
						agetodraw = 4
						if a4decklen == 0:
							gameover = 1
							print("\nDRAWING FROM HIGHEST AGE PILE, WHICH IS EMPTY. GAME OVER!")
		print("\nThe actual age Player 1 gets to draw from is Age "+str(agetodraw))
		# Draw from agetodraw
		if agetodraw == 1:
			for i in range(len(Deck.a1)):
				if Deck.a1[i].place == 1 and Deck.a1[i].location == "deck":
					Deck.a1[i].location = "p1hand"
					Deck.a1[i].place = -1
					print("\nYou have drawn "+Deck.a1[i].name)
			# Move the place of the other deck cards up one
			for i in range(len(Deck.a1)):
				if Deck.a1[i].location == "deck":
					Deck.a1[i].place = Deck.a1[i].place-1
		elif agetodraw == 2:
			for i in range(len(Deck.a2)):
				if Deck.a2[i].place == 1 and Deck.a2[i].location == "deck":
					Deck.a2[i].location = "p1hand"
					Deck.a2[i].place = -1
					print("\nYou have drawn "+Deck.a2[i].name)
			# Move the place of the other deck cards up one
			for i in range(len(Deck.a2)):
				if Deck.a2[i].location == "deck":
							Deck.a2[i].place = Deck.a2[i].place-1
		elif agetodraw == 3:
			for i in range(len(Deck.a3)):
				if Deck.a3[i].place == 1 and Deck.a3[i].location == "deck":
					Deck.a3[i].location = "p1hand"
					Deck.a3[i].place = -1
					print("\nYou have drawn "+Deck.a3[i].name)
			# Move the place of the other deck cards up one
			for i in range(len(Deck.a3)):
				if Deck.a3[i].location == "deck":
					Deck.a3[i].place = Deck.a3[i].place-1
		elif agetodraw == 4:
			for i in range(len(Deck.a4)):
				if Deck.a4[i].place == 1 and Deck.a4[i].location == "deck":
					Deck.a4[i].location = "p1hand"
					Deck.a4[i].place = -1
					print("\nYou have drawn "+Deck.a4[i].name)
			# Move the place of the other deck cards up one
			for i in range(len(Deck.a4)):
				if Deck.a4[i].location == "deck":
					Deck.a4[i].place = Deck.a4[i].place-1
	elif who == "p2":
		print("\nPlayer 2 gets to draw from Age "+str(p2max))
		# Draw from p2max, if empty go to higher age piles
		agetodraw = p2max
		if p2max == 4 and a4decklen == 0:
			gameover = 1
			print("\nDRAWING FROM HIGHEST AGE PILE, WHICH IS EMPTY. GAME OVER!")
		elif p2max == 3:
			if a3decklen == 0:
				agetodraw = 4
				if a4decklen == 0:
					gameover = 1
					print("\nDRAWING FROM HIGHEST AGE PILE, WHICH IS EMPTY. GAME OVER!")
		elif p2max == 2:
			if a2decklen == 0:
				agetodraw = 3
				if a3decklen == 0:
					agetodraw = 4
					if a4decklen == 0:
						gameover = 1
						print("\nDRAWING FROM HIGHEST AGE PILE, WHICH IS EMPTY. GAME OVER!")
		elif p2max == 1:
			if a1decklen == 0:
				agetodraw = 2
				if a2decklen == 0:
					agetodraw = 3
					if a3decklen == 0:
						agetodraw = 4
						if a4decklen == 0:
							gameover = 1
							print("\nDRAWING FROM HIGHEST AGE PILE, WHICH IS EMPTY. GAME OVER!")
		print("\nThe actual age Player 2 gets to draw from is Age "+str(agetodraw))
		# Draw from agetodraw
		if agetodraw == 1:
			for i in range(len(Deck.a1)):
				if Deck.a1[i].place == 1 and Deck.a1[i].location == "deck":
					Deck.a1[i].location = "p2hand"
					Deck.a1[i].place = -1
			# Move the place of the other deck cards up one
			for i in range(len(Deck.a1)):
				if Deck.a1[i].location == "deck":
					Deck.a1[i].place = Deck.a1[i].place-1
		elif agetodraw == 2:
			for i in range(len(Deck.a2)):
				if Deck.a2[i].place == 1 and Deck.a2[i].location == "deck":
					Deck.a2[i].location = "p2hand"
					Deck.a2[i].place = -1
			# Move the place of the other deck cards up one
			for i in range(len(Deck.a2)):
				if Deck.a2[i].location == "deck":
					Deck.a2[i].place = Deck.a2[i].place-1
		elif agetodraw == 3:
			for i in range(len(Deck.a3)):
				if Deck.a3[i].place == 1 and Deck.a3[i].location == "deck":
					Deck.a3[i].location = "p2hand"
					Deck.a3[i].place = -1
			# Move the place of the other deck cards up one
			for i in range(len(Deck.a3)):
				if Deck.a3[i].location == "deck":
					Deck.a3[i].place = Deck.a3[i].place-1
		elif agetodraw == 4:
			for i in range(len(Deck.a4)):
				if Deck.a4[i].place == 1 and Deck.a4[i].location == "deck":
					Deck.a4[i].location = "p2hand"
					Deck.a4[i].place = -1
			# Move the place of the other deck cards up one
			for i in range(len(Deck.a4)):
				if Deck.a4[i].location == "deck":
					Deck.a4[i].place = Deck.a4[i].place-1

## GETCARDS
# Function to quickly grab specific cards (a player's hand, the deck, the dominations, etc.)
# Input:
#   thedeck (arr) - the multi-dimensional array of all deck info
#   what (str) - "p1hand", "p2hand", "dominations", "deck", "p1field", "p2field"
#     p1hand (str) - 
#     p2hand (str) - 
#     dominations (str) - 
#     deck (str) - 
#     p1field (str) - 
#     p2field (str) - 
# Output:
#   array (arr) - an array of the requested info (e.g. an array of the card names in Player 1's hand)
def getcards(thedeck,what):
	# Get then length of each Age array:
	lengtharr = lengths(thedeck,0)
	tota1len = lengtharr[0]
	tota2len = lengtharr[1]
	tota3len = lengtharr[2]
	tota4len = lengtharr[3]
	# Initialize the various subsets:
	p1hand = []
	p2hand = []
	dominations = []
	indeck = []
	inp1field = []
	inp2field = []
	# Loop through the whole deck:
	for i in range(tota1len):
		if thedeck.a1[i].location == "p1hand":
			p1hand = p1hand+[thedeck.a1[i].name]
		elif thedeck.a1[i].location == "p2hand":
			p2hand = p2hand+[thedeck.a1[i].name]
		elif thedeck.a1[i].location == "domination":
			dominations = dominations+[thedeck.a1[i].name]
		elif thedeck.a1[i].location == "deck":
			indeck = indeck+[thedeck.a1[i].name]
		elif thedeck.a1[i].location == "p1field":
			inp1field = inp1field+[thedeck.a1[i].name]
		elif thedeck.a1[i].location == "p2field":
			inp2field = inp2field+[thedeck.a1[i].name]
	for i in range(tota2len):
		if thedeck.a2[i].location == "p1hand":
			p1hand = p1hand+[thedeck.a2[i].name]
		elif thedeck.a2[i].location == "p2hand":
			p2hand = p2hand+[thedeck.a2[i].name]
		elif thedeck.a2[i].location == "domination":
			dominations = dominations+[thedeck.a2[i].name]
		elif thedeck.a2[i].location == "deck":
			indeck = indeck+[thedeck.a2[i].name]
		elif thedeck.a2[i].location == "p1field":
			inp1field = inp1field+[thedeck.a2[i].name]
		elif thedeck.a2[i].location == "p2field":
			inp2field = inp2field+[thedeck.a2[i].name]
	for i in range(tota3len):
		if thedeck.a3[i].location == "p1hand":
			p1hand = p1hand+[thedeck.a3[i].name]
		elif thedeck.a3[i].location == "p2hand":
			p2hand = p2hand+[thedeck.a3[i].name]
		elif thedeck.a3[i].location == "domination":
			dominations = dominations+[thedeck.a3[i].name]
		elif thedeck.a3[i].location == "deck":
			indeck = indeck+[thedeck.a3[i].name]
		elif thedeck.a3[i].location == "p1field":
			inp1field = inp1field+[thedeck.a3[i].name]
		elif thedeck.a3[i].location == "p2field":
			inp2field = inp2field+[thedeck.a3[i].name]
	for i in range(tota4len):
		if thedeck.a4[i].location == "p1hand":
			p1hand = p1hand+[thedeck.a4[i].name]
		elif thedeck.a4[i].location == "p2hand":
			p2hand = p2hand+[thedeck.a4[i].name]
		elif thedeck.a4[i].location == "domination":
			dominations = dominations+[thedeck.a4[i].name]
		elif thedeck.a4[i].location == "deck":
			indeck = indeck+[thedeck.a4[i].name]
		elif thedeck.a4[i].location == "p1field":
			inp1field = inp1field+[thedeck.a4[i].name]
		elif thedeck.a4[i].location == "p2field":
			inp2field = inp2field+[thedeck.a4[i].name]
	# Return desired info:
	if what == "p1hand":
		return p1hand
	elif what == "p2hand":
		return p2hand
	elif what == "dominations":
		return dominations
	elif what == "deck":
		return indeck
	elif what == "p1field":
		return inp1field
	elif what == "p2field":
		return inp2field

## GOESFIRST
# Function to decide who goes first (by the lowest card alphabetically)
# Input:
#   thedeck (arr) - the multi-dimensional array of all deck info
#   p1choice (int) - location of Age 1 (a1) card Player 1 (p1) is playing first
#   p2choice (int) - location of Age 1 (a1) card Player 2 (p2) is playing first
# Output:
#   1 (int) if Player 1 goes first
#   2 (int) if Player 2 goes first
def goesfirst(thedeck,p1choice,p2choice):
	if thedeck.a1[p1choice].name == "Archery":
		return 1
	elif thedeck.a1[p2choice].name == "Archery":
		return 2
	elif thedeck.a1[p1choice].name == "ArcheryX":
		return 1
	elif thedeck.a1[p2choice].name == "ArcheryX":
		return 2
	elif thedeck.a1[p1choice].name == "ArcheryXX":
		return 1
	elif thedeck.a1[p2choice].name == "ArcheryXX":
		return 2
	elif thedeck.a1[p1choice].name == "Metalworking":
		return 1
	elif thedeck.a1[p2choice].name == "Metalworking":
		return 2
	elif thedeck.a1[p1choice].name == "MetalworkingX":
		return 1
	elif thedeck.a1[p2choice].name == "MetalworkingX":
		return 2
	elif thedeck.a1[p1choice].name == "MetalworkingXX":
		return 1
	elif thedeck.a1[p2choice].name == "MetalworkingXX":
		return 2
	elif thedeck.a1[p1choice].name == "Oars":
		return 1
	elif thedeck.a1[p2choice].name == "Oars":
		return 2
	elif thedeck.a1[p1choice].name == "OarsX":
		return 1
	elif thedeck.a1[p2choice].name == "OarsX":
		return 2
	elif thedeck.a1[p1choice].name == "OarsXX":
		return 1
	elif thedeck.a1[p2choice].name == "OarsXX":
		return 2

## LENGTHS
# Function to grab all possible relevant array lengths (e.g. size of Age 1 pile, size of Player 1 hand, etc.)
# Input:
#   thedeck (arr) - the multi-dimensional array of all deck info
# Output:
#   lengtharr (arr) - [tota1len,tota2len,tota3len,tota4len,totdecklen,decklen,dominationlen,p1handlen,p1fieldlen,redp1fieldlen,
#                      p2handlen,p2fieldlen,redp2fieldlen,a1decklen,a2decklen,a3decklen,a4decklen]
#     lengtharr[0] = tota1len
#     lengtharr[1] = tota2len
#     lengtharr[2] = tota3len
#     lengtharr[3] = tota4len
#     lengtharr[4] = totdecklen
#     lengtharr[5] = decklen
#     lengtharr[6] = dominationlen
#     lengtharr[7] = p1handlen
#     lengtharr[8] = p1fieldlen
#     lengtharr[9] = redp1fieldlen
#     lengtharr[10] = p2handlen
#     lengtharr[11] = p2fieldlen
#     lengtharr[12] = redp2fieldlen
#     lengtharr[13] = a1decklen
#     lengtharr[14] = a2decklen
#     lengtharr[15] = a3decklen
#     lengtharr[16] = a4decklen
def lengths(thedeck,printall):
	# Get all array lengths
	tota1len = len(thedeck.a1)
	tota2len = len(thedeck.a2)
	tota3len = len(thedeck.a3)
	tota4len = len(thedeck.a4)
	totdecklen = tota1len+tota2len+tota3len+tota4len
	if printall == 1:
		print("\ntota1len "+str(tota1len))
		print("tota2len "+str(tota2len))
		print("tota3len "+str(tota3len))
		print("tota4len "+str(tota4len))
		print("totdecklen "+str(totdecklen))
	decklen = 0
	dominationlen = 0
	p1handlen = 0
	p1fieldlen = 0
	redp1fieldlen = 0
	p2handlen = 0
	p2fieldlen = 0
	redp2fieldlen = 0
	a1decklen = 0
	for i in range(tota1len):
		if thedeck.a1[i].location == "deck":
			decklen = decklen+1
			a1decklen = a1decklen+1
		elif thedeck.a1[i].location == "domination":
			dominationlen = dominationlen+1
		elif thedeck.a1[i].location == "p1hand":
			p1handlen = p1handlen+1
		elif thedeck.a1[i].location == "p1field":
			p1fieldlen = p1fieldlen+1
			if thedeck.a1[i].color == "red":
				redp1fieldlen = redp1fieldlen+1
		elif thedeck.a1[i].location == "p2hand":
			p2handlen = p2handlen+1
		elif thedeck.a1[i].location == "p2field":
			p2fieldlen = p2fieldlen+1
			if thedeck.a1[i].color == "red":
				redp2fieldlen = redp2fieldlen+1
	a2decklen = 0
	for i in range(tota2len):
		if thedeck.a2[i].location == "deck":
			decklen = decklen+1
			a2decklen = a2decklen+1
		elif thedeck.a2[i].location == "domination":
			dominationlen = dominationlen+1
		elif thedeck.a2[i].location == "p1hand":
			p1handlen = p1handlen+1
		elif thedeck.a2[i].location == "p1field":
			p1fieldlen = p1fieldlen+1
			if thedeck.a1[i].color == "red":
				redp1fieldlen = redp1fieldlen+1
		elif thedeck.a2[i].location == "p2hand":
			p2handlen = p2handlen+1
		elif thedeck.a2[i].location == "p2field":
			p2fieldlen = p2fieldlen+1
			if thedeck.a1[i].color == "red":
				redp2fieldlen = redp2fieldlen+1
	a3decklen = 0
	for i in range(tota3len):
		if thedeck.a3[i].location == "deck":
			decklen = decklen+1
			a3decklen = a3decklen+1
		elif thedeck.a3[i].location == "domination":
			dominationlen = dominationlen+1
		elif thedeck.a3[i].location == "p1hand":
			p1handlen = p1handlen+1
		elif thedeck.a3[i].location == "p1field":
			p1fieldlen = p1fieldlen+1
			if thedeck.a1[i].color == "red":
				redp1fieldlen = redp1fieldlen+1
		elif thedeck.a3[i].location == "p2hand":
			p2handlen = p2handlen+1
		elif thedeck.a3[i].location == "p2field":
			p2fieldlen = p2fieldlen+1
			if thedeck.a1[i].color == "red":
				redp2fieldlen = redp2fieldlen+1
	a4decklen = 0
	for i in range(tota4len):
		if thedeck.a4[i].location == "deck":
			decklen = decklen+1
			a4decklen = a4decklen+1
		elif thedeck.a4[i].location == "domination":
			dominationlen = dominationlen+1
		elif thedeck.a4[i].location == "p1hand":
			p1handlen = p1handlen+1
		elif thedeck.a4[i].location == "p1field":
			p1fieldlen = p1fieldlen+1
			if thedeck.a1[i].color == "red":
				redp1fieldlen = redp1fieldlen+1
		elif thedeck.a4[i].location == "p2hand":
			p2handlen = p2handlen+1
		elif thedeck.a4[i].location == "p2field":
			p2fieldlen = p2fieldlen+1
			if thedeck.a1[i].color == "red":
				redp2fieldlen = redp2fieldlen+1
	if printall == 1:
		print("decklen "+str(decklen))
		print("dominationlen "+str(dominationlen))
		print("p1handlen "+str(p1handlen))
		print("p1fieldlen "+str(p1fieldlen))
		print("redp1fieldlen "+str(redp1fieldlen))
		print("p2handlen "+str(p2handlen))
		print("p2fieldlen "+str(p2fieldlen))
		print("redp2fieldlen "+str(redp2fieldlen))
		print("a1decklen "+str(a1decklen))
		print("a2decklen "+str(a2decklen))
		print("a3decklen "+str(a3decklen))
		print("a4decklen "+str(a4decklen)+"\n")
	lengtharr = [tota1len,tota2len,tota3len,tota4len,totdecklen,decklen,dominationlen,p1handlen,p1fieldlen,redp1fieldlen,
				 p2handlen,p2fieldlen,redp2fieldlen,a1decklen,a2decklen,a3decklen,a4decklen]
	return lengtharr

## P1INITIAL
# Function for Player 1 to pick initial card to play
# Input:
#   thedeck (arr) - the multi-dimensional array of all deck info
# Output:
#   location (int) - the location of Player 1's choice (i.e. thedeck.a1[location])
def p1initial(thedeck):
	# Get the length of the Age 1 array:
	a1len = len(thedeck.a1)
	# Grab the locations of Player 1's cards:
	p1handloc = []
	for i in range(a1len):
		if thedeck.a1[i].location == "p1hand":
			p1handloc = p1handloc+[i]
	# Ask for choice:
	flag = 0
	while flag == 0:
		print("\nPlayer 1 starting cards:")
		print("1 - "+thedeck.a1[p1handloc[0]].name)
		print("2 - "+thedeck.a1[p1handloc[1]].name)
		p1choice = input("\nChoose a card to play first, or 0 for card info: ")
		if p1choice == "0":
			cardinfo(thedeck,"p1hand")
		elif p1choice == "1":
			return p1handloc[0]
		elif p1choice == "2":
			return p1handloc[1]

## P1TURN
# Function for Player 1 to take their turn
# Input:
#   thedeck (arr) - the multi-dimensional array of all deck info
#   actions (int) - number of actions
# Output:
#   nothing (null)
def p1turn(thedeck,actions):
	while actions > 0:
		# Ask for choice:
		print("\nPlayer 1: Choose an action, or check game info: ")
		print("0 - Hand info")
		print("1 - Field info")
		print("2 - Draw")
		print("3 - Play")
		print("4 - Activate")
		p1choice = input("\n")
		if p1choice == "0":
			cardinfo(thedeck,"p1hand")
		elif p1choice == "1":
			print("\nPlayer 1 field:")
			cardinfo(thedeck,"p1field")
			print("\nPlayer 2 field:")
			cardinfo(thedeck,"p2field")
			print("\nAvailable age piles:")
			cardinfo(thedeck,"deck")
		elif p1choice == "2":
			draw(thedeck,"p1")
			actions = actions-1
		elif p1choice == "3":
			play(thedeck,"p1")
			actions = actions-1
		elif p1choice == "4":
			activate(thedeck,"p1")
			actions = actions-1
		else:
			print("\nNot a valid choice.")

## P2INITIAL
# Function for Player 2 to pick initial card to play
# (for now I'm making it the first card alphabetically)
# Input:
#   thedeck (arr) - the multi-dimensional array of all deck info
# Output:
#   location (int) - the location of Player 2's choice (i.e. thedeck.a1[location])
def p2initial(thedeck):
	# Get the length of the Age 1 array:
	a1len = len(thedeck.a1)
	# Grab the locations of Player 2's cards:
	p2handloc = []
	for i in range(a1len):
		if thedeck.a1[i].location == "p2hand":
			p2handloc = p2handloc+[i]
	# Choose the best card to play:
	if thedeck.a1[p2handloc[0]].name == "Archery":
		return p2handloc[0]
	elif thedeck.a1[p2handloc[1]].name == "Archery":
		return p2handloc[1]
	elif thedeck.a1[p2handloc[0]].name == "ArcheryX":
		return p2handloc[0]
	elif thedeck.a1[p2handloc[1]].name == "ArcheryX":
		return p2handloc[1]
	elif thedeck.a1[p2handloc[0]].name == "ArcheryXX":
		return p2handloc[0]
	elif thedeck.a1[p2handloc[1]].name == "ArcheryXX":
		return p2handloc[1]
	elif thedeck.a1[p2handloc[0]].name == "Metalworking":
		return p2handloc[0]
	elif thedeck.a1[p2handloc[1]].name == "Metalworking":
		return p2handloc[1]
	elif thedeck.a1[p2handloc[0]].name == "MetalworkingX":
		return p2handloc[0]
	elif thedeck.a1[p2handloc[1]].name == "MetalworkingX":
		return p2handloc[1]
	elif thedeck.a1[p2handloc[0]].name == "MetalworkingXX":
		return p2handloc[0]
	elif thedeck.a1[p2handloc[1]].name == "MetalworkingXX":
		return p2handloc[1]
	elif thedeck.a1[p2handloc[0]].name == "Oars":
		return p2handloc[0]
	elif thedeck.a1[p2handloc[1]].name == "Oars":
		return p2handloc[1]
	elif thedeck.a1[p2handloc[0]].name == "OarsX":
		return p2handloc[0]
	elif thedeck.a1[p2handloc[1]].name == "OarsX":
		return p2handloc[1]
	elif thedeck.a1[p2handloc[0]].name == "OarsXX":
		return p2handloc[0]
	elif thedeck.a1[p2handloc[1]].name == "OarsXX":
		return p2handloc[1]

## P2TURN
# Function for Player 2 to take their turn
# Input:
#   thedeck (arr) - the multi-dimensional array of all deck info
#   actions (int) - number of actions
# Output:
#   nothing (null)
def p2turn(thedeck,actions):
	# Ask for choice:
	#print("\nPlayer 2: Choose an action, or check game info: ")
	#print("0 - Hand info")
	#print("1 - Field info")
	#print("2 - Draw")
	#print("3 - Play")
	#print("4 - Activate")
	while actions > 0:
		# Possibile options:
		# 1 = only Draw
		# 2 = only Play
		# 3 = only Activate
		# 4 = Draw + Play
		# 5 = Draw + Activate
		# 6 = Play + Activate
		# 7 = Draw + Play + Activate
		# Considerations of the options:
		# First case = Draw
		# - Always an option
		yesdraw = 1
		# Second case = Play
		# - Need a card in hand
		p2hand = getcards(thedeck,"p2hand")
		yesplay = 0
		if len(p2hand) > 0:
			yesplay = 1
		# Third case = Activate
		# - Need a card in the field
		p2field = getcards(thedeck,"p2field")
		yesactivate = 0
		if len(p2field) > 0:
			yesactivate = 1
		# Figure out specific option scenario:
		if yesdraw == 1:
			p2option = 1
			if yesplay == 1:
				p2option = 4
				if yesactivate == 1:
					p2option = 7
			elif yesplay == 0:
				if yesactivate == 1:
					p2option = 5
		elif yesplay == 1:
			p2option = 2
			if yesactivate == 1:
				p2option = 6
		elif yesactivate == 1:
			p2option = 3
		# Pick a random option:
		if p2option == 1:
			p2choice = "2"
		elif p2option == 2:
			p2choice = "3"
		elif p2option == 3:
			p2choice = "4"
		elif p2option == 4:
			randarray = [0,1]
			randpick = random.choice(randarray)
			p2choice = "3"
			if randpick == 0:
				p2choice = "2"
		elif p2option == 5:
			randarray = [0,1]
			randpick = random.choice(randarray)
			p2choice = "4"
			if randpick == 0:
				p2choice = "2"
		elif p2option == 6:
			randarray = [0,1]
			randpick = random.choice(randarray)
			p2choice = "4"
			if randpick == 0:
				p2choice = "3"
		elif p2option == 7:
			randarray = [0,1,2]
			randpick = random.choice(randarray)
			p2choice = "4"
			if randpick == 0:
				p2choice = "2"
			elif randpick == 1:
				p2choice = "3"
		# Make the choice:
		if p2choice == "2":
			print("\nPlayer 2 has chosen to Draw.")
			draw(thedeck,"p2")
			actions = actions-1
		elif p2choice == "3":
			print("\nPlayer 2 has chosen to Play.")
			play(thedeck,"p2")
			actions = actions-1
		elif p2choice == "4":
			print("\nPlayer 2 has chosen to Activate.")
			activate(thedeck,"p2")
			actions = actions-1

## PLAY
# Function to play a card
# Input:
#   thedeck (arr) - the multi-dimensional array of all deck info
#   who (str) - "p1", "p2"
#     p1 - Player 1
#     p2 - Player 2
# Output:
#   nothing (null)
def play(thedeck,who):
	if who == "p1":
		# Get the length of the Age arrays:
		lengtharr = lengths(thedeck,0)
		tota1len = lengtharr[0]
		tota2len = lengtharr[1]
		tota3len = lengtharr[2]
		tota4len = lengtharr[3]
		# Grab the locations of Player 1's cards:
		p1a1handloc = []
		p1a2handloc = []
		p1a3handloc = []
		p1a4handloc = []
		agearr = []
		for i in range(tota1len):
			if thedeck.a1[i].location == "p1hand":
				p1a1handloc = p1a1handloc+[i]
				agearr = agearr+[1]
		for i in range(tota2len):
			if thedeck.a2[i].location == "p1hand":
				p1a2handloc = p1a2handloc+[i]
				agearr = agearr+[2]
		for i in range(tota3len):
			if thedeck.a3[i].location == "p1hand":
				p1a3handloc = p1a3handloc+[i]
				agearr = agearr+[3]
		for i in range(tota4len):
			if thedeck.a4[i].location == "p1hand":
				p1a4handloc = p1a4handloc+[i]
				agearr = agearr+[4]
		# Ask for choice:
		flag = 0
		while flag == 0:
			print("\nPlayer 1 hand:")
			n = 1
			print("Age 1")
			for i in range(len(p1a1handloc)):
				print(str(n)+" - "+thedeck.a1[p1a1handloc[i]].name)
				n = n+1
			print("Age 2")
			for i in range(len(p1a2handloc)):
				print(str(n)+" - "+thedeck.a2[p1a2handloc[i]].name)
				n = n+1
			print("Age 3")
			for i in range(len(p1a3handloc)):
				print(str(n)+" - "+thedeck.a3[p1a3handloc[i]].name)
				n = n+1
			print("Age 4")
			for i in range(len(p1a4handloc)):
				print(str(n)+" - "+thedeck.a4[p1a4handloc[i]].name)
				n = n+1
			p1choice = input("\nChoose a card to play, or enter 0 to check game info: ")
			if p1choice == "0":
				print("\n0 - Hand info")
				print("1 - Field info")
				p1infochoice = input("\n")
				if p1infochoice == "0":
					cardinfo(thedeck,"p1hand")
				elif p1infochoice == "1":
					print("\nPlayer 1 field:")
					cardinfo(thedeck,"p1field")
					print("\nPlayer 2 field:")
					cardinfo(thedeck,"p2field")
					print("\nAvailable age piles:")
					cardinfo(thedeck,"deck")
			elif int(p1choice) < n:
				flag = 1
				a1count = 0
				a2count = 0
				a3count = 0
				a4count = 0
				for i in range(len(agearr)):
					if agearr[i] == 1:
						a1count = a1count + 1
					elif agearr[i] == 2:
						a2count = a2count + 1
					elif agearr[i] == 3:
						a3count = a3count + 1
					elif agearr[i] == 4:
						a4count = a4count + 1
				if agearr[int(p1choice)-1] == 1:
					print("\nYou have chosen to play "+thedeck.a1[p1a1handloc[int(p1choice)-1]].name)
					# First move place of field pile cards up one to account for the new card being played on the pile:
					for i in range(len(Deck.a1)):
						if Deck.a1[i].location == "p1field" and Deck.a1[i].color == Deck.a1[p1a1handloc[int(p1choice)-1]].color:
							Deck.a1[i].place = Deck.a1[i].place + 1
					# Put the new card on the top of the corresponding pile:
					Deck.a1[p1a1handloc[int(p1choice)-1]].location = "p1field"
					Deck.a1[p1a1handloc[int(p1choice)-1]].place = 1
				elif agearr[int(p1choice)-1] == 2:
					print("\nYou have chosen to play "+thedeck.a2[p1a2handloc[int(p1choice)-1-a1count]].name)
					# First move place of field pile cards up one to account for the new card being played on the pile:
					for i in range(len(Deck.a2)):
						if Deck.a2[i].location == "p1field" and Deck.a2[i].color == Deck.a2[p1a2handloc[int(p1choice)-1-a1count]].color:
							Deck.a2[i].place = Deck.a2[i].place + 1
					# Put the new card on the top of the corresponding pile:
					Deck.a2[p1a2handloc[int(p1choice)-1-a1count]].location = "p1field"
					Deck.a2[p1a2handloc[int(p1choice)-1-a1count]].place = 1
				elif agearr[int(p1choice)-1] == 3:
					print("\nYou have chosen to play "+thedeck.a3[p1a3handloc[int(p1choice)-1-a1count-a2count]].name)
					# First move place of field pile cards up one to account for the new card being played on the pile:
					for i in range(len(Deck.a3)):
						if Deck.a3[i].location == "p1field" and Deck.a3[i].color == Deck.a3[p1a3handloc[int(p1choice)-1-a1count-a2count]].color:
							Deck.a3[i].place = Deck.a3[i].place + 1
					# Put the new card on the top of the corresponding pile:
					Deck.a3[p1a3handloc[int(p1choice)-1-a1count-a2count]].location = "p1field"
					Deck.a3[p1a3handloc[int(p1choice)-1-a1count-a2count]].place = 1
				elif agearr[int(p1choice)-1] == 4:
					print("\nYou have chosen to play "+thedeck.a4[p1a4handloc[int(p1choice)-1-a1count-a2count-a3count]].name)
					# First move place of field pile cards up one to account for the new card being played on the pile:
					for i in range(len(Deck.a4)):
						if Deck.a4[i].location == "p1field" and Deck.a4[i].color == Deck.a4[p1a4handloc[int(p1choice)-1-a1count-a2count-a3count]].color:
							Deck.a4[i].place = Deck.a4[i].place + 1
					# Put the new card on the top of the corresponding pile:
					Deck.a4[p1a4handloc[int(p1choice)-1-a1count-a2count-a3count]].location = "p1field"
					Deck.a4[p1a4handloc[int(p1choice)-1-a1count-a2count-a3count]].place = 1
			else:
				print("\nNot a valid choice.")
	elif who == "p2":
		# Get the length of the Age arrays:
		lengtharr = lengths(thedeck,0)
		tota1len = lengtharr[0]
		tota2len = lengtharr[1]
		tota3len = lengtharr[2]
		tota4len = lengtharr[3]
		# Grab the locations of Player 2's cards:
		p2a1handloc = []
		p2a2handloc = []
		p2a3handloc = []
		p2a4handloc = []
		agearr = []
		for i in range(tota1len):
			if thedeck.a1[i].location == "p2hand":
				p2a1handloc = p2a1handloc+[i]
				agearr = agearr+[1]
		for i in range(tota2len):
			if thedeck.a2[i].location == "p2hand":
				p2a2handloc = p2a2handloc+[i]
				agearr = agearr+[2]
		for i in range(tota3len):
			if thedeck.a3[i].location == "p2hand":
				p2a3handloc = p2a3handloc+[i]
				agearr = agearr+[3]
		for i in range(tota4len):
			if thedeck.a4[i].location == "p2hand":
				p2a4handloc = p2a4handloc+[i]
				agearr = agearr+[4]
		# Pick a random card from hand to play:
		flag = 0
		while flag == 0:
			n = 1
			for i in range(len(p2a1handloc)):
				n = n+1
			for i in range(len(p2a2handloc)):
				n = n+1
			for i in range(len(p2a3handloc)):
				n = n+1
			for i in range(len(p2a4handloc)):
				n = n+1
			randarray = []
			for i in range(n-1):
				randarray = randarray+[i+1]
			p2choice = random.choice(randarray)
			if int(p2choice) < n:
				flag = 1
				a1count = 0
				a2count = 0
				a3count = 0
				a4count = 0
				for i in range(len(agearr)):
					if agearr[i] == 1:
						a1count = a1count + 1
					elif agearr[i] == 2:
						a2count = a2count + 1
					elif agearr[i] == 3:
						a3count = a3count + 1
					elif agearr[i] == 4:
						a4count = a4count + 1
				if agearr[int(p2choice)-1] == 1:
					print("\nPlayer 2 has chosen to play "+thedeck.a1[p2a1handloc[int(p2choice)-1]].name)
					# First move place of field pile cards up one to account for the new card being played on the pile:
					for i in range(len(Deck.a1)):
						if Deck.a1[i].location == "p2field" and Deck.a1[i].color == Deck.a1[p2a1handloc[int(p2choice)-1]].color:
							Deck.a1[i].place = Deck.a1[i].place + 1
					# Put the new card on the top of the corresponding pile:
					Deck.a1[p2a1handloc[int(p2choice)-1]].location = "p2field"
					Deck.a1[p2a1handloc[int(p2choice)-1]].place = 1
				elif agearr[int(p2choice)-1] == 2:
					print("\nPlayer 2 has chosen to play "+thedeck.a2[p2a2handloc[int(p2choice)-1-a1count]].name)
					# First move place of field pile cards up one to account for the new card being played on the pile:
					for i in range(len(Deck.a2)):
						if Deck.a2[i].location == "p2field" and Deck.a2[i].color == Deck.a2[p2a2handloc[int(p2choice)-1-a1count]].color:
							Deck.a2[i].place = Deck.a2[i].place + 1
					# Put the new card on the top of the corresponding pile:
					Deck.a2[p2a2handloc[int(p2choice)-1-a1count]].location = "p2field"
					Deck.a2[p2a2handloc[int(p2choice)-1-a1count]].place = 1
				elif agearr[int(p2choice)-1] == 3:
					print("\nPlayer 2 has chosen to play "+thedeck.a3[p2a3handloc[int(p2choice)-1-a1count-a2count]].name)
					# First move place of field pile cards up one to account for the new card being played on the pile:
					for i in range(len(Deck.a3)):
						if Deck.a3[i].location == "p2field" and Deck.a3[i].color == Deck.a3[p2a3handloc[int(p2choice)-1-a1count-a2count]].color:
							Deck.a3[i].place = Deck.a3[i].place + 1
					# Put the new card on the top of the corresponding pile:
					Deck.a3[p2a3handloc[int(p2choice)-1-a1count-a2count]].location = "p2field"
					Deck.a3[p2a3handloc[int(p2choice)-1-a1count-a2count]].place = 1
				elif agearr[int(p2choice)-1] == 4:
					print("\nPlayer 2 has chosen to play "+thedeck.a4[p2a4handloc[int(p2choice)-1-a1count-a2count-a3count]].name)
					# First move place of field pile cards up one to account for the new card being played on the pile:
					for i in range(len(Deck.a4)):
						if Deck.a4[i].location == "p2field" and Deck.a4[i].color == Deck.a4[p2a4handloc[int(p2choice)-1-a1count-a2count-a3count]].color:
							Deck.a4[i].place = Deck.a4[i].place + 1
					# Put the new card on the top of the corresponding pile:
					Deck.a4[p2a4handloc[int(p2choice)-1-a1count-a2count-a3count]].location = "p2field"
					Deck.a4[p2a4handloc[int(p2choice)-1-a1count-a2count-a3count]].place = 1
			else:
				print("\nNot a valid choice.")

## SYMBOLCOUNT
# Function to count the number of symbols for each player on the field
# Input:
#   thedeck (arr) - the multi-dimensional array of all deck info
#   who (str) - "p1", "p2"
#     p1 - Player 1
#     p2 - Player 2
# Output:
#   symbolarr (arr) - [p1bulb,p2bulb,p1castle,p2castle,p1crown,p2crown]
#     symbolarr[0] = p1bulb
#     symbolarr[1] = p2bulb
#     symbolarr[2] = p1castle
#     symbolarr[3] = p2castle
#     symbolarr[4] = p1crown
#     symbolarr[5] = p2crown
def symbolcount(thedeck):
	# Count the total symbols for each player
	lengtharr = lengths(thedeck,0)
	tota1len = lengtharr[0]
	tota2len = lengtharr[1]
	tota3len = lengtharr[2]
	tota4len = lengtharr[3]
	p1bulb = 0
	p2bulb = 0
	p1castle = 0
	p2castle = 0
	p1crown = 0
	p2crown = 0
	# AGE 1
	for i in range(tota1len):
		# PLAYER 1
		if thedeck.a1[i].location == "p1field":
			if thedeck.a1[i].place == 1:
				# P1 UL
				if thedeck.a1[i].syms.ul == "bulb":
					p1bulb = p1bulb + 1
				elif thedeck.a1[i].syms.ul == "castle":
					p1castle = p1castle + 1
				elif thedeck.a1[i].syms.ul == "crown":
					p1crown = p1crown + 1
				# P1 DL
				if thedeck.a1[i].syms.dl == "bulb":
					p1bulb = p1bulb + 1
				elif thedeck.a1[i].syms.dl == "castle":
					p1castle = p1castle + 1
				elif thedeck.a1[i].syms.dl == "crown":
					p1crown = p1crown + 1
				# P1 DM
				if thedeck.a1[i].syms.dm == "bulb":
					p1bulb = p1bulb + 1
				elif thedeck.a1[i].syms.dm == "castle":
					p1castle = p1castle + 1
				elif thedeck.a1[i].syms.dm == "crown":
					p1crown = p1crown + 1
				# P1 DR
				if thedeck.a1[i].syms.dr == "bulb":
					p1bulb = p1bulb + 1
				elif thedeck.a1[i].syms.dr == "castle":
					p1castle = p1castle + 1
				elif thedeck.a1[i].syms.dr == "crown":
					p1crown = p1crown + 1
			elif thedeck.a1[i].place > 1 and thedeck.a1[i].splay != "none":
				# Left splay means DR shows
				if thedeck.a1[i].splay == "left":
					# P1 DR
					if thedeck.a1[i].syms.dr == "bulb":
						p1bulb = p1bulb + 1
					elif thedeck.a1[i].syms.dr == "castle":
						p1castle = p1castle + 1
					elif thedeck.a1[i].syms.dr == "crown":
						p1crown = p1crown + 1
				# Right splay means UL and DL show
				elif thedeck.a1[i].splay == "right":
					# P1 UL
					if thedeck.a1[i].syms.ul == "bulb":
						p1bulb = p1bulb + 1
					elif thedeck.a1[i].syms.ul == "castle":
						p1castle = p1castle + 1
					elif thedeck.a1[i].syms.ul == "crown":
						p1crown = p1crown + 1
					# P1 DL
					if thedeck.a1[i].syms.dl == "bulb":
						p1bulb = p1bulb + 1
					elif thedeck.a1[i].syms.dl == "castle":
						p1castle = p1castle + 1
					elif thedeck.a1[i].syms.dl == "crown":
						p1crown = p1crown + 1
				# Up splay means DL, DM, and DR show
				elif thedeck.a1[i].splay == "up":
					# P1 DL
					if thedeck.a1[i].syms.dl == "bulb":
						p1bulb = p1bulb + 1
					elif thedeck.a1[i].syms.dl == "castle":
						p1castle = p1castle + 1
					elif thedeck.a1[i].syms.dl == "crown":
						p1crown = p1crown + 1
					# P1 DM
					if thedeck.a1[i].syms.dm == "bulb":
						p1bulb = p1bulb + 1
					elif thedeck.a1[i].syms.dm == "castle":
						p1castle = p1castle + 1
					elif thedeck.a1[i].syms.dm == "crown":
						p1crown = p1crown + 1
					# P1 DR
					if thedeck.a1[i].syms.dr == "bulb":
						p1bulb = p1bulb + 1
					elif thedeck.a1[i].syms.dr == "castle":
						p1castle = p1castle + 1
					elif thedeck.a1[i].syms.dr == "crown":
						p1crown = p1crown + 1
		# PLAYER 2
		if thedeck.a1[i].location == "p2field":
			if thedeck.a1[i].place == 1:
				# P2 UL
				if thedeck.a1[i].syms.ul == "bulb":
					p2bulb = p2bulb + 1
				elif thedeck.a1[i].syms.ul == "castle":
					p2castle = p2castle + 1
				elif thedeck.a1[i].syms.ul == "crown":
					p2crown = p2crown + 1
				# P2 DL
				if thedeck.a1[i].syms.dl == "bulb":
					p2bulb = p2bulb + 1
				elif thedeck.a1[i].syms.dl == "castle":
					p2castle = p2castle + 1
				elif thedeck.a1[i].syms.dl == "crown":
					p2crown = p2crown + 1
				# P2 DM
				if thedeck.a1[i].syms.dm == "bulb":
					p2bulb = p2bulb + 1
				elif thedeck.a1[i].syms.dm == "castle":
					p2castle = p2castle + 1
				elif thedeck.a1[i].syms.dm == "crown":
					p2crown = p2crown + 1
				# P2 DR
				if thedeck.a1[i].syms.dr == "bulb":
					p2bulb = p2bulb + 1
				elif thedeck.a1[i].syms.dr == "castle":
					p2castle = p2castle + 1
				elif thedeck.a1[i].syms.dr == "crown":
					p2crown = p2crown + 1
			elif thedeck.a1[i].place > 1 and thedeck.a1[i].splay != "none":
				# Left splay means DR shows
				if thedeck.a1[i].splay == "left":
					# P2 DR
					if thedeck.a1[i].syms.dr == "bulb":
						p2bulb = p2bulb + 1
					elif thedeck.a1[i].syms.dr == "castle":
						p2castle = p2castle + 1
					elif thedeck.a1[i].syms.dr == "crown":
						p2crown = p2crown + 1
				# Right splay means UL and DL show
				elif thedeck.a1[i].splay == "right":
					# P2 UL
					if thedeck.a1[i].syms.ul == "bulb":
						p2bulb = p2bulb + 1
					elif thedeck.a1[i].syms.ul == "castle":
						p2castle = p2castle + 1
					elif thedeck.a1[i].syms.ul == "crown":
						p2crown = p2crown + 1
					# P2 DL
					if thedeck.a1[i].syms.dl == "bulb":
						p2bulb = p2bulb + 1
					elif thedeck.a1[i].syms.dl == "castle":
						p2castle = p2castle + 1
					elif thedeck.a1[i].syms.dl == "crown":
						p2crown = p2crown + 1
				# Up splay means DL, DM, and DR show
				elif thedeck.a1[i].splay == "up":
					# P2 DL
					if thedeck.a1[i].syms.dl == "bulb":
						p2bulb = p2bulb + 1
					elif thedeck.a1[i].syms.dl == "castle":
						p2castle = p2castle + 1
					elif thedeck.a1[i].syms.dl == "crown":
						p2crown = p2crown + 1
					# P2 DM
					if thedeck.a1[i].syms.dm == "bulb":
						p2bulb = p2bulb + 1
					elif thedeck.a1[i].syms.dm == "castle":
						p2castle = p2castle + 1
					elif thedeck.a1[i].syms.dm == "crown":
						p2crown = p2crown + 1
					# P2 DR
					if thedeck.a1[i].syms.dr == "bulb":
						p2bulb = p2bulb + 1
					elif thedeck.a1[i].syms.dr == "castle":
						p2castle = p2castle + 1
					elif thedeck.a1[i].syms.dr == "crown":
						p2crown = p2crown + 1
	# AGE 2
	for i in range(tota2len):
		# PLAYER 1
		if thedeck.a2[i].location == "p1field":
			if thedeck.a2[i].place == 1:
				# P1 UL
				if thedeck.a2[i].syms.ul == "bulb":
					p1bulb = p1bulb + 1
				elif thedeck.a2[i].syms.ul == "castle":
					p1castle = p1castle + 1
				elif thedeck.a2[i].syms.ul == "crown":
					p1crown = p1crown + 1
				# P1 DL
				if thedeck.a2[i].syms.dl == "bulb":
					p1bulb = p1bulb + 1
				elif thedeck.a2[i].syms.dl == "castle":
					p1castle = p1castle + 1
				elif thedeck.a2[i].syms.dl == "crown":
					p1crown = p1crown + 1
				# P1 DM
				if thedeck.a2[i].syms.dm == "bulb":
					p1bulb = p1bulb + 1
				elif thedeck.a2[i].syms.dm == "castle":
					p1castle = p1castle + 1
				elif thedeck.a2[i].syms.dm == "crown":
					p1crown = p1crown + 1
				# P1 DR
				if thedeck.a2[i].syms.dr == "bulb":
					p1bulb = p1bulb + 1
				elif thedeck.a2[i].syms.dr == "castle":
					p1castle = p1castle + 1
				elif thedeck.a2[i].syms.dr == "crown":
					p1crown = p1crown + 1
			elif thedeck.a2[i].place > 1 and thedeck.a2[i].splay != "none":
				# Left splay means DR shows
				if thedeck.a2[i].splay == "left":
					# P1 DR
					if thedeck.a2[i].syms.dr == "bulb":
						p1bulb = p1bulb + 1
					elif thedeck.a2[i].syms.dr == "castle":
						p1castle = p1castle + 1
					elif thedeck.a2[i].syms.dr == "crown":
						p1crown = p1crown + 1
				# Right splay means UL and DL show
				elif thedeck.a2[i].splay == "right":
					# P1 UL
					if thedeck.a2[i].syms.ul == "bulb":
						p1bulb = p1bulb + 1
					elif thedeck.a2[i].syms.ul == "castle":
						p1castle = p1castle + 1
					elif thedeck.a2[i].syms.ul == "crown":
						p1crown = p1crown + 1
					# P1 DL
					if thedeck.a2[i].syms.dl == "bulb":
						p1bulb = p1bulb + 1
					elif thedeck.a2[i].syms.dl == "castle":
						p1castle = p1castle + 1
					elif thedeck.a2[i].syms.dl == "crown":
						p1crown = p1crown + 1
				# Up splay means DL, DM, and DR show
				elif thedeck.a2[i].splay == "up":
					# P1 DL
					if thedeck.a2[i].syms.dl == "bulb":
						p1bulb = p1bulb + 1
					elif thedeck.a2[i].syms.dl == "castle":
						p1castle = p1castle + 1
					elif thedeck.a2[i].syms.dl == "crown":
						p1crown = p1crown + 1
					# P1 DM
					if thedeck.a2[i].syms.dm == "bulb":
						p1bulb = p1bulb + 1
					elif thedeck.a2[i].syms.dm == "castle":
						p1castle = p1castle + 1
					elif thedeck.a2[i].syms.dm == "crown":
						p1crown = p1crown + 1
					# P1 DR
					if thedeck.a2[i].syms.dr == "bulb":
						p1bulb = p1bulb + 1
					elif thedeck.a2[i].syms.dr == "castle":
						p1castle = p1castle + 1
					elif thedeck.a2[i].syms.dr == "crown":
						p1crown = p1crown + 1
		# PLAYER 2
		if thedeck.a2[i].location == "p2field":
			if thedeck.a2[i].place == 1:
				# P2 UL
				if thedeck.a2[i].syms.ul == "bulb":
					p2bulb = p2bulb + 1
				elif thedeck.a2[i].syms.ul == "castle":
					p2castle = p2castle + 1
				elif thedeck.a2[i].syms.ul == "crown":
					p2crown = p2crown + 1
				# P2 DL
				if thedeck.a2[i].syms.dl == "bulb":
					p2bulb = p2bulb + 1
				elif thedeck.a2[i].syms.dl == "castle":
					p2castle = p2castle + 1
				elif thedeck.a2[i].syms.dl == "crown":
					p2crown = p2crown + 1
				# P2 DM
				if thedeck.a2[i].syms.dm == "bulb":
					p2bulb = p2bulb + 1
				elif thedeck.a2[i].syms.dm == "castle":
					p2castle = p2castle + 1
				elif thedeck.a2[i].syms.dm == "crown":
					p2crown = p2crown + 1
				# P2 DR
				if thedeck.a2[i].syms.dr == "bulb":
					p2bulb = p2bulb + 1
				elif thedeck.a2[i].syms.dr == "castle":
					p2castle = p2castle + 1
				elif thedeck.a2[i].syms.dr == "crown":
					p2crown = p2crown + 1
			elif thedeck.a2[i].place > 1 and thedeck.a2[i].splay != "none":
				# Left splay means DR shows
				if thedeck.a2[i].splay == "left":
					# P2 DR
					if thedeck.a2[i].syms.dr == "bulb":
						p2bulb = p2bulb + 1
					elif thedeck.a2[i].syms.dr == "castle":
						p2castle = p2castle + 1
					elif thedeck.a2[i].syms.dr == "crown":
						p2crown = p2crown + 1
				# Right splay means UL and DL show
				elif thedeck.a2[i].splay == "right":
					# P2 UL
					if thedeck.a2[i].syms.ul == "bulb":
						p2bulb = p2bulb + 1
					elif thedeck.a2[i].syms.ul == "castle":
						p2castle = p2castle + 1
					elif thedeck.a2[i].syms.ul == "crown":
						p2crown = p2crown + 1
					# P2 DL
					if thedeck.a2[i].syms.dl == "bulb":
						p2bulb = p2bulb + 1
					elif thedeck.a2[i].syms.dl == "castle":
						p2castle = p2castle + 1
					elif thedeck.a2[i].syms.dl == "crown":
						p2crown = p2crown + 1
				# Up splay means DL, DM, and DR show
				elif thedeck.a2[i].splay == "up":
					# P2 DL
					if thedeck.a2[i].syms.dl == "bulb":
						p2bulb = p2bulb + 1
					elif thedeck.a2[i].syms.dl == "castle":
						p2castle = p2castle + 1
					elif thedeck.a2[i].syms.dl == "crown":
						p2crown = p2crown + 1
					# P2 DM
					if thedeck.a2[i].syms.dm == "bulb":
						p2bulb = p2bulb + 1
					elif thedeck.a2[i].syms.dm == "castle":
						p2castle = p2castle + 1
					elif thedeck.a2[i].syms.dm == "crown":
						p2crown = p2crown + 1
					# P2 DR
					if thedeck.a2[i].syms.dr == "bulb":
						p2bulb = p2bulb + 1
					elif thedeck.a2[i].syms.dr == "castle":
						p2castle = p2castle + 1
					elif thedeck.a2[i].syms.dr == "crown":
						p2crown = p2crown + 1
	# AGE 3
	for i in range(tota3len):
		# PLAYER 1
		if thedeck.a3[i].location == "p1field":
			if thedeck.a3[i].place == 1:
				# P1 UL
				if thedeck.a3[i].syms.ul == "bulb":
					p1bulb = p1bulb + 1
				elif thedeck.a3[i].syms.ul == "castle":
					p1castle = p1castle + 1
				elif thedeck.a3[i].syms.ul == "crown":
					p1crown = p1crown + 1
				# P1 DL
				if thedeck.a3[i].syms.dl == "bulb":
					p1bulb = p1bulb + 1
				elif thedeck.a3[i].syms.dl == "castle":
					p1castle = p1castle + 1
				elif thedeck.a3[i].syms.dl == "crown":
					p1crown = p1crown + 1
				# P1 DM
				if thedeck.a3[i].syms.dm == "bulb":
					p1bulb = p1bulb + 1
				elif thedeck.a3[i].syms.dm == "castle":
					p1castle = p1castle + 1
				elif thedeck.a3[i].syms.dm == "crown":
					p1crown = p1crown + 1
				# P1 DR
				if thedeck.a3[i].syms.dr == "bulb":
					p1bulb = p1bulb + 1
				elif thedeck.a3[i].syms.dr == "castle":
					p1castle = p1castle + 1
				elif thedeck.a3[i].syms.dr == "crown":
					p1crown = p1crown + 1
			elif thedeck.a3[i].place > 1 and thedeck.a3[i].splay != "none":
				# Left splay means DR shows
				if thedeck.a3[i].splay == "left":
					# P1 DR
					if thedeck.a3[i].syms.dr == "bulb":
						p1bulb = p1bulb + 1
					elif thedeck.a3[i].syms.dr == "castle":
						p1castle = p1castle + 1
					elif thedeck.a3[i].syms.dr == "crown":
						p1crown = p1crown + 1
				# Right splay means UL and DL show
				elif thedeck.a3[i].splay == "right":
					# P1 UL
					if thedeck.a3[i].syms.ul == "bulb":
						p1bulb = p1bulb + 1
					elif thedeck.a3[i].syms.ul == "castle":
						p1castle = p1castle + 1
					elif thedeck.a3[i].syms.ul == "crown":
						p1crown = p1crown + 1
					# P1 DL
					if thedeck.a3[i].syms.dl == "bulb":
						p1bulb = p1bulb + 1
					elif thedeck.a3[i].syms.dl == "castle":
						p1castle = p1castle + 1
					elif thedeck.a3[i].syms.dl == "crown":
						p1crown = p1crown + 1
				# Up splay means DL, DM, and DR show
				elif thedeck.a3[i].splay == "up":
					# P1 DL
					if thedeck.a3[i].syms.dl == "bulb":
						p1bulb = p1bulb + 1
					elif thedeck.a3[i].syms.dl == "castle":
						p1castle = p1castle + 1
					elif thedeck.a3[i].syms.dl == "crown":
						p1crown = p1crown + 1
					# P1 DM
					if thedeck.a3[i].syms.dm == "bulb":
						p1bulb = p1bulb + 1
					elif thedeck.a3[i].syms.dm == "castle":
						p1castle = p1castle + 1
					elif thedeck.a3[i].syms.dm == "crown":
						p1crown = p1crown + 1
					# P1 DR
					if thedeck.a3[i].syms.dr == "bulb":
						p1bulb = p1bulb + 1
					elif thedeck.a3[i].syms.dr == "castle":
						p1castle = p1castle + 1
					elif thedeck.a3[i].syms.dr == "crown":
						p1crown = p1crown + 1
		# PLAYER 2
		if thedeck.a3[i].location == "p2field":
			if thedeck.a3[i].place == 1:
				# P2 UL
				if thedeck.a3[i].syms.ul == "bulb":
					p2bulb = p2bulb + 1
				elif thedeck.a3[i].syms.ul == "castle":
					p2castle = p2castle + 1
				elif thedeck.a3[i].syms.ul == "crown":
					p2crown = p2crown + 1
				# P2 DL
				if thedeck.a3[i].syms.dl == "bulb":
					p2bulb = p2bulb + 1
				elif thedeck.a3[i].syms.dl == "castle":
					p2castle = p2castle + 1
				elif thedeck.a3[i].syms.dl == "crown":
					p2crown = p2crown + 1
				# P2 DM
				if thedeck.a3[i].syms.dm == "bulb":
					p2bulb = p2bulb + 1
				elif thedeck.a3[i].syms.dm == "castle":
					p2castle = p2castle + 1
				elif thedeck.a3[i].syms.dm == "crown":
					p2crown = p2crown + 1
				# P2 DR
				if thedeck.a3[i].syms.dr == "bulb":
					p2bulb = p2bulb + 1
				elif thedeck.a3[i].syms.dr == "castle":
					p2castle = p2castle + 1
				elif thedeck.a3[i].syms.dr == "crown":
					p2crown = p2crown + 1
			elif thedeck.a3[i].place > 1 and thedeck.a3[i].splay != "none":
				# Left splay means DR shows
				if thedeck.a3[i].splay == "left":
					# P2 DR
					if thedeck.a3[i].syms.dr == "bulb":
						p2bulb = p2bulb + 1
					elif thedeck.a3[i].syms.dr == "castle":
						p2castle = p2castle + 1
					elif thedeck.a3[i].syms.dr == "crown":
						p2crown = p2crown + 1
				# Right splay means UL and DL show
				elif thedeck.a3[i].splay == "right":
					# P2 UL
					if thedeck.a3[i].syms.ul == "bulb":
						p2bulb = p2bulb + 1
					elif thedeck.a3[i].syms.ul == "castle":
						p2castle = p2castle + 1
					elif thedeck.a3[i].syms.ul == "crown":
						p2crown = p2crown + 1
					# P2 DL
					if thedeck.a3[i].syms.dl == "bulb":
						p2bulb = p2bulb + 1
					elif thedeck.a3[i].syms.dl == "castle":
						p2castle = p2castle + 1
					elif thedeck.a3[i].syms.dl == "crown":
						p2crown = p2crown + 1
				# Up splay means DL, DM, and DR show
				elif thedeck.a3[i].splay == "up":
					# P2 DL
					if thedeck.a3[i].syms.dl == "bulb":
						p2bulb = p2bulb + 1
					elif thedeck.a3[i].syms.dl == "castle":
						p2castle = p2castle + 1
					elif thedeck.a3[i].syms.dl == "crown":
						p2crown = p2crown + 1
					# P2 DM
					if thedeck.a3[i].syms.dm == "bulb":
						p2bulb = p2bulb + 1
					elif thedeck.a3[i].syms.dm == "castle":
						p2castle = p2castle + 1
					elif thedeck.a3[i].syms.dm == "crown":
						p2crown = p2crown + 1
					# P2 DR
					if thedeck.a3[i].syms.dr == "bulb":
						p2bulb = p2bulb + 1
					elif thedeck.a3[i].syms.dr == "castle":
						p2castle = p2castle + 1
					elif thedeck.a3[i].syms.dr == "crown":
						p2crown = p2crown + 1
	# AGE 4
	for i in range(tota4len):
		# PLAYER 1
		if thedeck.a4[i].location == "p1field":
			if thedeck.a4[i].place == 1:
				# P1 UL
				if thedeck.a4[i].syms.ul == "bulb":
					p1bulb = p1bulb + 1
				elif thedeck.a4[i].syms.ul == "castle":
					p1castle = p1castle + 1
				elif thedeck.a4[i].syms.ul == "crown":
					p1crown = p1crown + 1
				# P1 DL
				if thedeck.a4[i].syms.dl == "bulb":
					p1bulb = p1bulb + 1
				elif thedeck.a4[i].syms.dl == "castle":
					p1castle = p1castle + 1
				elif thedeck.a4[i].syms.dl == "crown":
					p1crown = p1crown + 1
				# P1 DM
				if thedeck.a4[i].syms.dm == "bulb":
					p1bulb = p1bulb + 1
				elif thedeck.a4[i].syms.dm == "castle":
					p1castle = p1castle + 1
				elif thedeck.a4[i].syms.dm == "crown":
					p1crown = p1crown + 1
				# P1 DR
				if thedeck.a4[i].syms.dr == "bulb":
					p1bulb = p1bulb + 1
				elif thedeck.a4[i].syms.dr == "castle":
					p1castle = p1castle + 1
				elif thedeck.a4[i].syms.dr == "crown":
					p1crown = p1crown + 1
			elif thedeck.a4[i].place > 1 and thedeck.a4[i].splay != "none":
				# Left splay means DR shows
				if thedeck.a4[i].splay == "left":
					# P1 DR
					if thedeck.a4[i].syms.dr == "bulb":
						p1bulb = p1bulb + 1
					elif thedeck.a4[i].syms.dr == "castle":
						p1castle = p1castle + 1
					elif thedeck.a4[i].syms.dr == "crown":
						p1crown = p1crown + 1
				# Right splay means UL and DL show
				elif thedeck.a4[i].splay == "right":
					# P1 UL
					if thedeck.a4[i].syms.ul == "bulb":
						p1bulb = p1bulb + 1
					elif thedeck.a4[i].syms.ul == "castle":
						p1castle = p1castle + 1
					elif thedeck.a4[i].syms.ul == "crown":
						p1crown = p1crown + 1
					# P1 DL
					if thedeck.a4[i].syms.dl == "bulb":
						p1bulb = p1bulb + 1
					elif thedeck.a4[i].syms.dl == "castle":
						p1castle = p1castle + 1
					elif thedeck.a4[i].syms.dl == "crown":
						p1crown = p1crown + 1
				# Up splay means DL, DM, and DR show
				elif thedeck.a4[i].splay == "up":
					# P1 DL
					if thedeck.a4[i].syms.dl == "bulb":
						p1bulb = p1bulb + 1
					elif thedeck.a4[i].syms.dl == "castle":
						p1castle = p1castle + 1
					elif thedeck.a4[i].syms.dl == "crown":
						p1crown = p1crown + 1
					# P1 DM
					if thedeck.a4[i].syms.dm == "bulb":
						p1bulb = p1bulb + 1
					elif thedeck.a4[i].syms.dm == "castle":
						p1castle = p1castle + 1
					elif thedeck.a4[i].syms.dm == "crown":
						p1crown = p1crown + 1
					# P1 DR
					if thedeck.a4[i].syms.dr == "bulb":
						p1bulb = p1bulb + 1
					elif thedeck.a4[i].syms.dr == "castle":
						p1castle = p1castle + 1
					elif thedeck.a4[i].syms.dr == "crown":
						p1crown = p1crown + 1
		# PLAYER 2
		if thedeck.a4[i].location == "p2field":
			if thedeck.a4[i].place == 1:
				# P2 UL
				if thedeck.a4[i].syms.ul == "bulb":
					p2bulb = p2bulb + 1
				elif thedeck.a4[i].syms.ul == "castle":
					p2castle = p2castle + 1
				elif thedeck.a4[i].syms.ul == "crown":
					p2crown = p2crown + 1
				# P2 DL
				if thedeck.a4[i].syms.dl == "bulb":
					p2bulb = p2bulb + 1
				elif thedeck.a4[i].syms.dl == "castle":
					p2castle = p2castle + 1
				elif thedeck.a4[i].syms.dl == "crown":
					p2crown = p2crown + 1
				# P2 DM
				if thedeck.a4[i].syms.dm == "bulb":
					p2bulb = p2bulb + 1
				elif thedeck.a4[i].syms.dm == "castle":
					p2castle = p2castle + 1
				elif thedeck.a4[i].syms.dm == "crown":
					p2crown = p2crown + 1
				# P2 DR
				if thedeck.a4[i].syms.dr == "bulb":
					p2bulb = p2bulb + 1
				elif thedeck.a4[i].syms.dr == "castle":
					p2castle = p2castle + 1
				elif thedeck.a4[i].syms.dr == "crown":
					p2crown = p2crown + 1
			elif thedeck.a4[i].place > 1 and thedeck.a4[i].splay != "none":
				# Left splay means DR shows
				if thedeck.a4[i].splay == "left":
					# P2 DR
					if thedeck.a4[i].syms.dr == "bulb":
						p2bulb = p2bulb + 1
					elif thedeck.a4[i].syms.dr == "castle":
						p2castle = p2castle + 1
					elif thedeck.a4[i].syms.dr == "crown":
						p2crown = p2crown + 1
				# Right splay means UL and DL show
				elif thedeck.a4[i].splay == "right":
					# P2 UL
					if thedeck.a4[i].syms.ul == "bulb":
						p2bulb = p2bulb + 1
					elif thedeck.a4[i].syms.ul == "castle":
						p2castle = p2castle + 1
					elif thedeck.a4[i].syms.ul == "crown":
						p2crown = p2crown + 1
					# P2 DL
					if thedeck.a4[i].syms.dl == "bulb":
						p2bulb = p2bulb + 1
					elif thedeck.a4[i].syms.dl == "castle":
						p2castle = p2castle + 1
					elif thedeck.a4[i].syms.dl == "crown":
						p2crown = p2crown + 1
				# Up splay means DL, DM, and DR show
				elif thedeck.a4[i].splay == "up":
					# P2 DL
					if thedeck.a4[i].syms.dl == "bulb":
						p2bulb = p2bulb + 1
					elif thedeck.a4[i].syms.dl == "castle":
						p2castle = p2castle + 1
					elif thedeck.a4[i].syms.dl == "crown":
						p2crown = p2crown + 1
					# P2 DM
					if thedeck.a4[i].syms.dm == "bulb":
						p2bulb = p2bulb + 1
					elif thedeck.a4[i].syms.dm == "castle":
						p2castle = p2castle + 1
					elif thedeck.a4[i].syms.dm == "crown":
						p2crown = p2crown + 1
					# P2 DR
					if thedeck.a4[i].syms.dr == "bulb":
						p2bulb = p2bulb + 1
					elif thedeck.a4[i].syms.dr == "castle":
						p2castle = p2castle + 1
					elif thedeck.a4[i].syms.dr == "crown":
						p2crown = p2crown + 1
	symbolarr = [p1bulb,p2bulb,p1castle,p2castle,p1crown,p2crown]
	return symbolarr

##################
## MAIN ROUTINE ##
##################

## PRINT OPENING TEXT

print("\n    ****************")
print(  "    ** Innovation **")
print(  "    ****************")

print("\n    Code Developed By")
print(  "       Alex Spacek")
print(  "     5/8/19-2/23/26")

## DEFINE CLASSES

## SYMBOLS
# Possible symbol:
#   bulb
#   castle
#   crown
#   none
# Initiate by:
#   test = Symbols("crown","castle","none","bulb")
# Then you have:
#   test.ul = "crown"
#   test.dl = "castle"
#   test.dm = "none"
#   test.dr = "bulb"
# This is itself used in the class "Card" below.
class Symbols:
	def __init__(self,ul,dl,dm,dr):
		self.ul = ul	# up left
		self.dl = dl	# down left
		self.dm = dm	# down middle
		self.dr = dr	# down right

## EFFECTS
# Possible type:
#   coop
#   demand
# Possible cost:
#   bulb
#   castle
#   crown
# Initiate by:
#   test = Effects("demand","castle","I demand you take my castle!")
# Then you have:
#   test.type = "demand"
#   test.cost = "castle"
#   test.text = "I demand you take my castle!"
# This is itself used in the class "Card" below.
class Effects:
	def __init__(self,type,cost,text):
		self.type = type
		self.cost = cost
		self.text = text

## CARD
# Possible name:
#   Any card name
# Possible age:
#   1, 2, 3, 4
# Possible color:
#   red
# Possible location:
#   deck
#   domination
#   p1field
#   p1hand
#   p2field
#   p2hand
# Possible place:
#   -1         - unused
#    1         - on top of its pile
#    2 or more - that place in its pile, from the top
# Possible splay:
#   left
#   none
#   right
#   up
# Possible syms:
#   See SYMBOLS above
# Possible effect:
#   See EFFECTS above
# Initiate by:
#   test = Card("Archery",1,"red","deck",-1,"none",
#               "castle","bulb","none","castle",
#               "demand","castle","I demand you draw a [1], then transfer the highest card in your hand to my hand!",
#               "","","")
# Then you have:
#   test.name = "Archery"
#   test.age = 1
#   test.color = "red"
#   test.location = "deck"
#	test.place = -1
#	test.splay = "none"
#   test.syms.ul = "castle"
#   test.syms.dl = "bulb"
#   test.syms.dm = "none"
#   test.syms.dr = "castle"
#   test.effect1.type = "demand"
#   test.effect1.cost = "castle"
#   test.effect1.text = "I demand you draw a [1], then transfer the highest card in your hand to my hand!"
#   test.effect2.type = ""
#   test.effect2.cost = ""
#   test.effect2.text = ""
# These Cards will be defined, placed in the "Ages" class, and assembled into the "Deck" later.
class Card:
	def __init__(self,name,age,color,location,place,splay,ul,dl,dm,dr,type1,cost1,text1,type2,cost2,text2):
		self.name = name
		self.age = age
		self.color = color
		self.location = location
		self.place = place
		self.splay = splay
		self.syms = Symbols(ul,dl,dm,dr)
		self.effect1 = Effects(type1,cost1,text1)
		self.effect2 = Effects(type2,cost2,text2)

## DOMAIN
# Initiate by:
#   test = Domain("World",
#	              "Claim this special achievement immediately if you have twelve or more [clocks] on your board.")
# Then you have:
#   test.name = "World"
#   test.text = "Claim this special achievement immediately if you have twelve or more [clocks] on your board."
# These will make up the special Domains to be dominated.
class Domain:
	def __init__(self,name,text):
		self.name = name
		self.text = text

## AGES
# Initiate by:
#   test = Ages((card1,card2,card3),
#               (card4,card5,card6),
#               (card7,card8,card9),
#               (card10,card11,card12))
# Then you have:
#   test.a1[2].name = card3.name
#   test.a4[0].location = card10.location
#   etc.
# The "Deck" will be set up using the "Ages" class.
class Ages:
	def __init__(self,a1,a2,a3,a4):
		self.a1 = a1
		self.a2 = a2
		self.a3 = a3
		self.a4 = a4

## DEFINE CARDS

# NOTE - While writing the code, I'm just using 3 cards (Archery, Metalworking, Oars) and duplicating them.
#        Age 1 - 3x each = 9 total
#        Age 2 - 2x each = 6 total
#        Age 3 - 2x each = 6 total
#        Age 4 - 2x each = 6 total

# Age 1 - 1/9 - Archery
Archery = Card("Archery",1,"red","deck",-1,"none",
	"castle","bulb","none","castle",
	"demand","castle","I demand you draw a [1], then transfer the highest card in your hand to my hand!",
	"","","")

# Age 1 - 2/9 - Archery (duplicate)
ArcheryX = Card("ArcheryX",1,"red","deck",-1,"none",
	"castle","bulb","none","castle",
	"demand","castle","I demand you draw a [1], then transfer the highest card in your hand to my hand!",
	"","","")

# Age 1 - 3/9 - Archery (duplicate)
ArcheryXX = Card("ArcheryXX",1,"red","deck",-1,"none",
	"castle","bulb","none","castle",
	"demand","castle","I demand you draw a [1], then transfer the highest card in your hand to my hand!",
	"","","")

# Age 2 - 1/6 - Archery (duplicate)
Archery2 = Card("Archery2",2,"red","deck",-1,"none",
	"castle","bulb","none","castle",
	"demand","castle","I demand you draw a [1], then transfer the highest card in your hand to my hand!",
	"","","")

# Age 2 - 2/6 - Archery (duplicate)
Archery2X = Card("Archery2X",2,"red","deck",-1,"none",
	"castle","bulb","none","castle",
	"demand","castle","I demand you draw a [1], then transfer the highest card in your hand to my hand!",
	"","","")

# Age 3 - 1/6 - Archery (duplicate)
Archery3 = Card("Archery3",3,"red","deck",-1,"none",
	"castle","bulb","none","castle",
	"demand","castle","I demand you draw a [1], then transfer the highest card in your hand to my hand!",
	"","","")

# Age 3 - 2/6 - Archery (duplicate)
Archery3X = Card("Archery3X",3,"red","deck",-1,"none",
	"castle","bulb","none","castle",
	"demand","castle","I demand you draw a [1], then transfer the highest card in your hand to my hand!",
	"","","")

# Age 4 - 1/6 - Archery (duplicate)
Archery4 = Card("Archery4",4,"red","deck",-1,"none",
	"castle","bulb","none","castle",
	"demand","castle","I demand you draw a [1], then transfer the highest card in your hand to my hand!",
	"","","")

# Age 4 - 2/6 - Archery (duplicate)
Archery4X = Card("Archery4X",4,"red","deck",-1,"none",
	"castle","bulb","none","castle",
	"demand","castle","I demand you draw a [1], then transfer the highest card in your hand to my hand!",
	"","","")

# Age 1 - 4/9 - Metalworking
Metalworking = Card("Metalworking",1,"red","deck",-1,"none",
	"castle","castle","none","castle",
	"coop","castle","Draw and reveal a [1]. If it has a [castle], score it and repeat this dogma effect. Otherwise, keep it.",
	"","","")

# Age 1 - 5/9 - Metalworking (duplicate)
MetalworkingX = Card("MetalworkingX",1,"red","deck",-1,"none",
	"castle","castle","none","castle",
	"coop","castle","Draw and reveal a [1]. If it has a [castle], score it and repeat this dogma effect. Otherwise, keep it.",
	"","","")

# Age 1 - 6/9 - Metalworking (duplicate)
MetalworkingXX = Card("MetalworkingXX",1,"red","deck",-1,"none",
	"castle","castle","none","castle",
	"coop","castle","Draw and reveal a [1]. If it has a [castle], score it and repeat this dogma effect. Otherwise, keep it.",
	"","","")

# Age 2 - 3/6 - Metalworking (duplicate)
Metalworking2 = Card("Metalworking2",2,"red","deck",-1,"none",
	"castle","castle","none","castle",
	"coop","castle","Draw and reveal a [1]. If it has a [castle], score it and repeat this dogma effect. Otherwise, keep it.",
	"","","")

# Age 2 - 4/6 - Metalworking (duplicate)
Metalworking2X = Card("Metalworking2X",2,"red","deck",-1,"none",
	"castle","castle","none","castle",
	"coop","castle","Draw and reveal a [1]. If it has a [castle], score it and repeat this dogma effect. Otherwise, keep it.",
	"","","")

# Age 3 - 3/6 - Metalworking (duplicate)
Metalworking3 = Card("Metalworking3",3,"red","deck",-1,"none",
	"castle","castle","none","castle",
	"coop","castle","Draw and reveal a [1]. If it has a [castle], score it and repeat this dogma effect. Otherwise, keep it.",
	"","","")

# Age 3 - 4/6 - Metalworking (duplicate)
Metalworking3X = Card("Metalworking3X",3,"red","deck",-1,"none",
	"castle","castle","none","castle",
	"coop","castle","Draw and reveal a [1]. If it has a [castle], score it and repeat this dogma effect. Otherwise, keep it.",
	"","","")

# Age 4 - 3/6 - Metalworking (duplicate)
Metalworking4 = Card("Metalworking4",4,"red","deck",-1,"none",
	"castle","castle","none","castle",
	"coop","castle","Draw and reveal a [1]. If it has a [castle], score it and repeat this dogma effect. Otherwise, keep it.",
	"","","")

# Age 4 - 4/6 - Metalworking (duplicate)
Metalworking4X = Card("Metalworking4X",4,"red","deck",-1,"none",
	"castle","castle","none","castle",
	"coop","castle","Draw and reveal a [1]. If it has a [castle], score it and repeat this dogma effect. Otherwise, keep it.",
	"","","")

# Age 1 - 7/9 - Oars
Oars = Card("Oars",1,"red","deck",-1,"none",
	"castle","crown","none","castle",
	"demand","castle","I demand you transfer a card with a [crown] from your hand to my score pile! If you do, draw a [1].",
	"coop","castle","If no cards were transferred due to this demand, draw a [1].")

# Age 1 - 8/9 - Oars (duplicate)
OarsX = Card("OarsX",1,"red","deck",-1,"none",
	"castle","crown","none","castle",
	"demand","castle","I demand you transfer a card with a [crown] from your hand to my score pile! If you do, draw a [1].",
	"coop","castle","If no cards were transferred due to this demand, draw a [1].")

# Age 1 - 9/9 - Oars (duplicate)
OarsXX = Card("OarsXX",1,"red","deck",-1,"none",
	"castle","crown","none","castle",
	"demand","castle","I demand you transfer a card with a [crown] from your hand to my score pile! If you do, draw a [1].",
	"coop","castle","If no cards were transferred due to this demand, draw a [1].")

# Age 2 - 5/6 - Oars (duplicate)
Oars2 = Card("Oars2",2,"red","deck",-1,"none",
	"castle","crown","none","castle",
	"demand","castle","I demand you transfer a card with a [crown] from your hand to my score pile! If you do, draw a [1].",
	"coop","castle","If no cards were transferred due to this demand, draw a [1].")

# Age 2 - 6/6 - Oars (duplicate)
Oars2X = Card("Oars2X",2,"red","deck",-1,"none",
	"castle","crown","none","castle",
	"demand","castle","I demand you transfer a card with a [crown] from your hand to my score pile! If you do, draw a [1].",
	"coop","castle","If no cards were transferred due to this demand, draw a [1].")

# Age 3 - 5/6 - Oars (duplicate)
Oars3 = Card("Oars3",3,"red","deck",-1,"none",
	"castle","crown","none","castle",
	"demand","castle","I demand you transfer a card with a [crown] from your hand to my score pile! If you do, draw a [1].",
	"coop","castle","If no cards were transferred due to this demand, draw a [1].")

# Age 3 - 6/6 - Oars (duplicate)
Oars3X = Card("Oars3X",3,"red","deck",-1,"none",
	"castle","crown","none","castle",
	"demand","castle","I demand you transfer a card with a [crown] from your hand to my score pile! If you do, draw a [1].",
	"coop","castle","If no cards were transferred due to this demand, draw a [1].")

# Age 4 - 5/6 - Oars (duplicate)
Oars4 = Card("Oars4",4,"red","deck",-1,"none",
	"castle","crown","none","castle",
	"demand","castle","I demand you transfer a card with a [crown] from your hand to my score pile! If you do, draw a [1].",
	"coop","castle","If no cards were transferred due to this demand, draw a [1].")

# Age 4 - 6/6 - Oars (duplicate)
Oars4X = Card("Oars4X",4,"red","deck",-1,"none",
	"castle","crown","none","castle",
	"demand","castle","I demand you transfer a card with a [crown] from your hand to my score pile! If you do, draw a [1].",
	"coop","castle","If no cards were transferred due to this demand, draw a [1].")

## BUILD THE DECK

# The deck is an "Ages" class consisting of "Card" classes.
# See the setup of the "Ages" class for how to address all of the card elements.
Deck = Ages((Archery,ArcheryX,ArcheryXX,Metalworking,MetalworkingX,MetalworkingXX,Oars,OarsX,OarsXX),
	(Archery2,Archery2X,Metalworking2,Metalworking2X,Oars2,Oars2X),
	(Archery3,Archery3X,Metalworking3,Metalworking3X,Oars3,Oars3X),
	(Archery4,Archery4X,Metalworking4,Metalworking4X,Oars4,Oars4X))

## DEFINE DOMAINS

# Domain - 1/5 - Monument
Monument = Domain("Monument",
	"Claim this special achievement immediately if you tuck six or score six cards during a single turn.")

# Domain - 2/5 - Empire
Empire = Domain("Empire",
	"Claim this special achievement immediately if you have three or more icons of all six types: [bulb] [leaf] [factory] [clock] [crown] [castle].")

# Domain - 3/5 - Wonder
Wonder = Domain("Wonder",
	"Claim this special achievement immediately if you have five colors on your board, and each is splayed either up or right.")

# Domain - 4/5 - World
World = Domain("World",
	"Claim this special achievement immediately if you have twelve or more [clocks] on your board.")

# Domain - 5/5 - Universe
Universe = Domain("Universe",
	"Claim this special achievement immediately if you have five top cards, and each is of value 8 or higher.")

## SHUFFLE DECKS AND BUILD THE DOMINATIONS

# Grab indexes for all Age 1 cards:
arr = [i for i in range(len(Deck.a1))]
# Arrange them randomly:
shuffle(arr)
# Assign each card to its place:
count = 1
for i in range(len(arr)):
	# Put the first card in the dominations:
	if i == 0:
		Deck.a1[arr[i]].location = "domination"
	else:
		Deck.a1[arr[i]].place = count
		count = count+1

# Grab indexes for all Age 2 cards:
arr = [i for i in range(len(Deck.a2))]
# Arrange them randomly:
shuffle(arr)
# Assign each card to its place:
count = 1
for i in range(len(arr)):
	# Put the first card in the dominations:
	if i == 0:
		Deck.a2[arr[i]].location = "domination"
	else:
		Deck.a2[arr[i]].place = count
		count = count+1

# Grab indexes for all Age 3 cards:
arr = [i for i in range(len(Deck.a3))]
# Arrange them randomly:
shuffle(arr)
# Assign each card to its place:
count = 1
for i in range(len(arr)):
	# Put the first card in the dominations:
	if i == 0:
		Deck.a3[arr[i]].location = "domination"
	else:
		Deck.a3[arr[i]].place = count
		count = count+1

# Grab indexes for all Age 4 cards:
arr = [i for i in range(len(Deck.a4))]
# Arrange them randomly:
shuffle(arr)
# Assign each card to its place:
count = 1
for i in range(len(arr)):
	# Put the first card in the dominations:
	if i == 0:
		Deck.a4[arr[i]].location = "domination"
	else:
		Deck.a4[arr[i]].place = count
		count = count+1

## DEAL CARDS

# Keep track of how many cards are in each player's hand:
p1count = 0
p2count = 0
# Loop through shuffled Age 1 (a1) cards, deal to players if the cards are in the deck, 2 cards per hand
# Count is 1 less because 1 card is in the domination pile
for i in range(len(Deck.a1)-1):
	for j in range(len(Deck.a1)):
		if Deck.a1[j].place == 1 and Deck.a1[j].location == "deck":
			if p1count < 2:
				Deck.a1[j].location = "p1hand"
				Deck.a1[j].place = -1
				p1count = p1count + 1
				# Move the place of the other deck cards up one
				for k in range(len(Deck.a1)):
					if Deck.a1[k].location == "deck":
						Deck.a1[k].place = Deck.a1[k].place-1
			elif p2count < 2:
				Deck.a1[j].location = "p2hand"
				Deck.a1[j].place = -1
				p2count = p2count + 1
				# Move the place of the other deck cards up one
				for k in range(len(Deck.a1)):
					if Deck.a1[k].location == "deck":
						Deck.a1[k].place = Deck.a1[k].place-1

## PLAY FIRST CARDS

# Note - Player 2 will be the computer player.

# Have Player 1 choose a card:
p1choice = p1initial(Deck)
Deck.a1[p1choice].location = "p1field"
Deck.a1[p1choice].place = 1

# Have Player 2 choose a card:
p2choice = p2initial(Deck)
Deck.a1[p2choice].location = "p2field"
Deck.a1[p2choice].place = 1

# Print out starting cards:
print("\nPlayer 1 has chosen to start with - "+Deck.a1[p1choice].name)
print(  "Player 2 has chosen to start with - "+Deck.a1[p2choice].name)

# Lowest card alphabetically goes first
starter = goesfirst(Deck,p1choice,p2choice)
if starter == 1:
	print("\nPlayer 1 has the lowest card alphabetically and goes first.")
	turn = 1
elif starter == 2:
	print("\nPlayer 2 has the lowest card alphabetically and goes first.")
	turn = 2
# Whoever goes first gets 1 action
print("\nFirst turn gets 1 action. Then every turn gets 2 actions.")

## Program Situation Check
print("\nChecking the state of the program.")
lengtharr = lengths(Deck,0)
if lengtharr[0] != 9:
	print("tota1len should be 9 (x3 each of Archery, Metalworking, and Oars)")
	print(lengtharr[0])
elif lengtharr[1] != 6:
	print("tota2len should be 6 (x2 each of Archery, Metalworking, and Oars)")
	print(lengtharr[1])
elif lengtharr[2] != 6:
	print("tota3len should be 6 (x2 each of Archery, Metalworking, and Oars)")
	print(lengtharr[2])
elif lengtharr[3] != 6:
	print("tota4len should be 6 (x2 each of Archery, Metalworking, and Oars)")
	print(lengtharr[3])
elif lengtharr[4] != 27:
	print("totdecklen should be 27 (9+6+6+6)")
	print(lengtharr[4])
elif lengtharr[5] != 19:
	print("decklen should be 19 (27-4 dominations-2 p1 hand-2 p2 hand)")
	print(lengtharr[5])
elif lengtharr[6] != 4:
	print("dominationlen should be 4 (using ages 1-4)")
	print(lengtharr[6])
elif lengtharr[7] != 1:
	print("p1handlen should be 1 (started with 2 cards, played 1)")
	print(lengtharr[7])
elif lengtharr[8] != 1:
	print("p1fieldlen should be 1 (played 1 card)")
	print(lengtharr[8])
elif lengtharr[9] != 1:
	print("redp1fieldlen should be 1 (played 1 card and they're all red)")
	print(lengtharr[9])
elif lengtharr[10] != 1:
	print("p2handlen should be 1 (started with 2 cards, played 1)")
	print(lengtharr[10])
elif lengtharr[11] != 1:
	print("p2fieldlen should be 1 (played 1 card)")
	print(lengtharr[11])
elif lengtharr[12] != 1:
	print("redp2fieldlen should be 1 (played 1 card and they're all red)")
	print(lengtharr[12])
elif lengtharr[13] != 4:
	print("a1decklen should be 4 (9-1 domination-2 p1 deal-2 p2 deal)")
	print(lengtharr[13])
elif lengtharr[14] != 5:
	print("a2decklen should be 5 (6-1 domination)")
	print(lengtharr[14])
elif lengtharr[15] != 5:
	print("a3decklen should be 5 (6-1 domination)")
	print(lengtharr[15])
elif lengtharr[16] != 5:
	print("a4decklen should be 5 (6-1 domination)")
	print(lengtharr[16])
else:
	print("All good!")

# Do first turn with 1 action, then the other player takes a normal turn
if turn == 1:
	p1turn(Deck,1)
	p2turn(Deck,2)
elif turn == 2:
	p2turn(Deck,1)
	p1turn(Deck,2)

print(getcards(Deck,"p1field"))
print(getcards(Deck,"p2field"))
