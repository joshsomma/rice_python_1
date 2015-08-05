# Testing template for format function in "Stopwatch - The game"

###################################################
# Student should add code for the format function here
#desired format

def format(t):
    total = ""
    #calc minutes
    a = t // 600
    #calc first part of seconds
    b = ((t // 10) % 60) // 10
    #calc second part of seconds
    c = ((t // 10) % 60) % 10
    #calc 10ths of seconds
    d = t % 10
    total = str(a) + ":" + str(b) + str(c) + "." + str(d)
    return total

###################################################
# Test code for the format function
# Note that function should always return a string with 
# six characters


print format(0)
print format(7)
print format(17)
print format(60)
print format(63)
print format(214)
print format(599)
print format(600)
print format(602)
print format(667)
print format(1325)
print format(4567)
print format(5999)

###################################################
# Output from test

#0:00.0
#0:00.7
#0:01.7
#0:06.0
#0:06.3
#0:21.4
#0:59.9
#1:00.0
#1:00.2
#1:06.7
#2:12.5
#7:36.7
#9:59.9

