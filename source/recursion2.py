# Given an array of ints, is it possible to choose a group of some of the ints, such that 
# the group sums to the given target? This is a classic backtracking recursion problem. 
# Once you understand the recursive backtracking strategy in this problem, you can use the 
# same pattern for many problems to search a space of choices. Rather than looking at the 
# whole array, our convention is to consider the part of the array starting at index start 
# and continuing to the end of the array. The caller can specify the whole array simply by 
# passing start as 0. No loops are needed -- the recursive calls progress down the array. 
def group_sum(start, nums, target):
    if start >= len(nums):
        return target == 0
    else:
        return group_sum(start + 1, nums, target - nums[start]) or \
               group_sum(start + 1, nums, target)

# Given an array of ints, is it possible to choose a group of some of the ints, beginning at 
# the start index, such that the group sums to the given target? However, with the additional 
# constraint that all 6's must be chosen. (No loops needed.)
def group_sum_6(start, nums, target):
    if start >= len(nums):
        return target == 0
    else:
        if nums[start] == 6:
            return group_sum_6(start + 1, nums, target - 6)
        else:
            return group_sum_6(start + 1, nums, target - nums[start]) or \
                   group_sum_6(start + 1, nums, target)

# Given an array of ints, is it possible to choose a group of some of the ints, such that the 
# group sums to the given target with this additional constraint: If a value in the array is 
# chosen to be in the group, the value immediately following it in the array must not be chosen. 
# (No loops needed.)
def group_no_adj(start, nums, target):
    if start >= len(nums):
        return target == 0
    else:
        return group_no_adj(start + 2, nums, target - nums[start]) or \
               group_no_adj(start + 1, nums, target)

# Given an array of ints, is it possible to choose a group of some of the ints, such that the 
# group sums to the given target with these additional constraints: all multiples of 5 in the 
# array must be included in the group. If the value immediately following a multiple of 5 is 1, 
# it must not be chosen. (No loops needed.)
def group_sum_5(start, nums, target):
    if start >= len(nums):
        return target == 0
    elif nums[start] % 5 == 0:
        if (start + 1) < len(nums) and nums[start + 1] == 1:
            return group_sum_5(start + 2, nums, target - nums[start])
        else:
            return group_sum_5(start + 1, nums, target - nums[start])
    else:
        return group_sum_5(start + 1, nums, target - nums[start]) or \
                group_sum_5(start + 1, nums, target)

# Given an array of ints, is it possible to choose a group of some of the ints, such that the 
# group sums to the given target, with this additional constraint: if there are numbers in the 
# array that are adjacent and the identical value, they must either all be chosen, or none of 
# them chosen. For example, with the array [1, 2, 2, 2, 5, 2], either all three 2's in the 
# middle must be chosen or not, all as a group. (one loop can be used to find the extent of the 
# identical values).
def group_sum_clump(start, nums, target):
    def find_clump_size(nums, start):
        clump_size = 0
        index = start
        while 0 <= index <= len(nums) - 1 and nums[index] == nums[start]:
            clump_size += 1
            index += 1
        return clump_size
    if start >= len(nums):
        return target == 0
    else:
        clump_size = find_clump_size(nums, start)
        return group_sum_clump(start + clump_size, nums, target - (clump_size * nums[start])) or \
               group_sum_clump(start + clump_size, nums, target)

# Given an array of ints, is it possible to divide the ints into two groups, so that the sums 
# of the two groups are the same. Every int must be in one group or the other. Write a recursive 
# helper method that takes whatever arguments you like, and make the initial call to your recursive 
# helper from split_array(). (No loops needed.)
def split_array(nums):
    def split_array_r(nums, index, first_group_total, second_group_total):
        if index >= len(nums):
            return first_group_total == second_group_total
        else:
            return split_array_r(nums, index + 1, first_group_total + nums[index], second_group_total) or \
                   split_array_r(nums, index + 1, first_group_total, second_group_total + nums[index])
    return split_array_r(nums, 0, 0, 0)

# Given an array of ints, is it possible to divide the ints into two groups, so that the sum of 
# one group is a multiple of 10, and the sum of the other group is odd. Every int must be in one 
# group or the other. Write a recursive helper method that takes whatever arguments you like, 
# and make the initial call to your recursive helper from splitOdd10(). (No loops needed.)
def split_odd_10(nums):
    is_odd_10 = lambda a, b: a % 10 == 0 and b % 2 == 1 or \
                              b % 10 == 0 and a % 2 == 1
    def split_odd_10_r(nums, index, first_group_total, second_group_total):
        if index >= len(nums):
            return is_odd_10(first_group_total, second_group_total)
        else:
            return split_odd_10_r(nums, index + 1, first_group_total + nums[index], second_group_total) or \
                   split_odd_10_r(nums, index + 1, first_group_total, second_group_total + nums[index])
    return split_odd_10_r(nums, 0, 0, 0)

# Given an array of ints, is it possible to divide the ints into two groups, so that the sum 
# of the two groups is the same, with these constraints: all the values that are multiple of 
# 5 must be in one group, and all the values that are a multiple of 3 (and not a multiple of 
# 5) must be in the other. (No loops needed.)
def split_53(nums):
    def split_53_r(nums, index, mults_of_5, mults_of_3):
        if index >= len(nums):
            return mults_of_5 == mults_of_3
        elif nums[index] % 5 == 0:
            return split_53_r(nums, index + 1, mults_of_5 + nums[index], mults_of_3)
        elif nums[index] % 3 == 0:
            return split_53_r(nums, index + 1, mults_of_5, mults_of_3 + nums[index])
        else:
            return split_53_r(nums, index + 1, mults_of_5 + nums[index], mults_of_3) or \
                   split_53_r(nums, index + 1, mults_of_5, mults_of_3 + nums[index])
    return split_53_r(nums, 0, 0, 0)
