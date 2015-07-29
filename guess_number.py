# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

#import libraries
import simplegui
import random


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    secret_number = random.randrange(1,100)



# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    
    # remove this when you add your code    
    pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    
    pass
    
def input_guess(guess):
    # main game logic goes here
    #print out guess string
    print secret_number
    print type(guess)
    print "Guess was ", int(guess)
    if guess > secret_number:
        print "Lower"
    elif guess < secret_number:
        print "Higher"
    else:
        print "Correct"


    
# create frame
frame = simplegui.create_frame('Guess the number', 100, 200)
inp = frame.add_input('Enter guess', input_guess, 50)
button1 = frame.add_button('Range is [0,100)', range100, 150)
button2 = frame.add_button('Range is [0,1000)', range1000, 150)

# register event handlers for control elements and start frame


# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
