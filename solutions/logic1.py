# When squirrels get together for a party, they like to have cigars. A squirrel party 
# is successful when the number of cigars is between 40 and 60, inclusive. Unless it is 
# the weekend, in which case there is no upper bound on the number of cigars. Return true 
# if the party with the given values is successful, or false otherwise.
def cigar_party(cigars, is_weekend):
    return cigars >= 40 and (is_weekend or cigars <= 60)

# You and your date are trying to get a table at a restaurant. The parameter "you" 
# is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness 
# of your date's clothes. The result getting the table is encoded as an int value with 0=no, 
# 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). 
# With the exception that if either of you has style of 2 or less, then the result is 0 (no). 
# Otherwise the result is 1 (maybe). 
def date_fashion(you, date):
    result = 1
    if you <= 2 or date <= 2:
        result = 0
    elif you >= 8 or date >= 8:
        result = 2
    return result

# The squirrels in Palo Alto spend most of the day playing. In particular, they play if the 
# temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 
# 100 instead of 90. Given an int temperature and a boolean isSummer, return true if the squirrels 
# play and false otherwise.
def squirrel_play(temp, is_summer):
    return 60 <= temp <= (100 if is_summer else 90)

# You are driving a little too fast, and a police officer stops you. Write code to compute 
# the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed 
# is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. 
# If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your 
# speed can be 5 higher in all cases.
def caught_speeding(speed, is_birthday):
    result = 0
    find_speed_limit = lambda base_speed, is_birthday : base_speed + 5 if is_birthday else base_speed
    if speed > (85 if is_birthday else 80):
        result = 2
    if  (66 if is_birthday else 61) <= speed <= (85 if is_birthday else 80):
        result = 1 
    return result

# Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, 
# are forbidden, so in that case just return 20.
def sorta_sum(a, b):
    return 20 if a+b in range(10, 20) else a+b

# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating 
# if we are on vacation, return a string of the form "7:00" indicating when the alarm clock 
# should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". 
# Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".
def alarm_clock(day, vacation):
    result = ''
    if 1 <= day <= 5:
       result = '10:00' if vacation else '7:00' 
    else:
        result = 'off' if vacation else '10:00' 
    return result

# The number 6 is a truly great number. Given two int values, a and b, return true if 
# either one is 6. Or if their sum or difference is 6. Note: the function abs(num) computes 
# the absolute value of a number.
def love_6(a, b):
    return 6 in {a, b, a+b, abs(a-b)} 

# Given a number n, return true if n is in the range 1..10, inclusive. Unless outsideMode 
# is true, in which case return true if the number is less or equal to 1, or greater or 
# equal to 10.
def in_1_to_10(n, outside_mode):
    return not (1 < n < 10) if outside_mode else 1 <= n <= 10 

# We'll say a number is special if it is a multiple of 11 or if it is one more than a 
# multiple of 11. Return true if the given non-negative number is special. Use the % "mod" 
# operator
def special_eleven(n):
    return n % 11 in {0, 1}

# Return true if the given non-negative number is 1 or 2 more than a multiple of 20.
def more_20(n):
    return n % 20 in {1, 2} 

# Return true if the given non-negative number is a multiple of 3 or 5, but not both.
def old_35(n):
    return (n % 5 == 0) != (n % 3 == 0)

# Return true if the given non-negative number is 1 or 2 less than a multiple of 20. So 
# for example 38 and 39 return true, but 40 returns false.
def less_20(n):
    return 0 in {(n + 1) % 20, (n + 2) % 20}

# Given a non-negative number "num", return true if num is within 2 of a multiple of 10. 
# Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2.
def near_ten(num):
    return num % 10 in {0, 1, 2, 8, 9} 

# Given 2 ints, a and b, return their sum. However, "teen" values in the range 13..19 
# inclusive, are extra lucky. So if either value is a teen, just return 19.
def teen_sum(a, b):
    is_teen = lambda x : 13 <= x <= 19
    return a + b if not any(map(is_teen, [a, b])) else 19

# Your cell phone rings. Return true if you should answer it. Normally you answer, except 
# in the morning you only answer if it is your mom calling. In all cases, if you are asleep, 
# you do not answer.
def answer_cell(is_morning, is_mom, is_asleep):
    return (not is_morning or is_mom) and not is_asleep

# We are having a party with amounts of tea and candy. Return the int outcome of the party encoded 
# as 0=bad, 1=good, or 2=great. A party is good (1) if both tea and candy are at least 5. 
# However, if either tea or candy is at least double the amount of the other one, the party is great 
# (2). However, in all cases, if either tea or candy is less than 5, the party is always bad (0).
def tea_party(tea, candy):
    result = 1 
    if tea < 5 or candy < 5:
        result = 0
    elif tea >= (2 * candy) or candy >= (2 * tea):
        result = 2
    return result

