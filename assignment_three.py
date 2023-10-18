# assignment_three
# Twig Williams
# 10/16/23
# this program calculates the total surface area of a rectangular prism

def area_of_rectangle(length, width):
    """
    calculate the area of a rectangle.

    :param length: Length of the rectangle (float or int).
    :param width: Width of the rectangle (float or int).
    :return: Area of the rectangle (float).
    """
    return length * width


def surface_area(length, width, height):
    """
    calculate the total surface area of a rectangular prism.

    :param length: Length of the prism (float or int).
    :param width: Width of the prism (float or int).
    :param height: Height of the prism (float or int).
    :return: Total surface area of the prism (float).
    """
    # calculate the area of all six sides of the prism
    area1 = 2 * area_of_rectangle(length, width)
    area2 = 2 * area_of_rectangle(width, height)
    area3 = 2 * area_of_rectangle(length, height)

    # calculate the total surface area
    total_area = area1 + area2 + area3
    return total_area


def get_length():
    """
    ask the user for the length and return it.

    :return: Length entered by the user (float).
    """
    length = float(input("Enter the length of the prism: "))
    return length


def get_width():
    """
    ask the user for the width and return it.

    :return: Width entered by the user (float).
    """
    width = float(input("Enter the width of the prism: "))
    return width


def get_height():
    """
    ask the user for the height and return it.

    :return: Height entered by the user (float).
    """
    height = float(input("Enter the height of the prism: "))
    return height


def print_instructions():
    """
    print instructions for the user.
    """
    print("This program calculates the total surface area of a rectangular prism.")
    print("You will be prompted to enter the length, width, and height of the prism.")


def main():
    # print instructions
    print_instructions()

    # get dimensions
    length = get_length()
    width = get_width()
    height = get_height()

    # calculate the surface area
    total_area = surface_area(length, width, height)

    # show the result
    print(f"The total surface area of the rectangular prism is: {total_area}")

#HEHE YOU MAY NEVER SEE THIS LINE HAHAHAHAHAHAHAHHAHAHAHAHAHAHA

if __name__ == "__main__":
    main()
