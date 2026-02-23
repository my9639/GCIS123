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
    This function will be used to draw all the circles we need for the Face Nose Eyes
    '''
    turtle.setheading(0)
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
    turtle.setheading(0)



def draw_eyes(x,y, eyeradius, iriscolor):
    '''
    This function draws the Eyes of the smiley face.
    '''
    draw_centered_circle(x,y, eyeradius, "White") #Draws the Eyeball
    draw_centered_circle(x,y, eyeradius/2, iriscolor) #Draws the iris
    draw_centered_circle(x,y, eyeradius/4, "Black") #Draws the pupil



def draw_mouth(x,y, radius, fill_color): 
    '''
    This function draws the mouth of the smiley face.
    '''
    turtle.setheading(180)
    turtle.up()
    turtle.goto(x,y)
    turtle.forward(radius)
    turtle.setheading(270)
    turtle.down()
    turtle.fillcolor(fill_color)
    turtle.begin_fill()
    turtle.circle(radius,180)
    turtle.end_fill()
    turtle.up()
    turtle.goto(x,y)
    turtle.setheading(180)
    


def draw_smiley(x,y, headradius, fill_color_head, fill_color_nose, iriscolor):
    '''
    This function draws our smiley face    
    '''
    draw_centered_circle(x,y, headradius, fill_color_head) #Draws Head
    
    draw_centered_circle (x,y, headradius/10, fill_color_nose) #Draws Nose
    
    draw_eyes(x + 0.35*headradius, y + 0.35*headradius, 0.25*headradius, iriscolor) #Right Eye
    draw_eyes(x - 0.35*headradius, y + 0.35*headradius, 0.25*headradius, iriscolor) #Left Eye

    draw_mouth(x, y - 0.25*headradius, 0.60*headradius, "Black")



def main():
    
    tweak(0,False)
    draw_smiley(100,100,70,"yellow","pink","red")
    draw_smiley(-50,-50,60,"yellow","pink","blue")
    draw_smiley(-200,-200,100,"yellow","pink","green")
    draw_smiley(200,200,60,"yellow","pink","purple")
    tweak(10,True)
    
    turtle.hideturtle()

    input("Press Enter to Close Program")



main()