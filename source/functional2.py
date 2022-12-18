# Given a list of integers, return a list of the integers, omitting any that are less than 0.
def no_neg(nums):
    return list(filter(lambda num: num >= 0, nums))

# Given a list of non-negative integers, return a list of those numbers except omitting any 
# that end with 9. (Note: % by 10)
def no_9(nums):
    return list(filter(lambda num: num % 10 != 9, nums))

# Given a list of integers, return a list of those numbers, omitting any that are between 13 
# and 19 inclusive.
def no_teen(nums):
    return list(filter(lambda num: not (13 <= num <= 19), nums))

# Given a list of strings, return a list of the strings, omitting any string that contains 
# a "z". (Note: the x in str returns a boolean)
def no_z(strings):
    return list(filter(lambda string: 'z' not in string, strings))

# Given a list of strings, return a list of the strings, omitting any string length 4 or more.
def no_long(strings):
    return list(filter(lambda string: len(string) < 4, strings))

# Given a list of strings, return a list of the strings, omitting any string length 3 or 4.
def no_34(strings):
    return list(filter(lambda string: len(string) not in {3, 4}, strings))

# Given a list of strings, return a list where each string has "y" added at its end, omitting 
# any resulting strings that contain "yy" as a substring anywhere.
def no_yy(strings):
    return list(filter(lambda string: 'yy' not in string, map(lambda string: string + 'y', strings)))

# Given a list of non-negative integers, return a list of those numbers multiplied by 2, 
# omitting any of the resulting numbers that end in 2.
def two_2(nums):
    return list(filter(lambda num: num % 10 != 2, map(lambda num: 2 * num, nums)))

# Given a list of integers, return a list of those numbers squared and the product added to 10, 
# omitting any of the resulting numbers that end in 5 or 6.
def square_56(nums):
    return list(filter(lambda num: num % 10 not in {5, 6}, map(lambda num: (num ** 2) + 10, nums)))
