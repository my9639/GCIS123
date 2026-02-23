def addition(number1 , number2):
    return number1 + number2



def subtraction(number1, number2):
    return number1 - number2



def multiplication(number1, number2):
    return number1 * number2



def division(number1 , number2):
    return int(number1 / number2)



def main():
    
    number1 = int(input("Number 1: "))
    number2 = int(input("Number 2: "))
    
    print(addition(number1,number2))
    print(subtraction(number1,number2))
    print(multiplication(number1,number2))
    print(division(number1,number2))



main()