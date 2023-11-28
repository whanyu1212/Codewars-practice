def high_and_low(numbers: str) -> str:
    """Take in a string of numbers,
    split them by space and return
    the highest and lowest number.

    Args:
        numbers (str): A string of numbers separated by space

    Returns:
        str: Max and min separated by space
    """
    numbers_list = [int(i) for i in numbers.split()]
    return f"{max(numbers_list)} {min(numbers_list)}"
