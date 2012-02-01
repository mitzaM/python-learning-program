#!/usr/bin/env python

ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
suits = ["Spades", "Diamonds", "Clubs", "Hearts"]


class Card:
    def __init__(self):
	self.rank = ""
	self.suit = ""


    def __init__(self, rank, suit):
	self.rank = rank
	self.suit = suit


    def __str__(self):
	return self.rank + " of " + self.suit


    def getRank(self):
	return self.rank


    def getSuit(self):
	return self.suit


class Hand:
    def __init__(self):
	self.cards = []


    def __str__(self):
	result = ''
	for card in self.cards:
	    result += '(' + card.rank + ', ' + card.suit + ') '
	return result


    def clear(self):
	self.cards = []


    def add(self, card):
	self.cards.append(card)


    def remove(self, card):
	self.cards.remove(card)


    def give(self, card, hand):
	self.remove(card)
	hand.add(card)


class Deck(Hand):
    def populate(self):
	for s in suits:
	    for r in ranks:
		self.add(Card(r, s))


    def get_top_card(self):
	if self.cards:
	    return self.cards[0]
	else:
	    return False


    def shuffle(self):
	import random
	random.shuffle(self.cards)


    def deal(self, hands, table):
	for _ in range(2):
	    for hand in hands:
		card = self.get_top_card()
		if not card:
		    print "No more cards left"
                    return
		self.give(card, hand)

	card = self.get_top_card()
	if not card:
	    print "No more cards left"
	    return
	self.remove(card)
	for _ in range(3):
	    card = self.get_top_card()
	    if not card:
		print "No more cards left"
		return
	    self.give(card, table)

	for _ in range(2):
	    card = self.get_top_card()
	    if not card:
		print "No more cards left"
		return
	    self.remove(card)
	    card = self.get_top_card()
	    if not card:
		print "No more cards left"
		return
	    self.give(card, table)


d = Deck()
d.populate()
d.shuffle()

table = Hand()
hands = []
for _ in range(5):
    hands.append(Hand())
d.deal(hands, table)

print 'cards on table:'
for card in table.cards:
    print ' ', card

print '\nplayer cards:'
for hand in hands:
    for card in hand.cards:
	print ' ', card
    print ''
