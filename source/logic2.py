
def make_bricks(small, big, goal):
    """We want to make a row of bricks that is goal inches long. We have a number of 
    small bricks (1 inch each) and big bricks (5 inches each). Return true if it 
    is possible to make the goal by choosing from the given bricks. This is a little 
    harder than it looks and can be done without any loops. 
    """
    # Use integer dividsion to find how many big bricks we can use.
    # If we don't have enough big bricks, we need to replace them with small bricks.
    smalls_to_replace_missing_bigs = 5 * max(goal // 5 - big, 0)
    remaining_smalls_needed = goal % 5
    total_smalls_needed = smalls_to_replace_missing_bigs + remaining_smalls_needed
    return small >= total_smalls_needed

def lone_sum(a, b, c):
    """Given 3 int values, a b c, return their sum. However, if one of the values is 
    the same as another of the values, it does not count towards the sum.
    """
    num_freq = {num: (a, b, c).count(num) for num in (a, b, c)}
    return sum([key for key, val in num_freq.items() if val == 1])

def lucky_sum(a, b, c):
    """Given 3 int values, a b c, return their sum. However, if one of the values is 13 
    then it does not count towards the sum and values to its right do not count. So 
    for example, if b is 13, then both b and c do not count.
    """
    nums = (a, b, c)
    index_13 = [index for index, val in enumerate(nums) if val == 13]
    new_lst = nums if len(index_13) == 0 else nums[:index_13[0]]
    return sum(new_lst)

def no_teen_sum(a, b, c):
    """Given 3 int values, a b c, return their sum. However, if any of the values is a teen 
    -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do 
    not count as a teens. Write a separate function, fix_teen, that takes 
    in an int value and returns that value fixed for the teen rule. In this way, you avoid 
    repeating the teen code 3 times (i.e. "decomposition"). Define the nested helper function 
    within the body of no_teen_sum. 
    """
    def fix_teen(num):
        return 0 if 13 <= num <= 19 and num not in {15, 16} else num

    fixed_nums = map(fix_teen, (a, b, c))
    return sum(fixed_nums)

def round_sum(a, b, c):
    """For this problem, we'll round an int value up to the next multiple of 10 if its rightmost
    digit is 5 or more, so 15 rounds up to 20. Alternately, round down to the previous multiple 
    of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, 
    return the sum of their rounded values. To avoid code repetition, write a nested helper 
    function, round_10, and call it 3 times. Write the helper entirely below and 
    at the same indent level as round_sum().
    """
    def round_up(n): 
        return n + (10 - (n % 10))
    def round_down(n):
        return n - (n % 10)
    def round_10(n):
        return round_down(n) if (n % 10) < 5 else round_up(n)

    return sum(map(round_10, (a, b, c)))

def close_far(a, b, c):
    """Given three ints, a b c, return true if one of b or c is "close" (differing from a by at 
    most 1), while the other is "far", differing from both other values by 2 or more.
    """
    def close(num, target):
        return abs(num - target) <= 1

    def far(num, target1, target2):
        return abs(num - target1) >= 2 and abs(num - target2) >= 2

    return (close(b, a) and far(c, a, b)) or (close(c, a) and far(b, a, c))

def blackjack(a, b):
    """Given 2 int values greater than 0, return whichever value is nearest to 21 without going over. 
    Return 0 if they both go over. 
    """
    def diff_by_21(n): 
        return abs(21 - n) 

    if a > 21 and b > 21:
        return 0
    else:
        nums_that_are_lower = (n for n in (a, b) if n <= 21)
        return min(nums_that_are_lower, key=diff_by_21)

def evenly_spaces(a, b, c):
    """Given three ints, a b c, one of them is small, one is medium and one is large. Return true if the
    three values are evenly spaced, so the difference between small and medium is the same as the 
    difference between medium and large.
    """
    small, medium, large = sorted((a, b, c))
    return medium - small == large - medium

def make_chocolate(small, big, goal):
    """We want to make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars 
    (5 kilos each). Return the number of small bars to use, assuming we always use big bars before 
    small bars. Return -1 if it can't be done.
    """
    smalls_to_replace_missing_bigs = 5 * max(goal // 5 - big, 0)
    remaining_smalls_needed = goal % 5
    total_smalls_needed = smalls_to_replace_missing_bigs + remaining_smalls_needed
    return total_smalls_needed if small >= total_smalls_needed else -1
