
'''
Problem
=======

Create a computer program that completes the following tasks:

It prompts the user for a series of 5 integers.
The user must be prompted for 5 numbers.
After the fifth entry, the program stops prompting for values and performs the following calculations:
 - the product of the integers
 - the average of the integers
 - the sum of the integers
 
After performing the calculations, the program should display the following to the user:
the values the user entered
each of the calculations, using a phrase that identifies the value

'''
def get_user_num_input():
    """Prompts the user to enter a number and ensures it is an integer."""
    while True:
        try:
            value = input("Enter a number: ")
            return int(value)
        except ValueError:
            print("Please enter a valid integer.", end="\n")


def prompt_user_for_number(num_of_time_to_prompt=5):
    """
    Prompts the user to enter a specified number of integers.
    
    :param num_of_time_to_prompt: The number of times to prompt the user.
    :return: A list containing the user's numbers.
    """
    user_nums = []
  
    for _ in range(num_of_time_to_prompt):
        num = get_user_num_input()
        user_nums.append(num)
        
    return user_nums


def calculate_user_numbers_summary(user_num_list):
    """
    Takes a list of user numbers and calculates a summary (sum, product, average).
    
    :param user_num_list: A list of integers from the user.
    :return: A dictionary containing the summary calculations (sum, product, average).
    """
    if not isinstance(user_num_list, list):
        raise TypeError("The parameter provided is not a list")
    
    user_num_summary = {}
    user_num_summary["average"] = calculate_average(user_num_list)
    user_num_summary["product"] = calculate_product_of_numbers(user_num_list)
    user_num_summary["sum"] = calculate_sum_of_numbers(user_num_list)
    user_num_summary["users_numbers"] = ", ".join(map(str, user_num_list))
    
    return user_num_summary


def display_summary_to_user(summary):
    """Displays the calculated summary to the user."""
    print(f"\n\nUser chosen numbers: {summary.get('users_numbers', 'N/A')}", end="\n\n")
    print(f"The sum of the numbers chosen by the user: {summary.get('sum', 'N/A')}")
    print(f"The product of the numbers chosen by the user: {summary.get('product', 'N/A')}")
    print(f"The average of the numbers chosen by the user: {summary.get('average', 'N/A')}", end="\n")


def calculate_sum_of_numbers(num_list):
    """
    Returns the sum of a list of numbers.
    
    :param num_list: A list of numbers.
    :return: The sum of the numbers within the list.
    :raises TypeError: If the parameter is not a list.
    """
    if not isinstance(num_list, list):
        raise TypeError("The parameter provided is not a list")
    return sum(num_list)


def calculate_product_of_numbers(num_list):
    """
    Returns the product of a list of numbers.
    
    :param num_list: A list of numbers.
    :return: The product of the numbers within the list.
    :raises TypeError: If the parameter is not a list.
    """
    if not isinstance(num_list, list):
        raise TypeError("The parameter provided is not a list")
    product = 1
    for num in num_list:
        product *= num
    return product


def calculate_average(num_list):
    """
    Returns the average of a list of numbers.
    
    :param num_list: A list of numbers.
    :return: The average of the numbers within the list.
    :raises TypeError: If the parameter is not a list.
    """
    if not isinstance(num_list, list):
        raise TypeError("The parameter provided is not a list")
    if len(num_list) == 0:
        return 0
    return sum(num_list) / len(num_list)


def main():
    user_nums = prompt_user_for_number()
    calculation_summary = calculate_user_numbers_summary(user_nums)
    display_summary_to_user(calculation_summary)


if __name__ == "__main__":
    main()
