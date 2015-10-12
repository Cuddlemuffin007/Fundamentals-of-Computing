# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
    def draw_back(self, canvas, pos):
        card_loc = (CARD_BACK_CENTER[0], CARD_BACK_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_BACK_SIZE, 
                          [pos[0] + CARD_BACK_CENTER[0] + 1, 
                           pos[1] + CARD_BACK_CENTER[1] + 1], 
                          CARD_BACK_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        hand = ""
        for card in self.hand:
            hand += (str(card) + " ")
        return "Hand contains " + hand.strip()

    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        hand_value = 0
        contains_ace = False
        for card in self.hand:
            hand_value += VALUES[card.get_rank()]
            if card.get_rank() == 'A':
                contains_ace = True
        if contains_ace and hand_value < 12:
                hand_value += 10
        return hand_value
   
    def draw(self, canvas, pos):
        for card in self.hand:
            pos[0] = pos[0] + CARD_SIZE[0] + 20
            card.draw(canvas, pos)
    
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()
    
    def __str__(self):
        # return a string representing the deck
        deck = ""
        for card in self.deck:
            deck += (str(card) + " ")
        return "Deck contains " + deck.strip()



#define event handlers for buttons
def deal():
    global outcome, in_play, game_deck, player_hand, dealer_hand, score
    
    if in_play:
        score -= 1
        in_play = False
        deal()
    else:
        game_deck = Deck()
        player_hand = Hand()
        dealer_hand = Hand()
        game_deck.shuffle()
        player_hand.add_card(game_deck.deal_card())
        player_hand.add_card(game_deck.deal_card())
        dealer_hand.add_card(game_deck.deal_card())
        dealer_hand.add_card(game_deck.deal_card())
        outcome = "Hit or Stand?"
        in_play = True
        print "Player: " + str(player_hand), player_hand.get_value()
        print "Dealer: " + str(dealer_hand), dealer_hand.get_value()

def hit():
    global outcome, in_play, game_deck, player_hand, score
    # if the hand is in play, hit the player
    if in_play:
        if player_hand.get_value() < 22:
            player_hand.add_card(game_deck.deal_card())
            if player_hand.get_value() > 21:
                outcome = "Player Busted. New Deal?"
                score -= 1
                in_play = False
    print "Player: " + str(player_hand), player_hand.get_value()
    print "Dealer: " + str(dealer_hand), dealer_hand.get_value()
    
def stand():
    global outcome, in_play, game_deck, dealer_hand, score
    if in_play:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(game_deck.deal_card())
        if dealer_hand.get_value() > 21:
            outcome = "Dealer Busted. You win!"
            score += 1
            in_play = False
        elif dealer_hand.get_value() > player_hand.get_value():
            outcome = "Dealer wins!"
            score -= 1
            in_play = False
        elif dealer_hand.get_value() < player_hand.get_value():
            outcome = "Player wins!"
            score += 1
            in_play = False
        elif dealer_hand.get_value() == player_hand.get_value():
            outcome = "Hands tie, so you lose! Thanks house edge!"
            score -= 1
            in_play = False
    print "Player: " + str(player_hand), player_hand.get_value()
    print "Dealer: " + str(dealer_hand), dealer_hand.get_value()
    

# draw handler    
def draw(canvas):
    canvas.draw_text("Blackjack", (60, 80), 50, "Black")
    canvas.draw_text("Score: " + str(score), (450, 80), 33, "Black")
    canvas.draw_text("Dealer", (30, 155), 25, "Black")
    dealer_hand.draw(canvas, [-65, 180])
    canvas.draw_text("Player", (30, 355), 25, "Black")
    player_hand.draw(canvas, [-65, 380])
    canvas.draw_text(outcome, (30, 550), 33, "Black")
    if in_play:
        dealer_hand.hand[0].draw_back(canvas, [26, 180])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()