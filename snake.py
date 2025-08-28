import turtle
import time
import random

delay = 0.1
score = 0
highestscore = 0

# Snake bodies
bodies = []

# Main Screen
main_Screen = turtle.Screen()
main_Screen.title('Snake Game')
main_Screen.bgcolor('green')
main_Screen.setup(width=600, height=600)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape('circle')
head.color('white')
head.fillcolor('blue')
head.penup()
head.goto(0, 0)
head.direction = 'stop'

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('yellow')
food.fillcolor('red')
food.penup()
food.goto(0, 200)

# Score Board
sb = turtle.Turtle()
sb.color('black')
sb.penup()
sb.ht()
sb.goto(-280, 250)
sb.write('Score : 0 | Highest Score : 0', font=('arial', 15, 'bold'))

# Function Declaration
def moveup():
    if head.direction != 'down':
        head.direction = 'up'

def movedown():
    if head.direction != 'up':
        head.direction = 'down'

def moveleft():
    if head.direction != 'right':
        head.direction = 'left'

def moveright():
    if head.direction != 'left':
        head.direction = 'right'

def movestop():
    head.direction = 'stop'

def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)

# Event Handling
main_Screen.listen()
main_Screen.onkey(moveup, 'Up')
main_Screen.onkey(movedown, 'Down')
main_Screen.onkey(moveleft, 'Left')
main_Screen.onkey(moveright, 'Right')
main_Screen.onkey(movestop, 'space')

# Main Loop
while True:
    main_Screen.update()

    # Border wrapping
    if head.xcor() > 280:
        head.setx(-280)

    if head.xcor() < -280:
        head.setx(280)

    if head.ycor() > 280:
        head.sety(-280)

    if head.ycor() < -280:
        head.sety(280)

    # Check collision with food
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # Increase the length of Snake
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape('circle')
        body.color('red')
        body.fillcolor('darkred')
        bodies.append(body)

        # Increase the score
        score += 10

        # change delay
        delay -= 0.001

        # Update the highest score
        if score > highestscore:
            highestscore = score

        sb.clear()
        sb.write('Score : {} | Highest Score : {}'.format(score, highestscore), font=('arial', 15, 'bold'))

    # Move the Snake Body
    for i in range(len(bodies) - 1, 0, -1):
        x = bodies[i - 1].xcor()
        y = bodies[i - 1].ycor()
        bodies[i].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

    move()

    # check collision with snake body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'

            # Hide body
            for body in bodies:
                body.ht()
            bodies.clear()

            score = 0
            delay = 0.1

            # update score board
            sb.clear()
            sb.write('Score : {} | Highest Score : {}'.format(score, highestscore), font=('arial', 15, 'bold'))

    time.sleep(delay)

main_Screen.mainloop()
