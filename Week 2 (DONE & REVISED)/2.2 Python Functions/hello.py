'''
The first function in this program prints "Hello, World!" to the user.
The second function prompts the user to input their name, with the program returning a greeting back to them.
'''

def Hello_World():
    print("Hello, World!")


def Hello_You():
    """
    Takes the name as input of the user.
    Then uses name to print a greeting to the user.
    """
    name = input("Please enter your name: ") #The input of the user will be converted into the "name" variable for later use.
    print("Halla Wallah, Bu" + name + "!")


Hello_World() 
Hello_You()