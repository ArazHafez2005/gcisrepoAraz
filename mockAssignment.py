#This function prompts the user to enter a number
def get_number():
    num = int(input("Please enter a number: "))
    return num 
""" Returns the number user enters """

#This function checks if it is even or odd
def even_or_odd(user_number):
    """ Use this if else to determine whether it is even or odd """
    if user_number % 2 == 0:
        print("The number you have entered is EVEN.")
    else:
        print("The number you have entered is ODD.")

#This function checks if it is positive or negative
def positive_or_negative(user_number):
    """ Use this if to determine if it is positive, negative or zero """
    if user_number > 0:
        print("The number you have entered is POSITIVE.")
    elif user_number < 0:
        print("The number you have entered is NEGATIVE.")
    else:
        print("The number is ZERO.")

#This function finds its square
def get_square(user_number):
    """ Squares the number and returns its value """
    squared = (user_number**2)
    return squared

#This function finds its cube
def get_cube(user_number):
    """ Squares the number and returns its value """
    cubed = (user_number**3)
    return cubed

#This is the main function of the program. In here we will call all the preceeding user-defined functions we have made:
def main():
    """ Created a variable by the name user_number that stores the value returned by our get_number function """
    user_number = get_number()
    print("The number you have entered is:", user_number) 
    
    even_or_odd(user_number)
    
    positive_or_negative(user_number)
    
    squared_number = get_square(user_number)
    print("The square of the number: ", squared_number)
    
    cubed_number = get_cube(user_number)
    print("The cube of the number: ", cubed_number)


main() 