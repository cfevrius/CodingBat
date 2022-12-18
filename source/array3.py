# Consider the leftmost and righmost appearances of some value in an array. We'll say that the 
# "span" is the number of elements between the two inclusive. A single value has a span of 1. 
# Returns the largest span found in the given array. (Efficiency is not a priority.)
def max_span(nums):
    nums_str = ''.join(str(num) for num in nums)
    def find_span(num):
        first = nums_str.index(str(num))
        last = nums_str.rindex(str(num))
        return (last - first) + 1
    all_spans = [find_span(v) for i, v in enumerate(nums)]
    return max(all_spans) if all_spans else 0

# Return an array that contains exactly the same numbers as the given array, but rearranged so 
# that every 3 is immediately followed by a 4. Do not move the 3's, but every other number may 
# move. The array contains the same number of 3's and 4's, every 3 has a number after it that is 
# not a 3, and a 3 appears in the array before any 4.
def fix_34(nums):
    index_of_4s = [i for i, val in enumerate(nums) if val == 4]

    def swap(index1, index2):
        nums[index1], nums[index2] = nums[index2], nums[index1]

    for index in index_of_4s:
        if nums[index - 1] != 3:
            available_3s = [i 
                            for i, val in enumerate(nums) 
                            if val == 3 and nums[i+1] != 4]
            if available_3s:
                swap(index, available_3s[0] + 1)
    return nums

# (This is a slightly harder version of the fix34 problem.) Return an array that contains exactly 
# the same numbers as the given array, but rearranged so that every 4 is immediately followed by 
# a 5. Do not move the 4's, but every other number may move. The array contains the same number 
# of 4's and 5's, and every 4 has a number after it that is not a 4. In this version, 5's may 
# appear anywhere in the original array.
def fix_45(nums):
    index_of_5s = [i for i, val in enumerate(nums) if val == 5]

    def swap(index1, index2):
        nums[index1], nums[index2] = nums[index2], nums[index1]
    
    for index in index_of_5s:
        if nums[index - 1] != 4:
            available_4s = [i 
                            for i, val in enumerate(nums) 
                            if val == 4 and nums[i + 1] != 5]
            if available_4s:
                swap(index, available_4s[0] + 1)
    return nums

# Given a non-empty array, return true if there is a place to split the array so that the sum of 
# the numbers on one side is equal to the sum of the numbers on the other side.
def can_balance(nums):
    are_sums_balanced = [sum(nums[:i]) == sum(nums[i:])
                         for i in range(1, len(nums))]
    return any(are_sums_balanced)

# Given two arrays of ints sorted in increasing order, outer and inner, return true if all of the 
# numbers in inner appear in outer. The best solution makes only a single "linear" pass of both 
# arrays, taking advantage of the fact that both arrays are already in sorted order.
def linear_in(outer, inner):
    return set(inner).issubset(set(outer))

# Given n>=0, create an array length n*n with the following pattern, shown here for n=3 : 
# {0, 0, 1,    0, 2, 1,    3, 2, 1} (spaces added to show the 3 groups).
def square_up(n):
    def create_group(num, group_size):
        zeroes = [0] * (group_size - num)
        nums   = range(1, num + 1)
        return zeroes + list(reversed(nums))
    group_of_groups = [create_group(i , n) for i in range(1, n+1)]
    flattened_groups = [item for group in group_of_groups for item in group]
    return flattened_groups

# Given n>=0, create an array with the pattern {1,    1, 2,    1, 2, 3,   ... 1, 2, 3 .. n} 
# (spaces added to show the grouping). Note that the length of the array will be 
# 1 + 2 + 3 ... + n, which is known to sum to exactly n*(n + 1)/2.
def series_up(n):
    nested_series = [list(range(1,i+1))  for i in range(1, n+1)]
    flattened_series = [num for series in nested_series for num in series]
    return flattened_series

# We'll say that a "mirror" section in an array is a group of contiguous elements such that 
# somewhere in the array, the same group appears in reverse order. For example, the largest 
# mirror section in {1, 2, 3, 8, 9, 3, 2, 1} is length 3 (the {1, 2, 3} part). Return the size 
# of the largest mirror section found in the given array.
def max_mirror(nums):
    all_contiguous_at_index = lambda index: [nums[index:index+i] 
                                             for i in range(1, len(nums) - index + 1)]                                            
    '''
    nums = [1, 2, 3]
    all_contiguous_at_index(0) => [[1], [1, 2], [1, 2, 3]]
    all_contiguous_at_index(1) => [[2], [2, 3]]
    all_contiguous_at_index(2) => [[3]]
    '''
    list_to_str = lambda list: ''.join(str(num) for num in list)
    is_sublist_in_list = lambda sublist: list_to_str(sublist) in list_to_str(nums)
    len_of_all_mirrors = [len(sequence) if is_sublist_in_list(reversed(sequence)) else 0
                          for i,_ in enumerate(nums)
                          for sequence in all_contiguous_at_index(i)]
    return max(len_of_all_mirrors, default=0)

# Say that a "clump" in an array is a series of 2 or more adjacent elements of the same value. 
# Return the number of clumps in the given array.
def count_clumps(nums):
    state = 'no clump'
    prev_num = None
    num_clump = 0
    for num in nums:
        if state == 'no clump':
            if prev_num is not None and num == prev_num:
                state = 'clump'
                num_clump += 1
        elif state == 'clump':
            if num != prev_num:
                state = 'no clump'
        prev_num = num
    return num_clump