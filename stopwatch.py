# template for "Stopwatch: The Game"

#import libraries
import simplegui

# define global variables
count = 0 #set the timer
attempts = 0 #set number of attempts the user has made
hits = 0 # set number of hits the user has made
running = True #value for if clock is running or not
d = 0 #create global for 10ths second value to check game

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global d
    total = ""
    a = t // 600 #calc minutes
    b = ((t // 10) % 60) // 10 #calc first part of seconds
    c = ((t // 10) % 60) % 10 #calc second part of seconds
    d = t % 10 #calc 10ths of seconds
    total = str(a) + ":" + str(b) + str(c) + "." + str(d) #format string
    return total
    
def start_button(): # start timer, set running to true
	global running
	timer.start()
	running = True

def stop_button(): 
	global d, hits, attempts, running
	timer.stop() #stop timer
	if running: # eval stop time for hit and increment if yes
		if d == 0:
			hits += 1
		attempts += 1 #increment attempts
	running = False #set running to false
	print d
	print hits

def reset_button():
	global count, hits, attempts
	count = 0
	hits = 0
	attempts = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global count
    count += 1

# define draw handler
def draw_handler(canvas):
    global count, attempts, hits
    canvas.draw_text(format(count), (75, 100), 24, 'Red') #draw timer
    canvas.draw_text(str(hits) + " / " + str(attempts), (150, 25), 24, 'White') #draw number of attempts

# create frame
frame = simplegui.create_frame('Stopwatch', 200, 200)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)
startButton = frame.add_button('Start', start_button, 100)
stopButton = frame.add_button('Stop', stop_button, 100)
resetButton = frame.add_button('Reset', reset_button, 100)
frame.set_draw_handler(draw_handler)


# start frame
frame.start()

# Please remember to review the grading rubric
