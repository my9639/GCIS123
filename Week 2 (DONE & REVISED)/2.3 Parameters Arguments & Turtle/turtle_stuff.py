import turtle

angle = 45


def test_drive():

    turtle.forward(100)
    turtle.left(87)
    turtle.setheading(0)
    turtle.goto(50,50)
    turtle.home()
    turtle.circle(25)
    turtle.up()


def square(sidesize,angle,pencolor,fillcolor):
    '''
    This function programs turtle to draw a square while starting and ending in the same position and orientation.
    '''
    turtle.pensize(4)
    turtle.pencolor(pencolor)
    turtle.fillcolor(fillcolor)
    turtle.begin_fill()

    turtle.setheading(0)
    turtle.right(angle)
    turtle.forward(sidesize) #Turtle starts facing to the right with the pen down so this command will move the turtle drawing sidesize pixels to the right. 
    turtle.right(90) #Faces the turtle down.
    turtle.forward(sidesize)
    turtle.right(90) #Faces the turtle left.
    turtle.forward(sidesize) 
    turtle.right(90) #Faces the turtle up.
    turtle.forward(sidesize) #All 4 sides must be equal for a square so we draw forward everytime by the exact same number of pixels each side.
    turtle.right(angle)

    turtle.end_fill()

def turtle_state(): 

    print("Is turtle pen down?", turtle.isdown())
    print("Turtle Heading", int(turtle.heading()))
    print("Turtle Coordinates: ", int(turtle.xcor()),int(turtle.ycor()))


def main():

    turtle.bgcolor("yellow")

    turtle_state()
    #test_drive()
    square(50,90,"red","White")
    square(100,135,"Black","Green")
    square(150,180,"Blue","Black")
    turtle_state()

    input("Press Enter to Close Program")


main()