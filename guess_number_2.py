# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

#import libraries
import simplegui
import random

max_range = 100


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    print "Starting a new game!"
    global secret_number, max_range
    secret_number = random.randrange(1,max_range)
    print max_range


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global max_range
    max_range = 100 
    print "Starting new game with range 1 - 100 \n"
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global max_range
    max_range = 1000
    print max_range
    print "Starting new game with range 1 - 1000 \n"
    new_game()
    
def input_guess(guess):
    # main game logic goes here
    print "Secret number: ", secret_number
    print "Guess was ", guess
    if secret_number > int(guess):
        print "Higher"
    elif secret_number < int(guess):
        print "Lower"
    else:
        print "Correct"

    
# create frame
frame = simplegui.create_frame('Guess the number', 100, 150)
inp = frame.add_input('Enter guess', input_guess, 50)
button1 = frame.add_button('Range is [0,100)', range100, 150)
button2 = frame.add_button('Range is [0,1000)', range1000, 150)
frame.start()

# register event handlers for control elements and start frame


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
