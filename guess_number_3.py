# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

#import libraries
import simplegui
import random

#set initial global value for max range and number of guesses
max_range = 100
number_tries = 7

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, max_range, player_tries
    #print welcome message
    print "Guess the number between 1 and ", max_range, "\n"
    #generate the secret number
    secret_number = random.randrange(1,max_range)
    #set player tries to one
    player_tries = 0

#define event handlers for control panel
def range100():
    #button that changes the range to [0,100) and starts a new game
    global max_range, number_tries #import globals
    max_range = 100 #set max range
    number_tries = 7 #set number of tries
    print "Starting new game with range 1 - ",max_range #print welcome message
    print "You have ",number_tries, "attempts \n"
    new_game() #start new game

def range1000():
    # button that changes the range to [0,1000) and starts a new game 
    global max_range, number_tries #import globals
    max_range = 1000 #set max range
    number_tries = 10 #set number of tries
    print "Starting new game with range 1 - ", max_range #print welcome message
    print "You have ",number_tries, "attempts \n"
    new_game() #start new game

def input_guess(guess):
    global player_tries, number_tries, max_range #import globals
    player_tries += 1 #increment player attempts
    player_guess = int(guess) #store player guess as int
    if player_guess > max_range or player_guess < 0: #check for a guess within the range and reset the game if not
        print "Invalid guess, please guess within 1 and ", max_range
        print "Resetting the game \n"
        new_game()
    else: # check the guess against secret number and return result to player
        print "Guess was ", guess
        if secret_number > player_guess:
            print "Higher, guess again"
            print "Guesses left: ",number_tries - player_tries,"\n"
        elif secret_number < player_guess:
            print "Lower, guess again"
            print "Guesses left: ",number_tries - player_tries,"\n"
        else:
            print "Correct, restarting the game\n"
            new_game()
    if player_tries >= number_tries: #reset game if no more attempts left
        print "The secret number was ", secret_number
        print "Sorry, you have run out of attempts, restarting the game \n"
        new_game()

# create frame
frame = simplegui.create_frame('Guess the number', 100, 150)

# register event handlers for control elements and start frame
inp = frame.add_input('Enter guess', input_guess, 50)
button1 = frame.add_button('Range is [0,100)', range100, 150)
button2 = frame.add_button('Range is [0,1000)', range1000, 150)
frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
