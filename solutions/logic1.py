# When squirrels get together for a party, they like to have cigars. A squirrel party 
# is successful when the number of cigars is between 40 and 60, inclusive. Unless it is 
# the weekend, in which case there is no upper bound on the number of cigars. Return true 
# if the party with the given values is successful, or false otherwise.
def cigar_party(cigars, is_weekend):
    return cigars >= 40 and (is_weekend or cigars <= 60)

# You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness 
# of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. The result 
# getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 
# 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, 
# then the result is 0 (no). Otherwise the result is 1 (maybe). 
def date_fashion(you, date):
    result = 1
    if you <= 2 or date <= 2:
        result = 0
    elif you >= 8 or date >= 8:
        result = 2
    return result

# The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 
# 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and 
# a boolean isSummer, return true if the squirrels play and false otherwise.
def squirrel_play(temp, is_summer):
    return temp >= 60 and temp <= (100 if is_summer else 90)

# You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int 
# value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, 
# the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
def caught_speeding(speed, is_birthday):
    result = 0
    if speed >= (86 if is_birthday else 81):
        result = 2
    if speed in range(66 if is_birthday else 61, (86 if is_birthday else 81)):
        result = 1 
    return result

# Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.
def sorta_sum(a, b):
    return 20 if a+b in range(10, 20) else a+b