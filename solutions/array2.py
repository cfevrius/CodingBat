# Return the number of even ints in the given array. Note: the % "mod" operator computes the 
# remainder, e.g. 5 % 2 is 1.
def count_evens(nums):
    return None

# Given an array length 1 or more of ints, return the difference between the largest and 
# smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) methods 
# return the smaller or larger of two values.
def big_diff(nums):
    return None

# Return the "centered" average of an array of ints, which we'll say is the mean average of 
# the values, except ignoring the largest and smallest values in the array. If there are multiple 
# copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int 
# division to produce the final average. You may assume that the array is length 3 or more.
def centered_average(nums):
    return None

# Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 
# 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do 
# not count.
def sum_13(nums):
    return None

# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 
# and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
def sum_67(nums):
    return None

# Given an array of ints, return true if the array contains a 2 next to a 2 somewhere.
def has_22(nums):
    return None

# Given an array of ints, return true if the array contains no 1's and no 3's.
def lucky_13(nums):
    return None

# Given an array of ints, return true if the sum of all the 2's in the array is exactly 8.
def sum_28(nums):
    return None

# Given an array of ints, return true if the number of 1's is greater than the number of 4's
def more_14(nums):
    return None

# Given a number n, create and return a new int array of length n, containing the numbers 0, 1, 
# 2, ... n-1. The given n may be 0, in which case just return a length 0 array. You do not need 
# a separate if-statement for the length-0 case; the for-loop should naturally execute 0 times in 
# that case, so it just works. The syntax to make a new int array is: desirec_length * [] or 
# list(range(desired_length))
def fizz_array(n):
    return None

# Given an array of ints, return true if every element is a 1 or a 4.
def only_14(nums):
    return None

# Given a number n, create and return a new string list of length n, containing the strings "0", 
# "1" "2" .. through n-1. N may be 0, in which case just return a length 0 array. Note: str(xxx) 
# will make the String form of most types. The syntax to make a new string list is: 
# desired_length * [] or list(range(desired_length))
def fizz_array_2(n):
    return None

# Given an array of ints, return true if it contains no 1's or it contains no 4's.
def no_14(nums):
    return None

# We'll say that a value is "everywhere" in an array if for every pair of adjacent elements in 
# the array, at least one of the pair is that value. Return true if the given value is everywhere 
# in the array.
def is_everywhere(nums, val):
    return None

# Given an array of ints, return true if the array contains a 2 next to a 2 or a 4 next to a 4, 
# but not both.
def either_24(nums):
    return None

# Given arrays nums1 and nums2 of the same length, for every element in nums1, consider the 
# corresponding element in nums2 (at the same index). Return the count of the number of times 
# that the two elements differ by 2 or less, but are not equal.
def match_up(nums1, nums2):
    return None

# Given an array of ints, return true if the array contains two 7's next to each other, or there 
# are two 7's separated by one element, such as with [7, 1, 7].
def has_77(nums):
    return None

# Given an array of ints, return true if there is a 1 in the array with a 2 somewhere later in 
# the array.
def has_12(nums):
    return None

# Given an array of ints, return true if the array contains either 3 even or 3 odd values all 
# next to each other.
def mod_three(nums):
    return None

# Given an array of ints, return true if the value 3 appears in the array exactly 3 times, and 
# no 3's are next to each other.
def have_three(nums):
    return None

# Given an array of ints, return true if every 2 that appears in the array is next to another 2.
def two_two(nums):
    return None

# Return true if the group of N numbers at the start and end of the array are the same. For example, 
# with [5, 6, 45, 99, 13, 5, 6], the ends are the same for n=0 and n=2, and false for n=1 and n=3. 
# You may assume that n is in the range 0..len(nums) inclusive.
def same_ends(nums, len):
    return None

# Return true if the array contains, somewhere, three increasing adjacent numbers like .... 4, 
# 5, 6, ... or 23, 24, 25.
def triple_up(nums):
    return None

# Given start and end numbers, return a new array containing the sequence of integers from start 
# up to but not including end, so start=5 and end=10 yields [5, 6, 7, 8, 9]. The end number will 
# be greater or equal to the start number. Note that a length-0 array is valid.
def fizz_array_3(start, end):
    return None

# Return an array that is "left shifted" by one -- so [6, 2, 5, 3] returns [2, 5, 3, 6]. You may 
# modify and return the given array, or return a new array.
def shift_left(nums):
    return None

# For each multiple of 10 in the given array, change all the values following it to be that multiple 
# of 10, until encountering another multiple of 10. So [2, 10, 3, 4, 20, 5] yields 
# [2, 10, 10, 10, 20, 20].
def ten_run(nums):
    return None

# Given a non-empty array of ints, return a new array containing the elements from the original 
# array that come before the first 4 in the original array. The original array will contain at 
# least one 4. Note that it is valid in Python to create an array of length 0.
def pre_4(nums):
    return None

# Given a non-empty array of ints, return a new array containing the elements from the original 
# array that come after the last 4 in the original array. The original array will contain at 
# least one 4. Note that it is valid in Python to create an array of length 0.
def post_4(nums):
    return None

# We'll say that an element in an array is "alone" if there are values before and after it, and 
# those values are different from it. Return a version of the given array where every instance 
# of the given value which is alone is replaced by whichever value to its left or right is larger.
def not_alone(nums, val): 
    return None

# Return an array that contains the exact same numbers as the given array, but rearranged so that 
# all the zeros are grouped at the start of the array. The order of the non-zero numbers does not 
# matter. So [1, 0, 0, 1] becomes [0 ,0, 1, 1]. You may modify and return the given array or make 
# a new array.
def zero_front(nums):
    return None

# Return a version of the given array where all the 10's have been removed. The remaining elements 
# should shift left towards the start of the array as needed, and the empty spaces a the end of 
# the array should be 0. So [1, 10, 10, 2] yields [1, 2, 0, 0]. You may modify and return the 
# given array or make a new array.
def without_ten(nums):
    return None

# Return a version of the given array where each zero value in the array is replaced by the 
# largest odd value to the right of the zero in the array. If there is no odd value to the 
# right of the zero, leave the zero as a zero.
def zero_max(nums):
    return None

# Return an array that contains the exact same numbers as the given array, but rearranged so 
# that all the even numbers come before all the odd numbers. Other than that, the numbers can 
# be in any order. You may modify and return the given array, or make a new array.
def even_odd(nums):
    return None

# This is slightly more difficult version of the famous FizzBuzz problem which is sometimes 
# given as a first problem for job interviews. (See also: FizzBuzz Code.) Consider the series 
# of numbers beginning at start and running up to but not including end, so for example start=1 
# and end=5 gives the series 1, 2, 3, 4. Return a new List[str] array containing the string form 
# of these numbers, except for multiples of 3, use "Fizz" instead of the number, for multiples 
# of 5 use "Buzz", and for multiples of both 3 and 5 use "FizzBuzz". In Python, str(xxx) 
# will make the string form of an int or other type. This version is a little more complicated than 
# the usual version since you have to allocate and index into an array instead of just printing, and 
# we vary the start/end instead of just always doing 1..100.
def fizz_buzz(start, end):
    return None