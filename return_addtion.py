# twig williams
# 10/11/23
# function to add two numbers that is called by a main func

def add_two(num1, num2):
    """
    This function takes two numbers as input and returns their sum.

    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.

    Returns:
    float: The sum of num1 and num2.
    """
    result = num1 + num2
    return result


def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    sum_result = add_two(num1, num2)

    print(f"The sum of {num1} and {num2} is {sum_result}")


if __name__ == "__main__":
    main()
