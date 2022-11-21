# Given an array of ints, return true if 6 appears as either the first 
# or last element in the array. The array will be length 1 or more.
def first_last_6(nums):
    return nums[0] == 6 or nums[-1] == 6

# Given an array of ints, return true if the array is length 1 or more, 
# and the first element and the last element are equal.
def same_first_last(nums):
    return len(nums) > 0 and nums[0] == nums[-1]

# Return an int array length 3 containing the first 3 digits of pi, [3, 1, 4].
def make_pi():
    return [3, 1, 4]

# Given 2 arrays of ints, a and b, return true if they have the same first element 
# or they have the same last element. Both arrays will be length 1 or more.
def common_end(a, b):
    return a[0] == b[0] or a[-1] == b[-1]

# Given an array of ints length 3, return the sum of all the elements.
def sum3(nums):
    return sum(nums)

# Given an array of ints length 3, return an array with the elements "rotated left" 
# so [1, 2, 3] yields [2, 3, 1].
def rotate_left_3(nums):
    return nums[1:] + nums[0:1]

# Given an array of ints length 3, return a new array with the elements in reverse order, 
# so [1, 2, 3] becomes [3, 2, 1].
def reverse_3(nums):
    return list(reversed(nums))

# Given an array of ints length 3, figure out which is larger, the first or last element in 
# the array, and set all the other elements to be that value. Return the changed array.
def max_end_3(nums):
    return [max(nums[0], nums[-1])] * len(nums)

# Given an array of ints, return the sum of the first 2 elements in the array. If the array 
# length is less than 2, just sum up the elements that exist, returning 0 if the array is 
# length 0.
def sum_2(nums):
    return sum(nums[:2])

# Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their 
# middle elements.
def middle_way(a, b):
    return [a[1], b[1]]

# Given an array of ints, return a new array length 2 containing the first and last elements 
# from the original array. The original array will be length 1 or more.
def make_ends(nums):
    return [nums[0], nums[-1]]

# Given an int array length 2, return true if it contains a 2 or a 3.
def has_2_3(nums):
    return (2 in nums) or (3 in nums)

# Given an int array length 2, return true if it does not contain a 2 or 3.
def no_2_3(nums):
    return not ((2 in nums) or (3 in nums))

# Given an int array, return a new array with double the length where its last 
# element is the same as the original array, and all the other elements are 0. 
# The original array will be length 1 or more. Note: by default, a new int array 
# contains all 0's.
def make_last(nums):
    return ((( len(nums) * 2) - 1) * [0]) + [nums[-1]]

# Given an int array, return true if the array contains 2 twice, or 3 twice. The array 
# will be length 0, 1, or 2.
def double_2_3(nums):
    return nums.count(2) == 2 or nums.count(3) == 2

# Given an int array length 3, if there is a 2 in the array immediately followed by a 3, set 
# the 3 element to 0. Return the changed array.
def fix_2_3(nums):
    matches = [i + 1 for i, _ in enumerate(nums[:-1]) if nums[i] == 2 and nums[i + 1] == 3]
    for match in matches:
        nums[match] = 0
    return nums

# Start with 2 int arrays, a and b, of any length. Return how many of the arrays have 1 as 
# their first element.
def start_1(a, b):
    matches = [x for x in [a, b] if x and x[0] == 1]
    return len(matches)

# Start with 2 int arrays, a and b, each length 2. Consider the sum of the values in each array. 
# Return the array which has the largest sum. In event of a tie, return a.
def bigger_two(a, b):
    return sorted([b, a], key=sum)[1]

# Given an array of ints of even length, return a new array length 2 containing the middle two elements 
# from the original array. The original array will be length 2 or more.
def make_middle(nums):
    start = (len(nums) // 2) - 1
    return nums[start:start+2]

# Given 2 int arrays, each length 2, return a new array length 4 containing all their elements.
def plus_two(a, b):
    return a + b

# Given an array of ints, swap the first and last elements in the array. Return the modified array. 
# The array length will be at least 1.
def swap_ends(nums):
    return nums[-1:] + nums[1:-1] + nums[0:1] if len(nums) > 1 else nums

# Given an array of ints of odd length, return a new array length 3 containing the elements from the 
# middle of the array. The array length will be at least 3.
def mid_three(nums):
    start = len(nums) // 2 - 1
    return nums[start:start+3]

# Given an array of ints of odd length, look at the first, last, and middle values in the array and return 
# the largest. The array length will be a least 1.
def max_triple(nums):
    return sorted([nums[0], nums[len(nums) // 2], nums[-1] ])[-1]

# Given an int array of any length, return a new array of its first 2 elements. If the array is smaller than length 2, 
# use whatever elements are present.
def front_piece(nums):
    return nums[:2]

# We'll say that a 1 immediately followed by a 3 in an array is an "unlucky" 1. Return true if the given array contains an 
# unlucky 1 in the first 2 or last 2 positions in the array.
def unlucky_1(nums):
    length = len(nums)
    matches = [i for i, x in enumerate(nums[:-1]) if x == 1 and nums[i+1] == 3 and i in {0, 1, length-1, length-2}]
    return len(matches) > 0

# Given 2 int arrays, a and b, return a new array length 2 containing, as much as will fit, the elements from a followed by the elements 
# from b. The arrays may be any length, including 0, but there will be 2 or more elements available between the 2 arrays.
def make_2(a, b):
    return (a + b)[:2]

# Given 2 int arrays, a and b, of any length, return a new array with the first element of each array. If either array is length 0, ignore that 
# array.
def front_1_1(a, b):
    return a[:1] + b[:1]
