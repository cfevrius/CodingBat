def factorial(n):
    """Given n of 1 or more, return the factorial of n, which is n * (n-1) * (n-2) ... 1. 
    Compute the result recursively (without loops).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def bunny_ears(bunnies):
    """We have a number of bunnies and each bunny has two big floppy ears. We want to compute 
    the total number of ears across all the bunnies recursively (without loops or multiplication).
    """
    if bunnies == 0:
        return 0
    else:
        return 2 + bunny_ears(bunnies - 1)

def fibonacci(n):
    """The fibonacci sequence is a famous bit of mathematics, and it happens to have a recursive 
    definition. The first two values in the sequence are 0 and 1 (essentially 2 base cases). 
    Each subsequent value is the sum of the previous two values, so the whole sequence is: 
    0, 1, 1, 2, 3, 5, 8, 13, 21 and so on. Define a recursive fibonacci(n) method that returns 
    the nth fibonacci number, with n=0 representing the start of the sequence.
    """
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def bunny_ears2(bunnies):
    """We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies (1, 3, ..) have the 
    normal 2 ears. The even bunnies (2, 4, ..) we'll say have 3 ears, because they each have a 
    raised foot. Recursively return the number of "ears" in the bunny line 1, 2, ... n (without 
    loops or multiplication).
    """
    if bunnies == 0:
        return 0
    elif bunnies % 2 == 0:
        return 3 + bunny_ears2(bunnies - 1)
    else:
        return 2 + bunny_ears2(bunnies - 1)

def triangle(rows):
    """We have triangle made of blocks. The topmost row has 1 block, the next row down has 2 blocks, 
    the next row has 3 blocks, and so on. Compute recursively (no loops or multiplication) the 
    total number of blocks in such a triangle with the given number of rows.
    """
    if rows == 0:
        return 0
    else:
        return rows + triangle(rows - 1)

def sum_digits(n):     
    """Given a non-negative int n, return the sum of its digits recursively (no loops). Note that 
    mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (//) by 10 removes the 
    rightmost digit (126 / 10 is 12).
    """
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_digits(n // 10)

def count7(n):
    """
    Given a non-negative int n, return the count of the occurrences of 7 as a digit, so for 
    example 717 yields 2. (no loops). Note that mod (%) by 10 yields the rightmost digit 
    (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).
    """
    if n == 0:
        return 0
    elif (n % 10) == 7:
        return 1 + count7(n // 10)
    else:
        return count7(n // 10)

def count8(n):
    """Given a non-negative int n, compute recursively (no loops) the count of the occurrences of 
    8 as a digit, except that an 8 with another 8 immediately to its left counts double, so 8818 
    yields 4. Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide 
    (/) by 10 removes the rightmost digit (126 / 10 is 12).  
    """
    if n == 0:
        return 0
    elif (n % 100) == 88:
        return 2 + count8(n // 10)
    elif (n % 10) == 8:
        return 1 + count8(n // 10)
    else:
        return count8(n // 10)

def power_n(base, n):
    """Given base and n that are both 1 or more, compute recursively (no loops) the value of base 
    to the n power, so powerN(3, 2) is 9 (3 squared).
    """
    if n == 0:
        return 1
    else:
        return base * power_n(base, n - 1)

def count_x(str):
    """Given a string, compute recursively (no loops) the number of lowercase 'x' chars in the string."""
    if str == "":
        return 0
    elif str[0] == 'x':
        return 1 + count_x(str[1:])
    else:
        return count_x(str[1:])

def count_hi(str):
    """Given a string, compute recursively the number of times lowercase "hi" appears in the string."""
    if len(str) < 2:
        return 0
    elif str[:2] == 'hi':
        return 1 + count_hi(str[2:])
    else:
        return count_hi(str[1:])

def change_xy(str):
    """Given a string, compute recursively a new string where all the lowercase 
    'x' chars have been changed to 'y' chars.
    """
    if str == "":
        return ""
    elif str[0] == 'x':
        return 'y' + change_xy(str[1:])
    else:
        return str[0] + change_xy(str[1:])

def change_pi(str):
    """Given a string, compute recursively a new string where all appearances of 
    "pi" have been replaced by "3.14".
    """
    if str == "":
        return ""
    elif len(str) >= 2 and str[0:2] == 'pi':
        return '3.14' + change_pi(str[2:])
    else:
        return str[0] + change_pi(str[1:]) 

def no_x(str):
    """Given a string, compute recursively a new string where all the 'x' chars have been removed."""
    if str == "":
        return ""
    elif str[0] == 'x':
        return no_x(str[1:])
    else:
        return str[0] + no_x(str[1:])

def array6(nums, index):
    """Given an array of ints, compute recursively if the array contains a 6. We'll use the convention 
    of considering only the part of the array that begins at the given index. In this way, a recursive 
    call can pass index+1 to move down the array. The initial call will pass in index as 0.
    """
    if index >= len(nums):
        return False
    elif nums[index] == 6:
        return True
    else:
        return array6(nums, index + 1)    

def array11(nums, index):
    """Given an array of ints, compute recursively the number of times that the value 11 appears in the 
    array. We'll use the convention of considering only the part of the array that begins at the given 
    index. In this way, a recursive call can pass index+1 to move down the array. The initial call will 
    pass in index as 0.
    """
    if index >= len(nums):
        return 0
    elif nums[index] == 11:
        return 1 + array11(nums, index + 1)
    else:
        return array11(nums, index + 1)

def array_220(nums, index):
    """Given an array of ints, compute recursively if the array contains somewhere a value followed in the 
    array by that value times 10. We'll use the convention of considering only the part of the array that 
    begins at the given index. In this way, a recursive call can pass index+1 to move down the array. The 
    initial call will pass in index as 0.
    """
    if index >= len(nums):
        return False
    elif index + 1 < len(nums) and nums[index + 1] == 10 * nums[index]:
        return True
    else:
        return array_220(nums, index + 1) 

def all_star(str):
    """Given a string, compute recursively a new string where all the adjacent chars are now separated by a "*"."""
    if len(str) <= 1:
        return str
    else:
        return str[0] + '*' + all_star(str[1:])

def pair_star(str):
    """Given a string, compute recursively a new string where identical chars that are adjacent in the 
    original string are separated from each other by a "*".
    """
    if str == "":
        return ""
    elif len(str) >= 2 and str[0] == str[1]:
        return str[0] + '*' + pair_star(str[1:])
    else:
        return str[0] + pair_star(str[1:])

def end_x(str):
    """Given a string, compute recursively a new string where all the lowercase 'x' chars have been 
    moved to the end of the string.
    """
    if str == "":
        return ""
    elif str[0] == 'x':
        return end_x(str[1:]) + 'x' 
    else:
        return str[0] + end_x(str[1:])


def count_pairs(str):
    """We'll say that a "pair" in a string is two instances of a char separated by a char. So "AxA" 
    the A's make a pair. Pair's can overlap, so "AxAxA" contains 3 pairs -- 2 for A and 1 for x. 
    Recursively compute the number of pairs in the given string.
    """
    if len(str) < 3:
        return 0
    elif str[0] == str[2]:
        return 1 + count_pairs(str[1:])
    else:
        return count_pairs(str[1:])

def count_abc(str):
    """Count recursively the total number of "abc" and "aba" substrings that appear in the given string."""
    if len(str) < 3:
        return 0
    elif str[0:3] == 'abc' or str[0:3] == 'aba':
        return 1 + count_abc(str[1:]) 
    else:
        return count_abc(str[1:])

def count11(str):
    """Given a string, compute recursively the number of "11" substrings in the string. 
    The "11" substrings should not overlap.
    """
    if len(str) < 2:
        return 0
    elif str[0:2] == '11':
        return 1 + count11(str[2:]) 
    else:
        return count11(str[1:])

def string_clean(str):
    """Given a string, return recursively a "cleaned" string where adjacent chars that are the same 
    have been reduced to a single char. So "yyzzza" yields "yza".
    """
    if str == "":
        return ""
    elif len(str) >= 2 and str[0] == str[1]:
        return string_clean(str[1:])
    else:
        return str[0] + string_clean(str[1:])

def count_hi2(str):
    """Given a string, compute recursively the number of times lowercase "hi" appears in the string, 
    however do not count "hi" that have an 'x' immedately before them.
    """
    if str == "":
        return 0
    elif len(str) >= 3 and str[0:3] == 'xhi':
        return count_hi2(str[3:])
    elif len(str) >= 2 and str[0:2] == 'hi':
        return 1 + count_hi2(str[2:])
    else:
        return count_hi2(str[1:])

def paren_bit(str):
    """Given a string that contains a single pair of parenthesis, compute recursively a new string 
    made of only of the parenthesis and their contents, so "xyz(abc)123" yields "(abc)".
    """
    if str[0] == '(' and str[-1] == ')':
        return str
    if str[0] != '(':
        return paren_bit(str[1:])
    if str[-1] != ')':
        return paren_bit(str[:-1])

def nest_paren(str):
    """Given a string, return true if it is a nesting of zero or more pairs of parenthesis, like 
    "(())" or "((()))". Suggestion: check the first and last chars, and then recur on what's inside 
    them.
    """
    if str == "":
        return True
    elif str[0] == '(' and str[-1] == ')':
        return nest_paren(str[1:-1])
    else:
        return False

def str_count(str, sub):
    """Given a string and a non-empty substring sub, compute recursively the number of times that sub
    appears in the string, without the sub strings overlapping.
    """
    if len(str) < len(sub):
        return 0
    if len(str) >= len(sub) and str[:len(sub)] == sub:
        return 1 + str_count(str[len(sub):], sub)
    else:
        return str_count(str[1:], sub)

def str_copies(str, sub, n):
    """Given a string and a non-empty substring sub, compute recursively if at least n copies of sub 
    appear in the string somewhere, possibly with overlapping. N will be non-negative.
    """
    if str == "" and n != 0:
        return False
    elif str == "" and n == 0:
        return True
    elif len(str) >= len(sub) and str[:len(sub)] == sub:
        return str_copies(str[1:], sub, n - 1)
    else:
        return str_copies(str[1:], sub, n)

def str_dist(str, sub):
    """Given a string and a non-empty substring sub, compute recursively the largest substring which 
    starts and ends with sub and return its length.
    """
    if len(str) < len(sub):
        return 0
    if str.startswith(sub) and str.endswith(sub):
        return len(str)
    elif not str.startswith(sub):
        return str_dist(str[1:], sub)
    elif not str.endswith(sub):
        return str_dist(str[:-1], sub)
