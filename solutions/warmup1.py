# The parameter weekday is true if it is a weekday, and the parameter vacation is true if 
# we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return true 
# if we sleep in.
def sleep_in(weekday, vacation):
    return not weekday or vacation

# We have two monkeys, a and b, and the parameters aSmile and bSmile indicate if each is 
# smiling. We are in trouble if they are both smiling or if neither of them is smiling. 
# Return true if we are in trouble.
def monkey_trouble(aSmile, bSmile):
    return aSmile and bSmile or (not aSmile and not bSmile)

# Given two int values, return their sum. Unless the two values are the same, then return 
# double their sum.
def sum_double(a, b):
    result = a + b if a !=b else 2 * (a + b)
    return result

# Given an int n, return the absolute difference between n and 21, except return double the 
# absolute difference if n is over 21.
def diff_21(n):
    diff = abs(21 - n)
    result = diff if n <= 21 else 2 * diff
    return result

# We have a loud talking parrot. The "hour" parameter is the current hour time in the range 
# 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return 
# true if we are in trouble.
def parrot_trouble(talking, hour):
    return talking and (hour < 7 or hour > 20)

# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
def makes_10(a, b):
    return a == 10 or b == 10 or a + b == 10

# Given an int n, return True if it is within 10 of 100 or 200. Note: Math.abs(num) computes the 
# absolute value of a number.
def near_hundred(n):
    return abs(n - 100) <= 10 or abs(n - 200) <= 10

# Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" 
# is true, then return true only if both are negative.
def pos_neg(a, b, negative):
    result = (a < 0 and b < 0) if negative else (a * b) < 0
    return result

# Given a string, return a new string where "not " has been added to the front. However, if the string already 
# begins with "not", return the string unchanged. Note: use .equals() to compare 2 strings.
def not_string(str):
    result = "not " + str
    if len(str) >= 3 and str[0:3] == "not" :
        result = str
    return result

# Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value 
# of n will be a valid index of a char in the original string (i.e. n will be in the range 0..str.length()-1 inclusive).
def missing_char(str, n):
    return str[0:n] + str[n+1:]

# Given a string, return a new string where the first and last chars have been exchanged.
def front_back(str):
    result = (str[-1] + str[1:-1] + str[0]) if len(str) > 1 else str
    return result

# Given a string, we'll say that the front is the first 3 chars of the string. If the string 
# length is less than 3, the front is whatever is there. Return a new string which is 3 copies of 
# the front.
def front_3(str):
    front = str[0:3] if len(str) >= 3 else str
    return 3 * front

# Given a string, take the last char and return a new string with the last char added at the front and back, so "cat" 
# yields "tcatt". The original string will be length 1 or more.
def back_around(str):
    back = str[-1]
    return back + str + back

# Return true if the given non-negative number is a multiple of 3 or a multiple of 5. Use the % "mod" operator
def or_35(n):
    return n % 3 == 0 or n % 5 == 0

# Given a string, take the first 2 chars and return the string with the 2 chars added at both the front and back, 
# so "kitten" yields"kikittenki". If the string length is less than 2, use whatever chars are there.
def front_22(str):
    front = str if len(str) < 2 else str[:2]
    return front + str + front

# Given a string, return true if the string starts with "hi" and false otherwise.
def start_hi(str):
    return str.startswith('hi')

# Given two temperatures, return true if one is less than 0 and the other is greater than 100.
def icy_hot(temp1, temp2):
    one_icy_another_hot = lambda x, y : x < 0 and y > 100
    return one_icy_another_hot(temp1, temp2) or one_icy_another_hot(temp2, temp1)

# Given 2 int values, return true if either of them is in the range 10..20 inclusive.
def in_1020(a, b):
    in_range = lambda x : x >= 10 and x <= 20
    return in_range(a) or in_range(b)

# We'll say that a number is "teen" if it is in the range 13..19 inclusive. Given 3 int values, return 
# true if 1 or more of them are teen.
def has_teen(a, b, c):
    is_teen = lambda x : x >= 13 and x <= 19
    return is_teen(a) or is_teen(b) or is_teen(c)

# We'll say that a number is "teen" if it is in the range 13..19 inclusive. Given 2 int values, return true 
# if one or the other is teen, but not both.
def lone_teen(a, b):
    is_teen = lambda x : x >= 13 and x <= 19
    teens = [x for x in [a, b] if is_teen(x)]
    return len(teens) == 1

# Given a string, if the string "del" appears starting at index 1, return a string where that "del" has been deleted. 
# Otherwise, return the string unchanged.
def del_del(str):
    return str[0] + str[4:] if len(str) >= 4 and str[1:4] == 'del' else str

# Return true if the given string begins with "mix", except the 'm' can be anything, so "pix", "9ix" .. all count.
def mix_start(str):
    return len(str) >= 3 and str[1:3] == 'ix'

# Given a string, return a string made of the first 2 chars (if present), however include first char only if it is 'o' 
# and include the second only if it is 'z', so "ozymandias" yields "oz".
def start_oz(str):
    first_char_is_o = len(str) >= 1 and str[0] == 'o'
    second_char_is_z = len(str) >= 2 and str[1] == 'z'
    return ''.join(['o' if first_char_is_o else '', 'z' if second_char_is_z else ''])

# Given three int values, a b c, return the largest.
def int_max(a, b, c):
    return max(a, b, c)

# Given 2 int values, return whichever value is nearest to the value 10, or return 0 in the event of a tie. Note that 
# abs(n) returns the absolute value of a number.
def close_10(a, b):
    a_dist_10 = abs(10 - a)
    b_dist_10 = abs(10 - b)
    return 0 if a_dist_10 == b_dist_10 else (a if a_dist_10 < b_dist_10 else b)

# Given 2 int values, return true if they are both in the range 30..40 inclusive, or they are both in the range 40..50 
# inclusive.
def in_3040(a, b):
    in_30_40 = lambda x : x >= 30 and x <= 40
    in_40_50 = lambda x : x >= 40 and x <= 50
    return (in_30_40(a) and in_30_40(b)) or (in_40_50(a) and in_40_50(b))

# Given 2 positive int values, return the larger value that is in the range 10..20 inclusive, or return 0 if neither is in that range.
def max_1020(a, b):
    nums_in_range = [x for x in [a, b] if x >= 10 and x <= 20]
    return 0 if len(nums_in_range) == 0 else max(nums_in_range)

# Return True if the given string contains between 1 and 3 'e' chars.
# 
# (NOTE): Look into regex solution
def string_e(str):
    num_es = str.count('e')
    return num_es >= 1 and num_es <= 3

# Given two non-negative int values, return true if they have the same last digit, such as with 27 and 57. Note that the % "mod" operator 
# computes remainders, so 17 % 10 is 7.
def last_digit(a, b):
    a_last_digit = a % 10
    b_last_digit = b % 10
    return a_last_digit == b_last_digit

# Given a string, return a new string where the last 3 chars are now in upper case. If the string has less than 3 chars, uppercase whatever 
# is there. Note that str.upper() returns the uppercase version of a string.
def end_up(str):
    front = str[:-3]
    end = str[-3:]
    return front + end.upper()

# Given a non-empty string and an int N, return the string made starting with char 0, and then every Nth char of the string. So if N is 3, use 
# char 0, 3, 6, ... and so on. N is 1 or more.
def every_nth(str, n):
    return str[::n]