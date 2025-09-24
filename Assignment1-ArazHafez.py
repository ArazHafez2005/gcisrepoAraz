#   Name:Araz Hafez    Section: 605    ID: 433006827

#Function to validate triangle based on the 3 side lengths user enters
def triangle_validator(side_1,side_2,side_3):
    """
    The condition to validate if it is triangle or not: 
    """
    
    if side_1+side_2 > side_3 and side_1+side_3 > side_2 and side_2+side_3 > side_1:
        return True
    else:
        return False

def main():
    #Getting inputs for side lengths from user
    side_1 = float(input("Enter the length for side 1: "))
    side_2 = float(input("Enter the length for side 2: "))
    side_3 = float(input("Enter the length for side 3: "))

    """This variable stores the boolean result for the validator function which we will then use for printing result"""

    result = triangle_validator(side_1, side_2, side_3)
    
    if result == True:
        print("It is a TRIANGLE")
    else:
        print("It is NOT a TRIANGLE")

#Calling the main function that tests the program
main()