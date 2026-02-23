
pi = 3.14159

def circumference_given_radius(radius):
    return 2*pi*radius 



def area_given_radius(radius):
    return pi*radius**2



def addition(number1 , number2):
    return number1 + number2



def subtraction(number1, number2):
    return number1 - number2



def multiplication(number1, number2):
    return number1 * number2



def division(number1 , number2):
    return int(number1 / number2)



def main():
    
    radius = float(input("Input a radius to get the circle's circumference & area: "))

    print(circumference_given_radius(radius))
    print(area_given_radius(radius))

    number1 = int(input("Number 1: "))
    number2 = int(input("Number 2: "))
    
    print(addition(number1,number2))
    print(subtraction(number1,number2))
    print(multiplication(number1,number2))
    print(division(number1,number2))



main()