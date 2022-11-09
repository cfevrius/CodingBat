import re

def string_times(str, n):
    return str * n

def front_times(str, n):
    end_pos = min(len(str), 3)
    front = str[:end_pos]
    return front * n

def string_bits(str):
    return str[::2]

def string_splosion(str):
    lst_of_substrs = [str[:i] for i in range(1, len(str)+1)]
    return ''.join(lst_of_substrs)

def last2(str):
    search_str = str[-2:]
    occurrences = [i for i in range(len(str)) if str.startswith(search_str, i, -1)]
    return len(occurrences)

def array_count9(nums):
    return len([i for i in nums if i == 9])

def array_front9(nums):
    end = min(len(nums), 4)
    front = nums[:end]
    return 9 in front

def array123(nums):
    occurrences = [i for i in range(len(nums) - 2) if nums[i:i+3] == [1, 2, 3]]
    return len(occurrences) > 0

def string_match(a, b):
    lower = min(len(a), len(b))
    occurrences = [i for i in range(lower - 1) if a[i:i+2] == b[i:i+2]]
    return len(occurrences)

def string_x(str):
    new_str = ''.join([char for char in str if char != 'x'])
    str_with_start = 'x' + new_str if len(str) > 0 and str[0] == 'x' else new_str
    str_with_end = str_with_start + 'x' if (len(str) > 1 and str[-1] == 'x') else str_with_start
    return str_with_end

# Given a string, return a string made of the cars at indexes 0,1, 4,5
# 8,9 ... so "kittens" yields "kien".
def alt_pairs(str):
    return ''.join([char for index, char in enumerate(str) if (index % 4) in {0, 1}])

# Given a string, return a version where all the 'yak' are removed, but the 'a'
# can by any char. The 'yak' string will not overlap
#
# (NOTE) This solution requires the Python regular expression module
def string_yak(str):
    return ''.join(re.split('y.k', str))

# Given an array of ints, return the number of times that two 6's are next to each other
# in the array. Also count instances where the second '6' is actually a 7.
def array_667(nums):
    str_nums = ''.join(str(x) for x in nums)
    return len(re.findall('(?=(6[67]))', str_nums))
    