import turtle
import time
import math


def main():
    #Game window
    WIDTH = 300
    HEIGHT=300
    wn=turtle.Screen()
    wn.bgcolor('black')
    wn.title('Space Invaders')

    fields=border(WIDTH, HEIGHT)
    player=character()
    bullet=gun()
    invador=enemy(0, HEIGHT-30)
    wn.onkey(player.move_left, 'Left')
    wn.onkey(player.move_right, 'Right')
    wn.onkey(lambda: bullet.fire(player.xcor(), player.ycor()), 'space')
    wn.listen()



    while True:
        invador.move()
        if bullet.ycor()>=HEIGHT-30:
            bullet.bulletstate='ready'
            bullet.hideturtle()
        if bullet.bulletstate=='in_progress':
            x=bullet.xcor()
            y=bullet.ycor()+bullet.bulletspeed
            bullet.setpos(x,y)

        #else:
        #    print(bullet.bulletstate)
        #    time.sleep(1)
        #time.sleep(1)
        #time.sleep(1)
        #    #if y >= HEIGHT - 30:
            #    bullet.bulletstate = 'ready'


    #wn.exitonclick()

def collision(x1, y1, x2, y2):
    distance=sqrt(sqr(x2-x1)+sqr(y2-y1))
    if distance < 2:
        return True

class border(turtle.Turtle):
    def __init__(self, width, height, shape='triangle', color='white', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.speed(0)
        self.color(color)
        self.penup()
        self.setpos(-width, -height)
        self.pensize(3)
        self.pendown()
        self.hideturtle()
        for side in range(4):
            self.fd(600)
            self.lt(90)

class enemy(turtle.Turtle):
    def __init__(self, x, y, shape='circle', color='red', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.penup()
        self.setpos(0, 270)
        self.shape(shape)
        self.color(color)
        self.setheading(270)
        self.speed(1)
        self.enemyspeed=20

    def move(self):
        x=self.xcor()
        y=self.ycor()
        x+=self.enemyspeed
        self.setx(x)
        if x >=300-30:
            self.enemyspeed*=-1
            self.sety(y-30)
        if x<=-300+30:
            self.enemyspeed*=-1
            self.sety(y-30)

class character(turtle.Turtle):
    def __init__(self, shape='triangle', color='blue', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.penup()
        self.setpos(0, -270)
        self.shape(shape)
        self.color(color)
        self.setheading(90)
        self.speed(0)

    def move_left(self):
        speed=15
        x=self.xcor()
        if x<=-270:
            x=-270
        else:
            x=x-speed
        self.setx(x)

    def move_right(self):
        speed=15
        x=self.xcor()
        if x>=270:
            x=270
        else:
            x=x+speed
        self.setx(x)

class gun(turtle.Turtle):
    def __init__(self, shape='triangle', color='yellow', *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bulletspeed=40
        self.bulletstate='ready'
        self.penup()
        #self.setpos(x, y+10)
        self.shape(shape)
        self.color(color)
        self.setheading(90)
        self.shapesize(0.5,0.5)
        self.speed(0)
        self.hideturtle()

    def fire(self, x, y):
        if self.bulletstate=='ready':
            self.setpos(x, y+10)
            self.showturtle()
            self.bulletstate='in_progress'



if __name__=='__main__':
    main()

