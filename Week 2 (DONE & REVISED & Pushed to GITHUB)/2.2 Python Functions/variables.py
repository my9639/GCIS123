def variable_practice():
    
    your_age = print("I am 20 years old")
    
    number_of_days_in_a_year = print("There are 365 days in a year")
    
    pet = print("What is the name of your first pet?: The name of my first pet is funny")

    pi = print(float("3.14"))


def expressions_practice():
    Literal = print(int("5")) 
    
    Addition = print(5 + 5)

    Exponent = print(5**2) #Answer is 25

    Floor_Division = print(9 // 2) #Answer is rounded down to 4

    Mod = print(9 % 2) #Answer is 1

    PEMDAS = print( (1+4-3) *2 ) #Answer is 4

    four_operators = print(int(2**2 * 2 / 2 + 12 - 6)) #Answer is 10 but / always returns a float so prints as 10.0 if not type converted


def prompt_and_print():
    
    print("Please enter 2 numbers")
    
    First_Number = int(input("First Number: "))
    Second_Number = int(input("Second Number: "))

    print(First_Number + Second_Number)
    print(First_Number - Second_Number)
    print(First_Number * Second_Number)
    print(int(First_Number / Second_Number))

def main(): 
    variable_practice()
    expressions_practice()
    prompt_and_print()


main()
