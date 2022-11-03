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