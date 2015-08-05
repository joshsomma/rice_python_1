# template for "Stopwatch: The Game"

#import libraries
import simplegui

# define global variables
count = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"


# define event handler for timer with 0.1 sec interval
def timer_handler():
    global count
    count += 1
    print count

# define draw handler
def draw_handler(canvas):
    global count
    canvas.draw_text(str(count), (20, 20), 12, 'Red')
    
# create frame
frame = simplegui.create_frame('Testing', 200, 200)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)
timer.start()

# start frame
frame.start()

# Please remember to review the grading rubric
