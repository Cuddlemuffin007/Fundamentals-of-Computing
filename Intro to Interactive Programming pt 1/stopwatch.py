# template for "Stopwatch: The Game"

import simplegui

# define global variables
tenths = 0
stop_counter = 0
whole_num_counter = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    a = str((t / 100) / 6)
    b = str(t / 100 % 6)
    c = str(t / 10 % 10)
    d = str(t % 10)
    return a + ":" + b + c + "." + d

# helper function to draw counters
def render_counters(x, y):
    return str(x) + "/" + str(y)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    timer.start()

def stop_handler():
    global stop_counter, whole_num_counter
    if timer.is_running():
        timer.stop()
        stop_counter += 1
        if tenths % 10 == 0:
            whole_num_counter += 1
    
    

def reset_handler():
    global tenths, stop_counter, whole_num_counter
    timer.stop()
    tenths = 0
    stop_counter = 0
    whole_num_counter = 0


# define event handler for timer with 0.1 sec interval
def timer_handler():
    global tenths
    tenths += 1


# define draw handler
def draw(canvas):
    global tenths
    canvas.draw_text(format(tenths), [75, 110], 60, "Green")
    canvas.draw_text(render_counters(whole_num_counter, stop_counter), [225, 30], 36, "Green")
    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)
start = frame.add_button("Start", start_handler, 50)
stop = frame.add_button("Stop", stop_handler, 50)
reset = frame.add_button("Reset", reset_handler, 50)
timer = simplegui.create_timer(100, timer_handler)

# register event handlers
frame.set_draw_handler(draw)

# start frame
frame.start()