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

paddle1_pos = HEIGHT / 2.5
paddle2_pos = HEIGHT / 2.5
paddle1_vel = 0
paddle2_vel = 0
paddle_vel = 5


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    ball_vel_x = random.randrange(120, 240)/60.0
    ball_vel_y = - random.randrange(60, 180)/60.0
    
    if direction == LEFT:
        ball_vel_x = - ball_vel_x
        
    
    ball_vel = [ball_vel_x, ball_vel_y]    
    

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_pos = HEIGHT / 2.5
    paddle2_pos = HEIGHT / 2.5

    spawn_ball(RIGHT)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # check for collision with TOP or BOTTOM of canvas and reflection
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    
    #check for collision with LEFT or RIGHT gutters and call spawn in the opposite direction
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if ball_pos[1] >= paddle1_pos and ball_pos[1] <= (paddle1_pos + PAD_HEIGHT):
            # reflects ball horizontally right
            ball_vel[0] = abs(ball_vel[0])
            # increase velocity by 10%
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
        else:
            spawn_ball(RIGHT)
            score2 += 1
    elif ball_pos[0] >= (WIDTH - 1) - (BALL_RADIUS + PAD_WIDTH):
        if ball_pos[1] >= paddle2_pos and ball_pos[1] <= (paddle2_pos + PAD_HEIGHT):
        # reflects ball horizontally right
            ball_vel[0] = - ball_vel[0]
        # increase velocity by 10%
            ball_vel[0] *= 1.1
            ball_vel[1] *= 1.1
        else:
            spawn_ball(LEFT)
            score1 += 1
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos <= HEIGHT - PAD_HEIGHT and paddle1_vel > 0) or (paddle1_pos >= 0 and paddle1_vel < 0) :
        paddle1_pos += paddle1_vel    
    elif (paddle2_pos <= HEIGHT - PAD_HEIGHT and paddle2_vel > 0) or (paddle2_pos >= 0 and paddle2_vel < 0) :
        paddle2_pos += paddle2_vel 
    
    # draw paddles
    # left paddle (paddle1)
    canvas.draw_polygon([[0, paddle1_pos], 
                         [PAD_WIDTH, paddle1_pos], 
                         [PAD_WIDTH, paddle1_pos + PAD_HEIGHT], 
                         [0, paddle1_pos + PAD_HEIGHT]], 1, "White", "White")
    
    # right paddle (paddle2)
    canvas.draw_polygon([[WIDTH, paddle2_pos], 
                         [WIDTH - PAD_WIDTH, paddle2_pos], 
                         [WIDTH - PAD_WIDTH, paddle2_pos + PAD_HEIGHT], 
                         [WIDTH, paddle2_pos + PAD_HEIGHT]], 1, "White", "White")
    
    # determine whether paddle and ball collide
    # left paddle - ball collision detection
    
    # draw scores
    canvas.draw_text(str(score1), [225, 50], 48, "White")
    canvas.draw_text(str(score2), [350, 50], 48, "White")
def keydown(key):
    global paddle1_vel, paddle2_vel
    
    #left paddle    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -paddle_vel     
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = paddle_vel  
    
    #right paddle
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = paddle_vel    
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -paddle_vel
    
def keyup(key):
    global paddle1_vel, paddle2_vel

    #left paddle
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
        
    #right paddle
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0

def reset():
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
reset = frame.add_button("Reset", reset, 50)

# start frame
new_game()
frame.start()