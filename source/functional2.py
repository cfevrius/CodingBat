def no_neg(nums):
    """Given a list of integers, return a list of the integers, omitting any that are less than 0."""
    return list(filter(lambda num: num >= 0, nums))

def no_9(nums):
    """Given a list of non-negative integers, return a list of those numbers except omitting any 
    that end with 9. 
    """
    return list(filter(lambda num: num % 10 != 9, nums))

def no_teen(nums):
    """Given a list of integers, return a list of those numbers, omitting any that are between 13 
    and 19 inclusive.
    """
    return list(filter(lambda num: not (13 <= num <= 19), nums))

def no_z(strings):
    """Given a list of strings, return a list of the strings, omitting any string that contains 
    a "z". 
    """
    return list(filter(lambda string: 'z' not in string, strings))

def no_long(strings):
    """Given a list of strings, return a list of the strings, omitting any string length 4 or more."""
    return list(filter(lambda string: len(string) < 4, strings))

def no_34(strings):
    """Given a list of strings, return a list of the strings, omitting any string length 3 or 4."""
    return list(filter(lambda string: len(string) not in {3, 4}, strings))

def no_yy(strings):
    """Given a list of strings, return a list where each string has "y" added at its end, omitting 
    any resulting strings that contain "yy" as a substring anywhere.
    """
    return list(filter(lambda string: 'yy' not in string, map(lambda string: string + 'y', strings)))

def two_2(nums):
    """Given a list of non-negative integers, return a list of those numbers multiplied by 2, 
    omitting any of the resulting numbers that end in 2.
    """
    return list(filter(lambda num: num % 10 != 2, map(lambda num: 2 * num, nums)))

def square_56(nums):
    """Given a list of integers, return a list of those numbers squared and the product added to 10, 
    omitting any of the resulting numbers that end in 5 or 6.
    """
    return list(filter(lambda num: num % 10 not in {5, 6}, map(lambda num: (num ** 2) + 10, nums)))
