def doubling(nums):
    """Given a list of integers, return a list where each integer is multiplied by 2."""
    return list(map(lambda num: 2 * num, nums))

def square(nums):
    """Given a list of integers, return a list where each integer is multiplied with itself."""
    return list(map(lambda num: num * num, nums))

def add_star(strings):
    """Given a list of strings, return a list where each string has "*" added at its end."""
    return list(map(lambda string: string + '*', strings))

def copies3(strings):
    """Given a list of strings, return a list where each string is replaced by 3 copies of the 
    string concatenated together.
    """
    return list(map(lambda string: 3 * string, strings))

def more_y(strings):
    """Given a list of strings, return a list where each string has "y" added at its start and end."""
    return list(map(lambda string: 'y' + string + 'y', strings))

def math1(nums):
    """Given a list of integers, return a list where each integer is added to 1 and the result is 
    multiplied by 10.
    """
    return list(map(lambda num: (1 + num) * 10, nums))

def right_digit(nums):
    """Given a list of non-negative integers, return an integer list of the rightmost digits."""
    return list(map(lambda num: num % 10, nums))

def lower(strings):
    """Given a list of strings, return a list where each string is converted to lower case"""
    return list(map(lambda string: string.lower(), strings))

def no_x(strings): 
    """Given a list of strings, return a list where each string has all its "x" removed."""
    return list(map(lambda string: ''.join(str(char) for char in filter(lambda char: char != 'x', string)), strings))
