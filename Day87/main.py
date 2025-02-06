import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Breakout Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)  # Stop automatic screen updates

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=6)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, -200)
ball.dx = 1
ball.dy = 1

# Brick setup
bricks = []

def create_brick(x, y):
    brick = turtle.Turtle()
    brick.speed(0)
    brick.shape("square")
    brick.color("red")
    brick.penup()
    brick.goto(x, y)
    bricks.append(brick)

# Create the bricks
for i in range(-350, 350, 70):
    for j in range(100, 250, 40):
        create_brick(i, j)

# Paddle movement
def move_left():
    x = paddle.xcor()
    if x > -350:
        paddle.setx(x - 20)

def move_right():
    x = paddle.xcor()
    if x < 350:
        paddle.setx(x + 20)

# Keyboard bindings
screen.listen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Main game loop
while True:
    screen.update()  # Update the screen manually

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball-wall collision (left and right)
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.dx *= -1

    # Ball-wall collision (top and bottom)
    if ball.ycor() > 290:
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.dy *= -1
        ball.goto(0, -200)  # Reset ball position

    # Ball-paddle collision
    if ball.ycor() > paddle.ycor() + 10 and ball.ycor() < paddle.ycor() + 20:
        if paddle.xcor() - 50 < ball.xcor() < paddle.xcor() + 50:
            ball.dy *= -1

    # Ball-brick collision
    for brick in bricks:
        if ball.distance(brick) < 30:
            ball.dy *= -1
            brick.hideturtle()
            bricks.remove(brick)
            break

    # Check if all bricks are destroyed
    if not bricks:
        print("You win!")
        break

    # Add a small delay for the game loop
    screen.update()
