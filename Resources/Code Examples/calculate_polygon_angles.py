# The sum of interior angles in a triangle is 180°.
# To find the sum of interior angles of a polygon, multiply the number of triangles in the polygon by 180°.
# The formula for calculating the sum of interior angles is
# (n - 2) x 180° where n is the number of sides.
# All the interior angles in a regular polygon are equal.
# The formula for calculating the size of an interior angle is:
# interior angle of a polygon = sum of interior angles ÷ number of sides.
# The sum of exterior angles of a polygon is 360°.
# The formula for calculating the size of an exterior angle is:
# exterior angle of a polygon = 360 ÷ number of sides.
# Python3 implementation of the approach


# Python3 program to find the interior and exterior
# angle of a given polygon

# function to find the interior and exterior angle of a polygon
def findAngle(n):

    # formula to find the
    # interior angle
    interiorAngle = int((n - 2) * 180 / n)

    # formula to find
    # the exterior angle
    exteriorAngle = int(360 / n)

    # Displaying the output
    print("Interior angle: ",
          interiorAngle)

    print("Exterior angle: ",
          exteriorAngle)


def main():
    while True:
        print("Find the interior and exterior angles of any polygon")
        number_of_sides = int(input("Enter the number of sides (0 to quit): "))
        if number_of_sides < 3:
            break
        findAngle(number_of_sides)


# If a standalone program, call the main function
# Else, use as a module
if __name__ == '__main__':
    main()
