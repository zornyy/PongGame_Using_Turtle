# Made by ZORNY -_-

import turtle, time, random

# Basics -----------------------------------------------------
# Create Window
master = turtle.Screen()
master.cv._rootwindow.resizable(False, False)
master.title("Zy PONG")
master.bgcolor("black")
master.setup(width=800, height=600)
master.tracer(0)

# Variables
game_started = False
scoreA = 0
scoreB = 0
scoreDisplay = f"Player A: {scoreA}     |     Player B: {scoreB}"

loops = 0

# Objects creation ----------------------------------------

# Game
paddle_a = turtle.Turtle()
paddle_b = turtle.Turtle()
ball = turtle.Turtle()
ball.dx = 2
ball.dy = 2

pen = turtle.Turtle()
# Menu
title = turtle.Turtle()
subtitle = turtle.Turtle()
keys_instructions = turtle.Turtle()
# End
winner_announcment = turtle.Turtle()
retry_proposal = turtle.Turtle()



# Functions ----------------------------------------------------
def get_start_direction():
    poss = [1, -1]
    ball.dx *= random.choice(poss)
    ball.dy *= random.choice(poss)

def reset_game():
    get_start_direction()
    paddle_a.goto(-350, 0)
    paddle_b.goto(350, 0)
    ball.goto(0, 0)

def paddle_a_up():
    y = paddle_a.ycor()
    if y < 300 -60:
        paddle_a.sety(y+20)
    
def paddle_a_down():
    y = paddle_a.ycor()
    if y > -300 + 60:
        paddle_a.sety(y-20)  
    
def paddle_b_up():
    y = paddle_b.ycor()
    if y < 300 -60:
        paddle_b.sety(y+20)
    
def paddle_b_down():
    y = paddle_b.ycor()
    if y > -300 + 60:
        paddle_b.sety(y-20)

def start_game():
    global game_started
    if game_started == False:
        game_started = True
        
        # Reset speed
        ball.dx = 2
        ball.dy = 2
        
        # Clear Screen 
        title.clear()
        subtitle.clear()
        keys_instructions.clear()
        winner_announcment.clear()
        retry_proposal.clear()
        
        # Clear Variables
        global scoreA
        scoreA = 0
        global scoreB
        scoreB = 0
        
        scoreDisplay = f"Player A: {scoreA}     |     Player B: {scoreB}"
        
        
        #Create OBJECTS ----------------------------------------

        # Paddle A
        paddle_a.speed(0)
        paddle_a.shape("square")
        paddle_a.shapesize(stretch_wid=5, stretch_len=1)
        paddle_a.color("White")
        paddle_a.penup()
        paddle_a.goto(-350, 0)

        # Paddle B
        paddle_b.speed(0)
        paddle_b.shape("square")
        paddle_b.shapesize(stretch_wid=5, stretch_len=1)
        paddle_b.color("White")
        paddle_b.penup()
        paddle_b.goto(350, 0)

        # Ball
        ball.speed(0)
        ball.shape("square")
        ball.color("White")
        ball.penup()
        ball.goto(0, 0)
        

        # Score Display
        pen.speed(0)
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 260)
        pen.write(scoreDisplay, align="center", font=("Courier", 24, "normal"))
        # -------------------------------------------------

        # Keyboard binding
        master.listen()
        master.onkeypress(paddle_a_up, "w")
        master.onkeypress(paddle_a_down, "s")

        master.onkeypress(paddle_b_up, "Up")
        master.onkeypress(paddle_b_down, "Down")
        
        time.sleep(1)

def menu():
    
    # Objects
    title.speed(0)
    title.color("white")
    title.penup()
    title.hideturtle()
    title.goto(0, 140)
    title.write("Welcome to ZORNY's PONG", align="center", font=("Courier", 35, "normal"))
    
    subtitle.speed(0)
    subtitle.color("white")
    subtitle.penup()
    subtitle.hideturtle()
    subtitle.goto(0, 50)
    subtitle.write("Press \"k\" to start", align="center", font=("Courier", 18, "normal"))
    
    keys_instructions.speed(0)
    keys_instructions.color("white")
    keys_instructions.penup()
    keys_instructions.hideturtle()
    keys_instructions.goto(0, -160)
    keys_instructions.write("Press \"w\", \"s\" or \"Up\", \"Down\" to move the paddles !\n\n             First to five points wins", align="center", font=("Courier", 11, "normal"))
    
   
    master.listen()
    master.onkeypress(start_game, "k")
    
