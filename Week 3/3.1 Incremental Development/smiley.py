import turtle

'''
def draw_circle(x,y, radius, fill_color):

    #This function draws a filled-in circle with 4 different parameters when called.   
    #We will test this function by defining a main function that uses it to draw 3 circles with different locations, radii, and fill colors. 

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
    '''
    This function will tweak the speed and animation of the turtle as we like.
    '''
    turtle.speed(speed)
    turtle.tracer(traceranimation)


def draw_centered_circle(x,y, radius, fill_color):
    '''
    This function always draws a circle with the turtle in the middle of the circle.
    '''
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
    '''
    This function draws the Head and Nose of the smiley face.    
    '''
    draw_centered_circle(x,y, headradius, fill_color_head)
    
    draw_centered_circle (x,y, headradius/10, fill_color_nose)

def draw_eyes(x,y, eyeradius, color):
    '''
    This function draws the Eyes of the smiley face.
    '''
    draw_centered_circle(x,y, eyeradius, "White") #Draws the Eyeball
    draw_centered_circle(x,y, eyeradius/2, "Light Blue") #Draws the iris
    draw_centered_circle(x,y, eyeradius/4, "Black") #Draws the pupil

def main():
    
    tweak(0,False)
    #draw_smiley(0,0,200,"yellow","pink")
    tweak(10,True)
    draw_eyes(10,10,100,"brown")
    
    #turtle.hideturtle()
    input("Press Enter to Close Program")

main()