## IMPORTS

import random

## PRINT OPENING TEXT

print ""
print "    ****************"
print "    ** Innovation **"
print "    ****************"
print ""
print "Developed by Alex Spacek"
print "     5/8/19-3/27/20"
print ""

## DEFINE CLASSES

class Symbols:
	def __init__(self,ul,dl,dm,dr):
		self.ul = ul	# up left
		self.dl = dl	# down left
		self.dm = dm	# down middle
		self.dr = dr	# down right

class Effects:
	def __init__(self,type,cost,text):
		self.type = type
		self.cost = cost
		self.text = text

class Card:
	def __init__(self,name,age,color,location,ul,dl,dm,dr,type1,cost1,text1,type2,cost2,text2):
		self.name = name
		self.age = age
		self.color = color
		self.location = location
		self.syms = Symbols(ul,dl,dm,dr)
		self.effect1 = Effects(type1,cost1,text1)
		self.effect2 = Effects(type2,cost2,text2)

class Domain:
	def __init__(self,name,text):
		self.name = name
		self.text = text

class Ages:
	def __init__(self,a1,a2,a3,a4):
		self.a1 = a1
		self.a2 = a2
		self.a3 = a3
		self.a4 = a4

## DEFINE CARDS

Archery = Card("Archery",1,"red","deck",
	"castle","bulb","none","castle",
	"demand","castle","I demand you draw a [1], then transfer the highest card in your hand to my hand!",
	"","","")

ArcheryX = Card("Archery",1,"red","deck",
	"castle","bulb","none","castle",
	"demand","castle","I demand you draw a [1], then transfer the highest card in your hand to my hand!",
	"","","")

ArcheryXX = Card("ArcheryX",1,"red","deck",
	"leaf","bulb","none","leaf",
	"demand","leaf","I demand you draw a [1], then transfer the highest card in your hand to my hand!",
	"","","")

Archery2 = Card("Archery",2,"red","deck",
	"castle","bulb","none","castle",
	"demand","castle","I demand you draw a [1], then transfer the highest card in your hand to my hand!",
	"","","")

Archery2X = Card("Archery",2,"red","deck",
	"castle","bulb","none","castle",
	"demand","castle","I demand you draw a [1], then transfer the highest card in your hand to my hand!",
	"","","")

Archery3 = Card("Archery",3,"red","deck",
	"castle","bulb","none","castle",
	"demand","castle","I demand you draw a [1], then transfer the highest card in your hand to my hand!",
	"","","")

Archery3X = Card("Archery",3,"red","deck",
	"castle","bulb","none","castle",
	"demand","castle","I demand you draw a [1], then transfer the highest card in your hand to my hand!",
	"","","")

Archery4 = Card("Archery",4,"red","deck",
	"castle","bulb","none","castle",
	"demand","castle","I demand you draw a [1], then transfer the highest card in your hand to my hand!",
	"","","")

Archery4X = Card("Archery",4,"red","deck",
	"castle","bulb","none","castle",
	"demand","castle","I demand you draw a [1], then transfer the highest card in your hand to my hand!",
	"","","")

Metalworking = Card("Metalworking",1,"red","deck",
	"castle","castle","none","castle",
	"coop","castle","Draw and reveal a [1]. If it has a [castle], score it and repeat this dogma effect. Otherwise, keep it.",
	"","","")

MetalworkingX = Card("Metalworking",1,"red","deck",
	"castle","castle","none","castle",
	"coop","castle","Draw and reveal a [1]. If it has a [castle], score it and repeat this dogma effect. Otherwise, keep it.",
	"","","")

MetalworkingXX = Card("MetalworkingX",1,"red","deck",
	"crown","crown","none","crown",
	"coop","crown","Draw and reveal a [1]. If it has a [crown], score it and repeat this dogma effect. Otherwise, keep it.",
	"","","")

Metalworking2 = Card("Metalworking",2,"red","deck",
	"castle","castle","none","castle",
	"coop","castle","Draw and reveal a [1]. If it has a [castle], score it and repeat this dogma effect. Otherwise, keep it.",
	"","","")

Metalworking2X = Card("Metalworking",2,"red","deck",
	"castle","castle","none","castle",
	"coop","castle","Draw and reveal a [1]. If it has a [castle], score it and repeat this dogma effect. Otherwise, keep it.",
	"","","")

Metalworking3 = Card("Metalworking",3,"red","deck",
	"castle","castle","none","castle",
	"coop","castle","Draw and reveal a [1]. If it has a [castle], score it and repeat this dogma effect. Otherwise, keep it.",
	"","","")

Metalworking3X = Card("Metalworking",3,"red","deck",
	"castle","castle","none","castle",
	"coop","castle","Draw and reveal a [1]. If it has a [castle], score it and repeat this dogma effect. Otherwise, keep it.",
	"","","")

Metalworking4 = Card("Metalworking",4,"red","deck",
	"castle","castle","none","castle",
	"coop","castle","Draw and reveal a [1]. If it has a [castle], score it and repeat this dogma effect. Otherwise, keep it.",
	"","","")

