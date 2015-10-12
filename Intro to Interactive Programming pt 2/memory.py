# implementation of card game - Memory

import simplegui
import random

deck = []
state = 0
choice1_index = 0
choice2_index = 0


# helper function to initialize globals
def new_game():
    global deck, exposed, turn
    deck = range(0, 8)
    deck.extend(range(0, 8))
    random.shuffle(deck)
    exposed = [False for x in range(0,16)]
    turn = 0
    #for testing print the deck and exposed lists
    #print deck
    #print exposed

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, state, choice1_index, choice2_index, turn
    clicked_index = pos[0]//50
    #print clicked_index #for testing
    if not exposed[clicked_index]:
        exposed[clicked_index] = True
        if state == 0:
            state = 1
            choice1_index = clicked_index
        elif state == 1:
            choice2_index = clicked_index
            state = 2
        elif state == 2:
            if deck[choice1_index] != deck[choice2_index]:
                exposed[choice1_index] = False
                exposed[choice2_index] = False
            choice1_index = clicked_index
            state = 1
        turn += 1
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global deck
    offset = 0
    index = 0
    label.set_text("Moves: " + str(turn))
    for card in deck:
        if exposed[index]:
            canvas.draw_text(str(card), [offset+15, 75], 50, "Green")
        else:
            canvas.draw_polygon([(offset, 0), (offset, 100),  
                                 (offset+50, 100),(offset+50, 0)],  
                                5, "Green")
        offset += 50
        index += 1


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()