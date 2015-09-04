# implementation of card game - Memory

import simplegui
import random

#globals
frame_size = [800,100]
l1 = range(1,9) + range(1,9)
random.shuffle(l1)
#exposed =  [False for l in range(len(l1))]
exposed = [True, False, True, False, True, False, True, False, True, False, True, False, True, False, True, False]

# helper function to initialize globals
def new_game():
    global l1



# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass


# cards are logically 50x100 pixels in size
def draw(canvas):
    global l1,exposed
    draw_letter = 10
    sq_tr = [0,0]
    sq_tl = [50,0]
    sq_br = [50,100]
    sq_bl = [0,100]
    for n in l1:
        for v in exposed:
            if v == True:
                canvas.draw_text(str(n), (draw_letter,80), 72, 'WHITE')
            else:
                canvas.draw_polygon([sq_tr, sq_tl,sq_br,sq_bl], 2, 'Orange', 'Green')

        draw_letter += 50
        sq_tr[0] += 50
        sq_tl[0] += 50
        sq_br[0] += 50
        sq_bl[0] += 50

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", frame_size[0], frame_size[1])
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
