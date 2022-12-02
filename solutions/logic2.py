
# We want to make a row of bricks that is goal inches long. We have a number of 
# small bricks (1 inch each) and big bricks (5 inches each). Return true if it 
# is possible to make the goal by choosing from the given bricks. This is a little 
# harder than it looks and can be done without any loops. 
def make_bricks(small, big, goal):
    # Use integer dividsion to find how many big bricks we can use.
    # If we don't have enough big bricks, we need to replace them with small bricks.
    smalls_to_replace_missing_bigs = 5 * max(goal // 5 - big, 0)
    remaining_smalls_needed = goal % 5
    total_smalls_needed = smalls_to_replace_missing_bigs + remaining_smalls_needed
    return small >= total_smalls_needed

# Given 3 int values, a b c, return their sum. However, if one of the values is 
# the same as another of the values, it does not count towards the sum.
def lone_sum(a, b, c):
    nums = (a, b, c)
    occurrences = (nums.count(a), nums.count(b), nums.count(c))
    num_freq = dict(zip(nums, occurrences))
    return sum([key for key, val in num_freq.items() if val == 1])

# Given 3 int values, a b c, return their sum. However, if one of the values is 13 
# then it does not count towards the sum and values to its right do not count. So 
# for example, if b is 13, then both b and c do not count.
def lucky_sum(a, b, c):
    nums = (a, b, c)
    index_13 = [index for index, val in enumerate(nums) if val == 13]
    new_lst = nums if not index_13 else nums[:index_13[0]]
    return sum(new_lst)

# Given 3 int values, a b c, return their sum. However, if any of the values is a teen 
# -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do 
# not count as a teens. Write a separate lambda function, fix_teen, that takes 
# in an int value and returns that value fixed for the teen rule. In this way, you avoid 
# repeating the teen code 3 times (i.e. "decomposition"). Define the lambda function 
# within the body of no_teen_sum. 
def no_teen_sum(a, b, c):
    fix_teen = lambda num : 0 if 13 <= num <= 19 and num not in {15, 16} else num
    fixed_nums = map(fix_teen, (a, b, c))
    return sum(fixed_nums)

# For this problem, we'll round an int value up to the next multiple of 10 if its rightmost
# digit is 5 or more, so 15 rounds up to 20. Alternately, round down to the previous multiple 
# of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, 
# return the sum of their rounded values. To avoid code repetition, write a separate lambda 
# function, round_10, and call it 3 times. Write the helper entirely below and 
# at the same indent level as round_sum().
def round_sum(a, b, c):
    round_up = lambda n : n + (10 - (n % 10))
    round_down = lambda n : n - (n % 10)
    round_10 = lambda n : round_down(n) if (n % 10) < 5 else round_up(n)
    return sum(map(round_10, (a, b, c)))

# Given three ints, a b c, return true if one of b or c is "close" (differing from a by at 
# most 1), while the other is "far", differing from both other values by 2 or more. Note: 
# abs(num) computes the absolute value of a number.
def close_far(a, b, c):
    close = lambda num, target: abs(num - target) <= 1
    far = lambda num, target1, target2: abs(num - target1) >= 2 and abs(num - target2) >= 2
    return (close(b, a) and far(c, a, b)) or (close(c, a) and far(b, a, c))

# Given 2 int values greater than 0, return whichever value is nearest to 21 without going over. 
# Return 0 if they both go over. 
def blackjack(a, b):
    diff_by_21 = lambda n : abs(21 - n)
    if a > 21 and b > 21:
        return 0
    else:
        nums_that_are_lower = (n for n in (a, b) if n <= 21)
        return min(nums_that_are_lower, key=diff_by_21)

# Given three ints, a b c, one of them is small, one is medium and one is large. Return true if the
# three values are evenly spaced, so the difference between small and medium is the same as the 
# difference between medium and large.
def evenly_spaces(a, b, c):
    small, medium, large = sorted((a, b, c))
    return medium - small == large - medium

# We want to make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars 
# (5 kilos each). Return the number of small bars to use, assuming we always use big bars before 
# small bars. Return -1 if it can't be done.
def make_chocolate(small, big, goal):
    smalls_to_replace_missing_bigs = 5 * max(goal // 5 - big, 0)
    remaining_smalls_needed = goal % 5
    total_smalls_needed = smalls_to_replace_missing_bigs + remaining_smalls_needed
    return total_smalls_needed if small >= total_smalls_needed else -1