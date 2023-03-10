import turtle
import winsound

win = turtle.Screen()
win.title("Pong me baby")
win.bgcolor('#3CB371')
win.setup(width=870, height=500)
win.tracer(0)

FTW = 0
fts = 0
# scoreboard
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 200)
score.write("Player A: 0    Player B: 0", align="center", font=("Calibri", 20, "bold"))

# paddle 1
thing1 = turtle.Turtle()
thing1.speed(0)
thing1.shape("square")
thing1.shapesize(stretch_wid=4, stretch_len=0.5)
thing1.color('#800000')
thing1.penup()
thing1.goto(-410, 0)

# paddle 2
thing2 = turtle.Turtle()
thing2.speed(0)
thing2.shape("square")
thing2.shapesize(stretch_wid=4, stretch_len=0.5)
thing2.color('#800000')
thing2.penup()
thing2.goto(410, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("turtle")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.13
ball.dy = 0.13

# function
def thing1_up():
    y = thing1.ycor()
    y += 40
    thing1.sety(y)
def thing1_down():
    y = thing1.ycor()
    y -= 40
    thing1.sety(y)
def thing2_up():
    y = thing2.ycor()
    y += 40
    thing2.sety(y)
def thing2_down():
    y = thing2.ycor()
    y -= 40
    thing2.sety(y)
#def exit_this_silly_game():
    #exit()

# keyboard input
win.listen()
win.onkeypress(thing1_up, "w")
win.onkeypress(thing1_down, "s")
win.onkeypress(thing2_up, "Up")
win.onkeypress(thing2_down, "Down")
#win.onkeypress(exit_this_silly_game,"Escape")
while True:
    win.update()

    # set ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # boundaries
    # ball boundaries first
    if ball.ycor() > 230:
        ball.sety(-230)
        ball.right(25)
        ball.dy *= 1.00
        # winsound.PlaySound('womp.wav', winsound.SND_ASYNC)
    if ball.ycor() < -230:
        ball.sety(230)
        ball.right(25)
        ball.dy *= 1.00
        # winsound.PlaySound('womp.wav', winsound.SND_ASYNC)
    # with the score now
    if ball.xcor() > 420:
        ball.goto(0, 0)
        ball.dx *= -1.00
        FTW += 1
        score.clear()
        score.write("Player A: {}   Player B: {}".format(FTW, fts), align="center", font=("Arial", 20, "bold"))
        winsound.PlaySound('wow.wav', winsound.SND_ASYNC)

    if ball.xcor() < -420:
        ball.goto(0, 0)
        ball.dx *= -1.00
        fts += 1
        score.clear()
        score.write("Player A: {}   Player B: {}".format(FTW, fts), align="center", font=("Arial", 20, "bold"))
        winsound.PlaySound('wow.wav', winsound.SND_ASYNC)


    # paddle boundaries
    if thing1.ycor() > 250:
        thing1.goto (-410,-250)
    if thing1.ycor() < -250:
        thing1.goto (-410,250)
    if thing2.ycor() > 250:
        thing2.goto (410,-250)
    if thing2.ycor() < -250:
        thing2.goto (410, 250)

    # ball collisions with paddle
    if (400 < ball.xcor() < 410) and (thing2.ycor() + 40 > ball.ycor() > thing2.ycor() - 40):
        ball.setx(400)
        ball.dx *= -1.00
        ball.right(180)
        winsound.PlaySound('womp.wav', winsound.SND_ASYNC)
    if (-400 > ball.xcor() > -410) and (thing1.ycor() + 40 > ball.ycor() > thing1.ycor() - 40):
        ball.setx(-400)
        ball.dx *= -1.00
        ball.right(180)
        winsound.PlaySound('womp.wav', winsound.SND_ASYNC)


# range the speed based on paddle bounce
# range the angle or direction in diagonal form for all bounces
# Triangle to rotate on bounces