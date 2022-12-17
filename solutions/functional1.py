# Given a list of integers, return a list where each integer is multiplied by 2.
def doubling(nums):
    return list(map(lambda num: 2 * num, nums))

# Given a list of integers, return a list where each integer is multiplied with itself.
def square(nums):
    return list(map(lambda num: num * num, nums))

# Given a list of strings, return a list where each string has "*" added at its end.
def add_star(strings):
    return list(map(lambda string: string + '*', strings))

# Given a list of strings, return a list where each string is replaced by 3 copies of the 
# string concatenated together.
def copies3(strings):
    return list(map(lambda string: 3 * string, strings))

# Given a list of strings, return a list where each string has "y" added at its start and end.
def more_y(strings):
    return list(map(lambda string: 'y' + string + 'y', strings))

# Given a list of integers, return a list where each integer is added to 1 and the result is 
# multiplied by 10.
def math1(nums):
    return list(map(lambda num: (1 + num) * 10, nums))

# Given a list of non-negative integers, return an integer list of the rightmost digits. 
# (Note: use %)
def right_digit(nums):
    return list(map(lambda num: num % 10, nums))

# Given a list of strings, return a list where each string is converted to lower case 
# (Note: str lower() method).
def lower(strings):
    return list(map(lambda string: string.lower(), strings))

# Given a list of strings, return a list where each string has all its "x" removed.
def no_x(strings): 
    return list(map(lambda string: ''.join(str(char) for char in filter(lambda char: char != 'x', string)), strings))
