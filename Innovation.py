########################################################
#### Innovation.py                                  ####
#### Program to play the game Innovation in Python. ####
#### Last edited 5/29/25 by Alex Spacek             ####
########################################################

#############
## IMPORTS ##
#############

## RANDOM
# Used to "shuffle" the cards
# > random.shuffle(array)
# Which we will use as
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
# Age 2 - Archery3
# Age 2 - Archery3X
# Age 2 - Metalworking3
# Age 2 - Metalworking3X
# Age 2 - Oars3
# Age 2 - Oars3X
# Age 2 - Archery4
# Age 2 - Archery4X
# Age 2 - Metalworking4
# Age 2 - Metalworking4X
# Age 2 - Oars4
# Age 2 - Oars4X

## The overall multi-dimensional array is thedeck
## The cards are located at:
# thedeck.a1[0-8].name = ['Archery','ArcheryX','ArcheryXX',...,'OarsX','OarsXX']
# thedeck.a2[0-6].name = ['Archery2','Archery2X','Metalworking2',...,'Oars2','Oars2X']
# thedeck.a3[0-6].name = ['Archery3','Archery3X','Metalworking3',...,'Oars3','Oars3X']
# thedeck.a4[0-6].name = ['Archery4','Archery4X','Metalworking4',...,'Oars4','Oars4X']

###############
## FUNCTIONS ##
###############

## ACTIVATE
# Function to play a card
# Input:
#   thedeck (arr) - the multi-dimensional array of all deck info
#   who (str) - 'p1', 'p2'
#     p1 - Player 1
#     p2 - Player 2
# Output:
#   nothing (null)
def activate(thedeck,who):

## CARDINFO
# Function to show card info
# Input:
#   thedeck (arr) - the multi-dimensional array of all deck info
#   what (str) - 'p1hand', 'p1field', 'p2field', 'deck'
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
#   who (str) - 'p1', 'p2'
#     p1 - Player 1
#     p2 - Player 2
# Output:
#   nothing (null)
def draw(thedeck,who):
	if who == "p1":
		print("blah")

## GETCARDS
# Function to quickly grab specific cards (a player's hand, the deck, the dominations, etc.)
# Input:
#   thedeck (arr) - the multi-dimensional array of all deck info
#   what (str) - 'p1hand', 'p2hand', 'dominations', 'deck', 'p1field', 'p2field'
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
	a1len = len(thedeck.a1)
	a2len = len(thedeck.a2)
	a3len = len(thedeck.a3)
	a4len = len(thedeck.a4)
	# Initialize the various subsets:
	p1hand = []
	p2hand = []
	dominations = []
	indeck = []
	inp1field = []
	inp2field = []
	# Loop through the whole deck:
	for i in range(a1len):
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
	for i in range(a2len):
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
	for i in range(a3len):
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
	for i in range(a4len):
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
#   L
def lengths(thedeck):
	# Get all array lengths
	

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
	print("Player 1 starting cards:")
	print("1 - "+thedeck.a1[p1handloc[0]].name)
	print("2 - "+thedeck.a1[p1handloc[1]].name)
	flag = 0
	while flag == 0:
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
	# Ask for choice:
	print("Player 1: Choose an action, or check game info: ")
	print("0 - Hand info")
	print("1 - Field info")
	print("2 - Draw")
	print("3 - Play")
	print("4 - Activate")
	while actions > 0:
		p1choice = input("\n")
		if p1choice == "0":
			cardinfo("p1hand",thedeck)
		elif p1choice == "1":
			print("Player 1 field:")
			cardinfo("p1field",thedeck)
			print("Player 2 field:")
			cardinfo("p2field",thedeck)
			print("Available age piles:")
			cardinfo("deck",thedeck)
		elif p1choice == "2":
			draw("p1",thedeck)
			actions = actions-1
		elif p1choice == "3":
			play("p1",thedeck)
			actions = actions-1
		elif p1choice == "4":
			activate("p1",thedeck)
			actions = actions-1

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
	print("Player 2: Choose an action, or check game info: ")
	print("0 - Hand info")
	print("1 - Field info")
	print("2 - Draw")
	print("3 - Play")
	print("4 - Activate")
	while actions > 0:
		p1choice = input("\n")
		if p1choice == "0":
			cardinfo("p1hand",thedeck)
		elif p1choice == "1":
			print("Player 1 field:")
			cardinfo("p1field",thedeck)
			print("Player 2 field:")
			cardinfo("p2field",thedeck)
			print("Available age piles:")
			cardinfo("deck",thedeck)
		elif p1choice == "2":
			draw("p2",thedeck)
			actions = actions-1
		elif p1choice == "3":
			play("p2",thedeck)
			actions = actions-1

## PLAY
# Function to play a card
# Input:
#   thedeck (arr) - the multi-dimensional array of all deck info
#   who (str) - 'p1', 'p2'
#     p1 - Player 1
#     p2 - Player 2
# Output:
#   nothing (null)
def play(thedeck,who):
	if who == "p1":
		# Get the length of the Age 1 array:
		a1len = len(thedeck.a1)
		# Grab the locations of Player 1's cards:
		p1handloc = []
		for i in range(a1len):
			if thedeck.a1[i].location == "p1hand":
				p1handloc = p1handloc+[i]
		# Ask for choice:
		print("Player 1 starting cards:")
		print("1 - "+thedeck.a1[p1handloc[0]].name)
		print("2 - "+thedeck.a1[p1handloc[1]].name)
		flag = 0
		while flag == 0:
			p1choice = input("\nChoose a card to play first, or 0 for card info: ")
			if p1choice == "0":
				cardinfo("p1hand",thedeck)
			elif p1choice == "1":
				return p1handloc[0]
			elif p1choice == "2":
				return p1handloc[1]

##################
## MAIN ROUTINE ##
##################

## PRINT OPENING TEXT

print("\n    ****************")
print(  "    ** Innovation **")
print(  "    ****************\n")

print(  "    Code Developed By")
print(  "       Alex Spacek")
print(  "     5/8/19-5/29/25\n")

## DEFINE CLASSES

## SYMBOLS
# Possible symbol:
#   bulb
#   castle
#   crown
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

# Domain:
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

# Ages:
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

# NOTE: place = where in its pile the card is, with 1 = on top

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
	# Using base 1 (instead of base 0 that range uses)
	count = i+1
	for j in range(len(Deck.a1)):
		if Deck.a1[j].place == count and Deck.a1[j].location == "deck":
			if p1count < 2:
				Deck.a1[j].location = "p1hand"
				Deck.a1[j].place = -1
				p1count = p1count + 1
			elif p2count < 2:
				Deck.a1[j].location = "p2hand"
				Deck.a1[j].place = -1
				p2count = p2count + 1
			else:
				break

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
	print("\nPlayer 1 has the lowest card alphabetically and goes first")
	turn = 1
elif starter == 2:
	print("\nPlayer 2 has the lowest card alphabetically and goes first")
	turn = 2
# Whoever goes first gets 1 action
print("\nFirst turn gets 1 action. Then every turn gets 2 actions.")

# Do first turn with 1 action, then the other player takes a normal turn
if turn == 1:
	p1turn(Deck,1)
	p2turn(Deck,2)
elif turn == 2:
	p2turn(Deck,1)
	p1turn(Deck,2)

print(getcards(Deck,"p1field"))
print(getcards(Deck,"p2field"))
