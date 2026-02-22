import turtle

'''
def draw_circle(x,y, radius, fill_color):
'''
    #This function draws a filled-in circle with 4 different parameters when called.   
    #We will test this function by defining a main function that uses it to draw 3 circles with different locations, radii, and fill colors. 
'''
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.up()    
'''


def tweak(speed,traceranimation):
    turtle.speed(speed)
    turtle.tracer(traceranimation)


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


def draw_smiley(x,y, headradius, fill_color_head, fill_color_nose):
    
    draw_centered_circle(x,y, headradius, fill_color_head)
    
    draw_centered_circle (x,y, headradius/10, fill_color_nose)


def main():
    
    tweak(0,False)
    draw_smiley(0,0,200,"yellow","pink")
    tweak(10,True)
    
    turtle.hideturtle()
    input("Press Enter to Close Program")

main()