def end(winner):
    paddle_a.clear()
    paddle_b.clear()
    ball.clear()
    pen.clear()
    
    winner_announcment.speed(0)
    winner_announcment.color("white")
    winner_announcment.penup()
    winner_announcment.hideturtle()
    winner_announcment.goto(0, 140)
    winner_announcment.write(f"Player {winner} WINS", align="center", font=("Courier", 35, "normal"))
    
    retry_proposal.speed(0)
    retry_proposal.color("white")
    retry_proposal.penup()
    retry_proposal.hideturtle()
    retry_proposal.goto(0, 0)
    retry_proposal.write("Press \"k\" to startover :))", align="center", font=("Courier", 15, "normal"))
    
    global game_started
    game_started = False

def increase_speed():
    if ball.dx < 0:
        ball.dx -= 1
    else:
        ball.dx += 1
    if ball.dy < 0:
        ball.dy -= 1
    else:
        ball.dy += 1
        
    global loops
    loops += 1

# Starting DISPLAY ------------------------------------------        
menu()
get_start_direction()


# Main loop ------------------------------------------------------
while True:
    master.update()
        
    if game_started == True:
        
        # Verify speed
        if loops == 10 or loops == 20 or loops == 30 or loops == 40 or loops == 50:
            increase_speed()
        
        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        time.sleep(0.01)
        
        
        # Bounce on the ceiling ang flore
        if ball.ycor() >= 290 or ball.ycor() <= -280:
            ball.dy = ball.dy * (-1)
        
        # Bounce on the paddle A
        if ball.xcor() < paddle_a.xcor() + 20 and ball.dx < 0:
            if ball.ycor() > paddle_a.ycor() - 50 and ball.ycor() < paddle_a.ycor() + 50 :
                ball.dx *= -1
                loops += 1
                
        # Bounce on the paddle B
        if ball.xcor() > paddle_b.xcor() - 20 and ball.dx > 0:
            if ball.ycor() > paddle_b.ycor() - 50 and ball.ycor() < paddle_b.ycor() + 50 :
                ball.dx *= -1
                loops += 1
                
        # End if someone loose and restart        
        if ball.xcor() >= 380 :
            scoreA += 1
            if scoreA < 5:
                scoreDisplay = f"Player A: {scoreA}     |     Player B: {scoreB}"
                pen.clear()
                pen.write(scoreDisplay, align="center", font=("Courier", 24, "normal"))
                reset_game()
            else:
                end("A")
            
            
        if ball.xcor() <= -380 :
            scoreB += 1
            if scoreB < 5:
                scoreDisplay = f"Player A: {scoreA}     |     Player B: {scoreB}"
                pen.clear()
                pen.write(scoreDisplay, align="center", font=("Courier", 24, "normal"))
                reset_game()
            else:
                end("B")
                
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠛⠛⠉⠉⠉⠋⠛⠛⠛⠻⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠛⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠏⠄⠄⠄⠄⠄⠄⠄⠂⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠹⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠠⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠘⢻⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⠄⢠⠄⠄⡀⠄⠄⢀⠂⠄⠄⠄⠄⠄⠄⠄⠄⠄⡁⠄⠄⢛⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠐⡈⢔⠸⣐⢕⢕⢵⢰⢱⢰⢐⢤⡡⡢⣕⢄⢢⢠⠄⠄⠄⠄⠄⠄⠙⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡁⠂⠅⢕⠌⡎⡎⣎⢎⢮⢮⣳⡳⣝⢮⢺⢜⢕⢕⢍⢎⠪⡐⠄⠁⠄⠸⣿⣿
# ⣿⣿⣿⣿⣿⣿⠏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠐⠄⠄⢅⠣⡡⡣⣣⡳⡵⣝⡮⣗⣗⡯⣗⣟⡮⡮⣳⣣⣳⢱⢱⠱⣐⠄⠂⠄⢿⣿
# ⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⠄⠄⠂⠄⠄⠄⠄⠄⠄⢂⢈⠢⡱⡱⡝⣮⣿⣟⣿⣽⣷⣿⣯⣿⣷⣿⣿⣿⣾⣯⣗⡕⡇⡇⠄⠂⡀⢹⣿
# ⣿⣿⣿⣿⣿⡟⠄⠄⠄⠄⠄⠄⠂⠄⠄⠄⠄⠄⠄⠐⢀⢂⢕⢸⢨⢪⢳⡫⣟⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡺⡮⡣⡣⠠⢂⠒⢸⣿
# ⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠠⠐⠄⡂⠆⡇⣗⣝⢮⢾⣻⣞⣿⣿⣿⣿⣿⣿⣿⣿⢿⣽⣯⡯⣺⢸⢘⠨⠔⡅⢨⣿
# ⣿⣿⠋⠉⠙⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠁⠄⠄⠄⡂⡪⡪⡪⡮⡮⡯⣻⣽⣾⣿⣿⣿⣟⣿⣿⣿⣽⣿⣿⡯⣯⡺⡸⡰⡱⢐⡅⣼⣿
# ⣿⠡⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠠⠈⠆⠱⠑⠝⠜⠕⡝⡝⣞⢯⢿⣿⣿⡿⣟⣿⣿⣿⡿⡿⣽⣷⣽⡸⡨⡪⣂⠊⣿⣿
# ⣿⠡⠄⡨⣢⠐⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠐⠍⡓⣗⡽⣝⠽⠍⠅⠑⠁⠉⠘⠘⠘⠵⡑⢜⢀⢀⢉⢽
# ⣿⠁⠠⢱⢘⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠈⠱⣁⠜⡘⠌⠄⠄⡪⣳⣟⡮⢅⠤⠠⠄⠄⣀⣀⡀⡀⠄⠈⡂⢲⡪⡠⣿
# ⣿⡇⠨⣺⢐⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡀⠄⠄⠄⠤⡠⡢⢒⠦⠠⠄⠄⠄⡸⢽⣟⢮⠢⡂⡐⠄⡈⡀⠤⡀⠄⠑⢄⠨⢸⡺⣐⣿
# ⣿⣿⠈⠕⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡂⡪⡐⡥⢤⣰⣰⣰⡴⡮⠢⠂⠄⠄⡊⢮⢺⢕⢵⢥⡬⣌⣒⡚⣔⢚⢌⢨⢚⠌⣾⡪⣾⣿
# ⣿⣿⣆⠄⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡑⢕⢕⡯⡷⣕⢧⢓⢭⠨⡀⠄⡂⠨⡨⣪⡳⣝⢝⡽⣻⣻⣞⢽⣲⢳⢱⢡⠱⠨⣟⢺⣿⣿
# ⣿⣿⣿⡆⠄⡅⠇⡄⠄⠄⠄⠄⠄⠄⠄⠐⠨⢪⢹⢽⢽⣺⢝⠉⠁⠁⠄⠄⠄⢌⢎⡖⡯⡎⡗⢝⠜⣶⣯⣻⢮⡻⣟⣳⡕⠅⣷⣿⣿⣿
# ⣿⣿⣿⣿⣶⣶⣿⣷⠄⠄⠄⠄⠄⠄⠄⠄⠈⠔⡑⠕⠝⠄⡀⠄⠄⠊⢆⠂⠨⡪⣺⣮⣿⡾⡜⣜⡜⣄⠙⢞⣿⢿⡿⣗⢝⢸⣾⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⡀⠄⠄⠄⠄⢀⠄⠠⠄⠠⠄⠄⠄⠄⠄⠄⠊⠺⡹⠳⡙⡜⡓⡭⡺⡀⠄⠣⡻⡹⡸⠨⣣⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⠄⠄⠠⠄⠄⣂⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢄⠤⡤⡄⡆⡯⡢⡣⡣⡓⢕⠽⣄⠄⠨⡂⢌⣼⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠈⠆⠄⠸⡂⠄⠄⠄⢀⠄⢀⠈⠄⠂⠁⠙⠝⠼⠭⠣⠣⠣⠑⠌⠢⠣⡣⡠⡘⣰⣱⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⢑⠄⠈⡱⠄⢘⠄⡀⠨⢐⣧⣳⣷⣶⣦⣤⣴⣶⣶⣶⡶⠄⡠⡢⡕⣜⠎⡮⣣⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠢⠄⠨⠄⠄⠣⡀⠄⢀⢀⢙⠃⡿⢿⠿⡿⡿⢟⢋⢔⡱⣝⢜⡜⡪⡪⣵⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⡁⠄⠄⠄⠄⠄⠄⠄⠅⠄⠡⠄⠄⠡⢀⢂⠢⡡⠡⠣⡑⣏⢯⡻⡳⣹⡺⡪⢎⠎⡆⢣⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⣇⠄⠄⠄⠄⠄⠄⠄⠐⠄⠄⠁⠄⢈⠄⢂⠕⡕⡝⢕⢎⢎⢮⢎⢯⢺⢸⢬⠣⢃⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠠⠨⡐⠌⢆⢇⢧⢭⣣⡳⣵⢫⣳⢱⠱⢑⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣆⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠁⡊⢌⢢⢡⢣⢪⡺⡪⡎⡎⡎⡚⣨⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠕⡅⢗⢕⡳⡭⣳⢕⠕⡱⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠌⠄⠑⠩⢈⢂⣱⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⡀⢄⠄⣀⠄⡀⣀⢠⢄⣖⣖⣞⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣱⡐⡕⡕⡽⣝⣟⣮⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣵⣽⣸⣃⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