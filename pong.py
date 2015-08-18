# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
paddle1_pos = [0, HEIGHT / 2 - HALF_PAD_HEIGHT]
paddle2_pos = [WIDTH, HEIGHT / 2 - HALF_PAD_HEIGHT]


# initialize ball_pos and ball_vel for new ball in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    # Update ball position
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    #ball_vel = [0, 2] # pixels per update (1/60 seconds)
    if direction == RIGHT:
        ball_vel = [random.randrange(120, 240) / 60,random.randrange(60, 180) / 60]
    elif direction == LEFT:
        ball_vel = [random.randrange(120, 240) / 60,-random.randrange(60, 180) / 60]
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(RIGHT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([0, HEIGHT / 2],[WIDTH, HEIGHT / 2], 1, "White")

    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    

    #check vertical position and reverse
    if ball_pos[1] <= BALL_RADIUS:
       ball_vel[1] = - ball_vel[1]
       print "hit1"
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
       ball_vel[1] = - ball_vel[1]
       print "hit2"

    #check horizontal position and reverse
    if ball_pos[0] <= PAD_WIDTH + BALL_RADIUS:
       ball_vel[0] = - ball_vel[0]
       print "hit1"
    if ball_pos[0] >= WIDTH - (PAD_WIDTH + BALL_RADIUS):
       ball_vel[0] = - ball_vel[0]
       print "hit2"
    

            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    def move_up(key):

    
    # draw paddles

    canvas.draw_line((paddle1_pos[0], paddle1_pos[1]), (paddle1_pos[0], paddle1_pos[1] + PAD_HEIGHT), PAD_WIDTH, 'WHITE') #paddle1
    canvas.draw_line((paddle2_pos[0], paddle2_pos[1]), (paddle2_pos[0], paddle2_pos[1] + PAD_HEIGHT), PAD_WIDTH, 'WHITE') #paddle2


    # determine whether paddle and ball collide    
    
    # draw scores
        
def keydown(key):
    global paddle1_vel, paddle2_vel
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
