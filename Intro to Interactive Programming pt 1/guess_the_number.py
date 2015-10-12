# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

# helper function to start and restart the game
def new_game(num_range = 100):
    # initialize global variables used in your code here
    global secret_number
    global guesses
    global game_range
    game_range = num_range
    if num_range == 1000:
        guesses = 10
    else:
        guesses = 7
    secret_number = random.randint(0, num_range)
    print "Range of the secret number is 0 to", num_range
    print "Remaining guesses:", guesses
    #prints the secret number for testing
    #print "Secret number is %s" % secret_number


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    num_range = 100
    new_game(num_range)

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    num_range = 1000
    new_game(num_range)
    
def input_guess(guess):
    # main game logic goes here
    global num_range
    global guesses
    guess = int(guess)
    print "Guess was %g" % guess
    if guesses >= 1:
        if guess > secret_number:
            print "Lower"
            guesses -= 1
            print "Remaining guesses:", guesses
        elif guess < secret_number:
            print "Higher"
            guesses -= 1
            print "Remaining guesses:", guesses
        elif guess == secret_number:
            print "Correct!"
            new_game(game_range)
    else:
        print "Out of guesses. Secret number was", secret_number
        new_game(game_range)

    
# create frame
frame = simplegui.create_frame('Guess the Number', 200, 200)

# register event handlers for control elements and start frame
inp = frame.add_input("Enter Guess:", input_guess, 50)
range100 = frame.add_button("Number 0 to 100", range100, 130)
range1000 = frame.add_button("Number 0 to 1000", range1000, 130)

frame.start()

# call new_game 
new_game()
