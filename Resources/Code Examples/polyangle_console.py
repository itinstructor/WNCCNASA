"""
    Name: polyangle_console.py
    Author: William A Loring
    Created: 11/24/21
    Purpose: Python console program to calculate the
    interior and exterior angles of a polygon
"""


#----------------- CALCULATE ANGLES OF REGULAR POLYGON -------------------------#
def calculate_angles(number_of_sides):
    """
        Function to calculate the interior and exterior angle
        of any regular polygon
    """
    # Calculate interior angle
    interior_angle = int((number_of_sides - 2) * 180 / number_of_sides)

    # Calculate exterior angle
    exterior_angle = int(360 / number_of_sides)

    # Display the output
    print(f"Interior angle: {interior_angle}°")
    print(f"Exterior angle: {exterior_angle}°")


#----------------------------- MAIN METHOD ------------------------------------#
def main():
    while True:
        print("**********************************************************")
        print("Find the interior and exterior angles of a regular polygon")

        # Try except exception handling
        try:
            number_of_sides = int(input("Enter number of sides (0 to quit): "))
            # A regular polygon has a minimum of 3 sides
            if number_of_sides == 0:
                break
            elif number_of_sides < 3:
                break
            calculate_angles(number_of_sides)
        # If there is improper input, let the user know, try again
        except:
            print("Please input a whole number")
            main()


#---------------------- CALL THE MAIN FUNCTION --------------------------------#
# If a standalone program, call the main function
# Else, use as a module
if __name__ == '__main__':
    main()
