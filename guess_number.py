# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

#import libraries
import simplegui
import random

max_range = 100

# helper function to start and restart the game
def new_game(max):
    # initialize global variables used in your code here
    frame.start()
    global secret_number, max_guesses
    max_guesses = 0
    secret_number = random.randrange(1,max)

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    new_game(100)

def range1000():
    # button that changes the range to [0,1000) and starts a new game
    new_game(1000)
    
def input_guess(guess):
    # main game logic goes here
    #print out guess string
    global max_guesses
    if max_guesses <= 7:
        print secret_number
        print "Guess was ", guess
        if int(guess) > secret_number:
            print "Lower"
        elif int(guess) < secret_number:
            print "Higher"
        else:
            print "Correct"
            new_game(100)
        max_guesses += 1
    else:
        print "sorry, out of guesses"
        new_game()

# create frame
frame = simplegui.create_frame('Guess the number', 100, 150)
inp = frame.add_input('Enter guess', input_guess, 50)
button1 = frame.add_button('Range is [0,100)', range100, 150)
button2 = frame.add_button('Range is [0,1000)', range1000, 150)
frame.start()

# register event handlers for control elements and start frame


# call new_game 
new_game(max_range)


# always remember to check your completed program against the grading rubric
