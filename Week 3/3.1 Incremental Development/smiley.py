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
    


def main():
    draw_circle(0,0,20,"red")
    draw_circle(50,50,40,"green")
    draw_circle(100,100,60,"yellow")

    input("Press Enter to Close Program")

main()