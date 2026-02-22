import turtle

def draw_circle(x,y, radius, fill_color):
    '''
    This function draws a filled-in circle with 4 different parameters when called.   
    We will test this function by defining a main function that uses it to draw 3 circles with different locations, radii, and fill colors. 
    '''
    turtle.up()
    turtle.goto(x,y)
    turtle.down
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.up()
    

def draw_centered_circle(x,y, radius, fill_color):

    original_heading = turtle.heading()

    print(int(turtle.heading()))

    turtle.up()
    turtle.goto(x,y)
    turtle.setheading(0)
    turtle.forward(radius)
    turtle.down()
    turtle.setheading(90)
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.up()
    turtle.goto(x,y)
    turtle.setheading(original_heading)


def main():
    draw_centered_circle(10,10, 50, "red")

    input("Press Enter to Close Program")

main()