# Given a string str, if the string starts with "f" return "Fizz". If the string ends with "b" 
# return "Buzz". If both the "f" and "b" conditions are true, return "FizzBuzz". In all other 
# cases, return the string unchanged.
def fizz_string(str):
    result = str
    if str.startswith('f') and str.endswith('b'):
        result =  'FizzBuzz'
    elif str.startswith('f'):
        result =  'Fizz'
    elif str.endswith('b'):
        result =  'Buzz'
    return result

# Given an int n, return the string form of the number followed by "!". So the int 6 yields "6!". 
# Except if the number is divisible by 3 use "Fizz" instead of the number, and if the number is 
# divisible by 5 use "Buzz", and if divisible by both 3 and 5, use "FizzBuzz". 
def fizz_string_2(n):
    result = f'{n}!'
    if n % 3 == 0 and n % 5 == 0:
        result = 'FizzBuzz!'
    elif n % 3 == 0:
        result = 'Fizz!'
    elif n % 5 == 0:
        result = 'Buzz!'
    return result

# Given three ints, a b c, return true if it is possible to add two of the ints to get the third.
def two_as_one(a, b, c):
    return any([a + b == c, a + c == b, b + c == a])

# Given three ints, a b c, return true if b is greater than a, and c is greater than b. However, 
# with the exception that if "bOk" is true, b does not need to be greater than a.
def in_order(a, b, c, b_ok):
    return  b < c if b_ok else a < b < c

# Given three ints, a b c, return true if they are in strict increasing order, such as 2 5 11, or 
# 5 6 7, but not 6 5 7 or 5 5 7. However, with the exception that if "equalOk" is true, equality 
# is allowed, such as 5 5 7 or 5 5 5.
def in_order_equal(a, b, c, equal_ok):
    return  a <= b <= c if equal_ok else a < b < c 

# Given three ints, a b c, return true if two or more of them have the same rightmost digit. The ints 
# are non-negative. Note: the % "mod" operator computes the remainder, e.g. 17 % 10 is 7.
def last_digit(a, b, c):
    right_digits = map(lambda x : x % 10, [a, b, c])
    return len(set(right_digits)) < 3

# Given three ints, a b c, return true if one of them is 10 or more less than one of the others.
def less_by_10(a, b, c):
    is_less_by_10 = lambda x, y : (y - 10 >= x) or (x - 10 >= y)
    return any([is_less_by_10(a, b), is_less_by_10(a, c), is_less_by_10(b, c)])

# Return the sum of two 6-sided dice rolls, each in the range 1..6. However, if noDoubles is true, 
# if the two dice show the same value, increment one die to the next value, wrapping around to 1 
# if its value was 6.
def without_doubles(die_1, die_2, no_doubles):
    wrap_up = lambda x : x + 1 if x != 6 else 1
    return (die_1 + wrap_up(die_2)) if no_doubles and (die_1 == die_2) else (die_1 + die_2)

# Given two int values, return whichever value is larger. However if the two values have the same 
# remainder when divided by 5, then the return the smaller value. However, in all cases, if the 
# two values are the same, return 0. Note: the % "mod" operator computes the remainder, 
# e.g. 7 % 5 is 2.
def max_mod_5(a, b):
    result =  0
    if a == b:
        result = 0
    elif a % 5  == b % 5:
        result =  min(a, b)
    else:
        result = max(a, b)
    return result

# You have a red lottery ticket showing ints a, b, and c, each of which is 0, 1, or 2. If they are 
# all the value 2, the result is 10. Otherwise if they are all the same, the result is 5. Otherwise 
# so long as both b and c are different from a, the result is 1. Otherwise the result is 0.
def red_ticket(a, b, c):
    return None

# You have a green lottery ticket, with ints a, b, and c on it. If the numbers are all different 
# from each other, the result is 0. If all of the numbers are the same, the result is 20. If two 
# of the numbers are the same, the result is 10.
def green_ticket(a, b, c):
    return None

# You have a blue lottery ticket, with ints a, b, and c on it. This makes three pairs, which we'll 
# call ab, bc, and ac. Consider the sum of the numbers in each pair. If any pair sums to exactly 10,
# the result is 10. Otherwise if the ab sum is exactly 10 more than either bc or ac sums, the result 
# is 5. Otherwise the result is 0.
def blue_ticket(a, b, c):
    return None

# Given two ints, each in the range 10..99, return true if there is a digit that appears in both 
# numbers, such as the 2 in 12 and 23. (Note: division, e.g. n/10, gives the left digit while the 
# % "mod" n%10 gives the right digit.)
def share_digit(a, b):
    return None

# Given 2 non-negative ints, a and b, return their sum, so long as the sum has the same number of 
# digits as a. If the sum has more digits than a, just return a without b. (Note: one way to 
# compute the number of digits of a non-negative int n is to convert it to a string with 
# String.valueOf(n) and then check the length of the string.) 
def sum_limit(a, b):
    return None