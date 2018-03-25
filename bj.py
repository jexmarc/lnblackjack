#!/usr/bin/python3

from random import shuffle
import time

# Define the deck made up of card ranks and suits
ranks = [_ for _ in range(2, 11)] + ['JACK', 'QUEEN', 'KING', 'ACE']
suits = ['SPADE', 'HEART', 'DIAMOND', 'CLUB']


def get_deck():
	"""Return a new deck of unshuffled cards."""
	return [[rank, suit] for rank in ranks for suit in suits]


def card_value(card):
	"""Returns the integer value of a single card."""

	rank = card[0]
	if rank in ranks[0:-4]:
		return int(rank)
	elif rank is 'ACE':
		return 11
	else:
		return 10


def hand_value(hand):
	"""Returns the integer value of a set of cards"""

	# Sum up the cards in the deck.
	tmp_value = sum(card_value(_) for _ in hand)
	# Count aces
	num_aces = len([_ for _ in hand if _[0] is 'ACE'])

	# Aces are 1 or 11. If it is possible to bring the value of
	# the hand under 21 by making 11 -> 1 subs, do so.
	while num_aces > 0:
		if tmp_value > 21 and 'ACE' in ranks:
			tmp_value -= 10
			num_aces -= 1
		else:
			break
	  # Return a string and int for value of hand.
	  # If hand is busted, return 100.
	if tmp_value < 21:
	  return [str(tmp_value), tmp_value]
	elif tmp_value == 21 and len(hand) == 2:
	  return ['BLACKJACK!', 21]
	elif tmp_value == 21 and len(hand) > 2:
		return ['21', 21]
	else:
	  return ['BUSTED!', 100]

playing = True
while playing:
	# Get a new deck of cards
	print('\nGrabbing a new deck...')
	time.sleep(1)
	deck = get_deck()

	# Shuffle the deck
	print('Shuffling...')
	time.sleep(1)
	shuffle(deck)

	# Deal hands
	print('Dealing...')
	time.sleep(1)
	player_hand=[deck.pop(),deck.pop()]
	dealer_hand=[deck.pop(),deck.pop()]

	# Show dealer face up card
	print('\nDealer shows face up: {}'.format(dealer_hand[0]))
	
	player_in = True
	
	while player_in:
		print('Your Hand: {} [{}]'.format(player_hand, hand_value(player_hand)[0]))
		if hand_value(player_hand)[1] == 100:
			break
	
		if player_in:
			response = int(input('Hit or Stay? (Hit = 1, Stay = 0):'))
			# If player "hits" take first card from top of deck into hand.
			# If player "stays" change player_in to false and move on to 
			# the dealer's hand.
			if response:
				player_in = True
				new_player_card = deck.pop()
				player_hand.append(new_player_card)
				print('You draw {}'.format(new_player_card))
			else:
				player_in = False
	
	player_score_label, player_score = hand_value(player_hand)
	dealer_score_label, dealer_score = hand_value(dealer_hand)
	
	if 'BLACKJACK' in player_score_label:
		print('Dealer shows hand: {} [{}]'.format(dealer_hand, hand_value(dealer_hand)[0]))
		print('Natural Blackjack!!! YOU WIN!!!')
	elif player_score <= 21:
		print('Dealer shows hand: {} [{}]'.format(dealer_hand, hand_value(dealer_hand)[0]))
		while hand_value(dealer_hand)[1] < 17:
			new_dealer_card = deck.pop()
			dealer_hand.append(new_dealer_card)
			print('Dealer draws {} [{}]'.format(new_dealer_card, hand_value(dealer_hand)[0]))
	
		dealer_score_label, dealer_score = hand_value(dealer_hand)
	
		if player_score < 100 and dealer_score == 100:
			print('Dealer Busts. YOU WIN!')
		elif player_score > dealer_score:
			print('YOU WIN!')
		elif player_score == dealer_score:
			print('PUSH (tie)')
		elif player_score < dealer_score:
			print('Dealer Wins.')
	else:
		print('Dealer shows hand: {} [{}]'.format(dealer_hand, hand_value(dealer_hand)[0]))
		print('Dealer Wins.')
	
	

	keep_playing = int(input('\nPlay Again? (Yes = 1, No = 0):'))
	if keep_playing == False:
		exit(0)





