# Given n of 1 or more, return the factorial of n, which is n * (n-1) * (n-2) ... 1. 
# Compute the result recursively (without loops).
def factorial(n):
    return None

# We have a number of bunnies and each bunny has two big floppy ears. We want to compute 
# the total number of ears across all the bunnies recursively (without loops or multiplication).
def bunny_ears(bunnies):
    return None

# The fibonacci sequence is a famous bit of mathematics, and it happens to have a recursive 
# definition. The first two values in the sequence are 0 and 1 (essentially 2 base cases). 
# Each subsequent value is the sum of the previous two values, so the whole sequence is: 
# 0, 1, 1, 2, 3, 5, 8, 13, 21 and so on. Define a recursive fibonacci(n) method that returns 
# the nth fibonacci number, with n=0 representing the start of the sequence.
def fibonacci(n):
    return None

# We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies (1, 3, ..) have the 
# normal 2 ears. The even bunnies (2, 4, ..) we'll say have 3 ears, because they each have a 
# raised foot. Recursively return the number of "ears" in the bunny line 1, 2, ... n (without 
# loops or multiplication).
def bunny_ears2(bunnies):
    return None

# We have triangle made of blocks. The topmost row has 1 block, the next row down has 2 blocks, 
# the next row has 3 blocks, and so on. Compute recursively (no loops or multiplication) the 
# total number of blocks in such a triangle with the given number of rows.
def triangle(rows):
    return None

# Given a non-negative int n, return the sum of its digits recursively (no loops). Note that 
# mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the 
# rightmost digit (126 / 10 is 12).
def sum_digits(n):     
    return None

# Given a non-negative int n, return the count of the occurrences of 7 as a digit, so for 
# example 717 yields 2. (no loops). Note that mod (%) by 10 yields the rightmost digit 
# (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).
def count7(n):
    return None

# Given a non-negative int n, compute recursively (no loops) the count of the occurrences of 
# 8 as a digit, except that an 8 with another 8 immediately to its left counts double, so 8818 
# yields 4. Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide 
# (/) by 10 removes the rightmost digit (126 / 10 is 12).  
def count8(n):
    return None

# Given base and n that are both 1 or more, compute recursively (no loops) the value of base 
# to the n power, so powerN(3, 2) is 9 (3 squared).
def power_n(base, n):
    return None

# Given a string, compute recursively (no loops) the number of lowercase 'x' chars in the string.
def count_x(str):
    return None

# Given a string, compute recursively (no loops) the number of times lowercase "hi" appears 
# in the string.
def count_hi(str):
    return None

# Given a string, compute recursively (no loops) a new string where all the lowercase 
# 'x' chars have been changed to 'y' chars.
def change_xy(str):
    return None

# Given a string, compute recursively (no loops) a new string where all appearances of 
# "pi" have been replaced by "3.14".
def change_pi(str):
    return None

# Given a string, compute recursively a new string where all the 'x' chars have been removed.
def no_x(str):
    return None

# Given an array of ints, compute recursively if the array contains a 6. We'll use the convention 
# of considering only the part of the array that begins at the given index. In this way, a recursive 
# call can pass index+1 to move down the array. The initial call will pass in index as 0.
def array6(nums, index):
    return None

# Given an array of ints, compute recursively the number of times that the value 11 appears in the 
# array. We'll use the convention of considering only the part of the array that begins at the given 
# index. In this way, a recursive call can pass index+1 to move down the array. The initial call will 
# pass in index as 0.
def array11(nums, index):
    return None

# Given an array of ints, compute recursively if the array contains somewhere a value followed in the 
# array by that value times 10. We'll use the convention of considering only the part of the array that 
# begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The 
# initial call will pass in index as 0.
def array_220(nums, index):
    return None

# Given a string, compute recursively a new string where all the adjacent chars are now separated by a "*".
def all_star(str):
    return None

# Given a string, compute recursively a new string where identical chars that are adjacent in the 
# original string are separated from each other by a "*".
def pair_star(str):
    return None

# Given a string, compute recursively a new string where all the lowercase 'x' chars have been 
# moved to the end of the string.
def end_x(str):
    return None

# We'll say that a "pair" in a string is two instances of a char separated by a char. So "AxA" 
# the A's make a pair. Pair's can overlap, so "AxAxA" contains 3 pairs -- 2 for A and 1 for x. 
# Recursively compute the number of pairs in the given string.
def count_pairs(str):
    return None

# Count recursively the total number of "abc" and "aba" substrings that appear in the given string.
def count_abc(str):
    return None

# Given a string, compute recursively (no loops) the number of "11" substrings in the string. 
# The "11" substrings should not overlap.
def count11(str):
    return None

# Given a string, return recursively a "cleaned" string where adjacent chars that are the same 
# have been reduced to a single char. So "yyzzza" yields "yza".
def string_clean(str):
    return None

# Given a string, compute recursively the number of times lowercase "hi" appears in the string, 
# however do not count "hi" that have an 'x' immedately before them.
def count_hi2(str):
    return None

# Given a string that contains a single pair of parenthesis, compute recursively a new string 
# made of only of the parenthesis and their contents, so "xyz(abc)123" yields "(abc)".
def paren_bit(str):
    return None

# Given a string, return true if it is a nesting of zero or more pairs of parenthesis, like 
# "(())" or "((()))". Suggestion: check the first and last chars, and then recur on what's inside 
# them.
def nest_paren(str):
    return None

# Given a string and a non-empty substring sub, compute recursively the number of times that sub
# appears in the string, without the sub strings overlapping.
def str_count(str, sub):
    return None

# Given a string and a non-empty substring sub, compute recursively if at least n copies of sub 
# appear in the string somewhere, possibly with overlapping. N will be non-negative.
def str_copies(str, sub, n):
    return None

# Given a string and a non-empty substring sub, compute recursively the largest substring which 
# starts and ends with sub and return its length.
def str_dist(str, sub):
    return None