Metalworking4X = Card("Metalworking",4,"red","deck",
	"castle","castle","none","castle",
	"coop","castle","Draw and reveal a [1]. If it has a [castle], score it and repeat this dogma effect. Otherwise, keep it.",
	"","","")

Oars = Card("Oars",1,"red","deck",
	"castle","crown","none","castle",
	"demand","castle","I demand you transfer a card with a [crown] from your hand to my score pile! If you do, draw a [1].",
	"coop","castle","If no cards were transferred due to this demand, draw a [1].")

OarsX = Card("Oars",1,"red","deck",
	"castle","crown","none","castle",
	"demand","castle","I demand you transfer a card with a [crown] from your hand to my score pile! If you do, draw a [1].",
	"coop","castle","If no cards were transferred due to this demand, draw a [1].")

OarsXX = Card("OarsX",1,"red","deck",
	"bulb","crown","none","bulb",
	"demand","bulb","I demand you transfer a card with a [crown] from your hand to my score pile! If you do, draw a [1].",
	"coop","castle","If no cards were transferred due to this demand, draw a [1].")

Oars2 = Card("Oars",2,"red","deck",
	"castle","crown","none","castle",
	"demand","castle","I demand you transfer a card with a [crown] from your hand to my score pile! If you do, draw a [1].",
	"coop","castle","If no cards were transferred due to this demand, draw a [1].")

Oars2X = Card("Oars",2,"red","deck",
	"castle","crown","none","castle",
	"demand","castle","I demand you transfer a card with a [crown] from your hand to my score pile! If you do, draw a [1].",
	"coop","castle","If no cards were transferred due to this demand, draw a [1].")

Oars3 = Card("Oars",3,"red","deck",
	"castle","crown","none","castle",
	"demand","castle","I demand you transfer a card with a [crown] from your hand to my score pile! If you do, draw a [1].",
	"coop","castle","If no cards were transferred due to this demand, draw a [1].")

Oars3X = Card("Oars",3,"red","deck",
	"castle","crown","none","castle",
	"demand","castle","I demand you transfer a card with a [crown] from your hand to my score pile! If you do, draw a [1].",
	"coop","castle","If no cards were transferred due to this demand, draw a [1].")

Oars4 = Card("Oars",4,"red","deck",
	"castle","crown","none","castle",
	"demand","castle","I demand you transfer a card with a [crown] from your hand to my score pile! If you do, draw a [1].",
	"coop","castle","If no cards were transferred due to this demand, draw a [1].")

Oars4X = Card("Oars",4,"red","deck",
	"castle","crown","none","castle",
	"demand","castle","I demand you transfer a card with a [crown] from your hand to my score pile! If you do, draw a [1].",
	"coop","castle","If no cards were transferred due to this demand, draw a [1].")

## BUILD THE DECK

Deck = Ages((Archery,ArcheryX,ArcheryXX,Metalworking,MetalworkingX,MetalworkingXX,Oars,OarsX,OarsXX),
	(Archery2,Archery2X,Metalworking2,Metalworking2X,Oars2,Oars2X),
	(Archery3,Archery3X,Metalworking3,Metalworking3X,Oars3,Oars3X),
	(Archery4,Archery4X,Metalworking4,Metalworking4X,Oars4,Oars4X))

## DEFINE DOMAINS

Monument = Domain("Monument",
	"Claim this special achievement immediately if you guck six or score six cards during a single turn.")

Empire = Domain("Empire",
	"Claim this special achievement immediately if you have three or more icons of all six types: [bulb] [leaf] [factory] [clock] [crown] [castle].")

Wonder = Domain("Wonder",
	"Claim this special achievement immediately if you have five colors on your board, and each is splayed either up or right.")

World = Domain("World",
	"Claim this special achievement immediately if you have twelve or more [clocks] on your board.")

Universe = Domain("Universe",
	"Claim this special achievement immediately if you have five top cards, and each is of value 8 or higher.")

## BUILD THE DOMINATIONS

arr = range(len(Deck.a1))
random.shuffle(arr)
for i in arr:
	if Deck.a1[i].location == "deck":
		Deck.a1[i].location = "domination"
		break

arr = range(len(Deck.a2))
random.shuffle(arr)
for i in arr:
	if Deck.a2[i].location == "deck":
		Deck.a2[i].location = "domination"
		break

arr = range(len(Deck.a3))
random.shuffle(arr)
for i in arr:
	if Deck.a3[i].location == "deck":
		Deck.a3[i].location = "domination"
		break

arr = range(len(Deck.a4))
random.shuffle(arr)
for i in arr:
	if Deck.a4[i].location == "deck":
		Deck.a4[i].location = "domination"
		break

## DEAL CARDS

arr = range(len(Deck.a1))
random.shuffle(arr)
p1count = 0
p2count = 0
for i in arr:
	if Deck.a1[i].location == "deck" and p1count < 2:
		Deck.a1[i].location = "p1hand"
		p1count = p1count + 1
	if Deck.a1[i].location == "deck" and p2count < 2:
		Deck.a1[i].location = "p2hand"
		p2count = p2count + 1

