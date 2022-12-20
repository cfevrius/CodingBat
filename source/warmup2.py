# Given a string and a non-negative int n, return 
# a larger string that is n copies of the original string.
def string_times(string, n):
    return string * n

# Given a string and a non-negative int n, we'll say that 
# the front of the string is the first 3 chars, or whatever is there 
# if the string is less than length 3. Return n copies of the front;
def front_times(string, n):
    front = string[:3]
    return front * n

# Count the number of "xx" in the given string. We'll say that 
# overlapping is allowed, so "xxx" contains 2 "xx".
def count_xx(string):
    matches = [i for i, _ in enumerate(string[:-1]) if string[i:i+2] == 'xx']
    return len(matches)

# Given a string, return true if the first instance of "x" in 
# the string is immediately followed by another "x".
def double_x(string):
    first_occur = string.find('x')
    second_occur = string.find('x', first_occur + 1)
    return second_occur == (first_occur + 1) 

# Given a string, return a new string made of every other char 
# starting with the first, so "Hello" yields "Hlo".
def string_bits(string):
    return string[::2]

# Given a non-empty string like "Code" return a string like "CCoCodCode".
def string_splosion(string):
    lst_of_substrs = [string[:i] for i in range(1, len(string)+1)]
    return ''.join(lst_of_substrs)

# Given a string, return the count of the number of times that a substring 
# length 2 appears in the string and also as the last 2 chars of the string, 
# so "hixxxhi" yields 1 (we won't count the end substring).
def last2(string):
    search_str = string[-2:]
    occurrences = [i for i, _ in enumerate(string[:-2]) if string[i:i+2] == search_str]
    return len(occurrences)

# Given an array of ints, return the number of 9's in the array.
def array_count9(nums):
    return len([i for i in nums if i == 9])

# Given an array of ints, return true if one of the first 4 elements in the array 
# is a 9. The array length may be less than 4.
def array_front9(nums):
    front = nums[:4]
    return 9 in front

# Given an array of ints, return true if the sequence of numbers 1, 2, 3 appears 
# in the array somewhere.
def array123(nums):
    occurrences = [i for i, _ in enumerate(nums[:-2]) if nums[i:i+3] == [1, 2, 3]]
    return len(occurrences) > 0

# Given 2 strings, a and b, return the number of the positions where they contain the 
# same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", 
# and "az" substrings appear in the same place in both strings.
def string_match(a, b):
    lower = min(len(a), len(b))
    occurrences = [i for i in range(lower - 1) if a[i:i+2] == b[i:i+2]]
    return len(occurrences)

# Given a string, return a version where all the "x" have been removed. 
# Except an "x" at the very start or end should not be removed.
def string_x(string):
    middle = ''.join([char for char in string[1:-1] if char != 'x'])
    return f"{string[0]}{middle}{string[-1]}" if len(string) > 1 else string

# Given a string, return a string made of the cars at indices 0,1, 4,5
# 8,9 ... so "kittens" yields "kien".
def alt_pairs(string):
    return ''.join([char for index, char in enumerate(string) if (index % 4) in {0, 1}])

# Given a string, return a version where all the 'yak' are removed, but the 'a'
# can by any char. The 'yak' string will not overlap.
def string_yak(string):
    indices = [(i, i+1, i+2) 
               for i, _ in enumerate(string[:-2]) 
               if string[i] == 'y' and string[i+2] == 'k' ]
    flatten_indices = [element for item in indices for element in item]
    return ''.join([x for i, x in enumerate(string) if i not in flatten_indices])

# Given an array of ints, return the number of times that two 6's are next to each other
# in the array. Also count instances where the second '6' is actually a 7.
def array_667(nums):
    matches = [i for i, x in enumerate(nums[:-1]) if nums[i] == 6 and nums[i+1] in {6, 7}] 
    return len(matches)

# Given an array of ints, we'll say that a triple is a value appearing 3 times in a
# row in the array. Return true if the array does not contain any triples.
def no_triples(nums):
    matches = [v for i, v in enumerate(nums[:-2]) if nums[i] == nums[i+1] == nums[i+2]]
    return len(matches) == 0

# Given an array of ints, return true if it contains a 2, 7, 1 pattern: a value, followed 
# by the value plus 5, followed by the value minus 1. Additionally the 271 counts even if 
# the "1" differs by 2 or less from the correct value.
def has_271(nums):
    matches = [x 
               for i, x in enumerate(nums[:-2]) 
               if (nums[i+1] == nums[i] + 5) and (abs((nums[i] - 1) - nums[i+2]) <= 2) ]
    return len(matches) > 0