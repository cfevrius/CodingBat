# Given an array of scores, return true if each score is equal or greater than the one before. 
# The array will be length 2 or more.
def scores_increasing(scores):
    return scores == sorted(scores)

# Given an array of scores, return true if there are scores of 100 next to each other in the array. 
# The array length will be at least 2.
def scores_100(scores):
    index_of_consecutive_100s = [i for i, v in enumerate(scores[:-1]) if v == 100 and scores[i + 1] == 100]
    return len(index_of_consecutive_100s) > 0

# Given an array of scores sorted in increasing order, return true if the array contains 3 
# adjacent scores that differ from each other by at most 2, such as with {3, 4, 5} or 
# {3, 5, 5}.
def scores_clump(scores):
    three_differ_by_at_most_2 = lambda a, b, c: abs(a - b) <= 2 and abs(a - c) <= 2 and abs(b - c) <= 2
    indicies_of_matches = [i for i, _ in enumerate(scores[:-2]) 
                           if three_differ_by_at_most_2(scores[i], scores[i+1], scores[i+2])]
    return len(indicies_of_matches) >  0

# Given an array of scores, compute the int average of the first half and the second half, 
# and return whichever is larger. We'll say that the second half begins at index length/2. 
# The array length will be at least 2. To practice decomposition, write a separate helper 
# method int average(int[] scores, int start, int end) { which computes the average of the 
# elements between indexes start..end. Call your helper method twice to implement 
# scoresAverage(). Write your helper method after your scores_average() method in the JavaBat 
# text area. Normally you would compute averages with doubles, but here we use ints so the 
# expected results are exact.
def scores_average(scores):
    average = lambda scores: sum(scores) / len(scores)
    mid = len(scores) // 2 
    return max(average(scores[:mid]), average(scores[mid:]))

# Given an array of strings, return the count of the number of strings with the given length.
def words_count(words, length):
    words_of_length = [word for word in words if len(word) == length]
    return len(words_of_length)

# Given an array of strings, return a new array containing the first N strings. N will be in 
# the range 1..length.
def words_front(words, n):
    return words[:n]

# Given an array of strings, return a new List (e.g. an ArrayList) where all the strings of the 
# given length are omitted. See wordsWithout() below which is more difficult because it uses arrays.
def words_without_list(words, length):
    words_without = [word for word in words if len(word) != length]
    return words_without

# Given a positive int n, return true if it contains a 1 digit. Note: use % to get the rightmost 
# digit, and / to discard the rightmost digit.
def has_one(n):
    n_str = str(n)
    return '1' in n_str

# We'll say that a positive int divides itself if every digit in the number divides into the 
# number evenly. So for example 128 divides itself since 1, 2, and 8 all divide into 128 evenly. 
# We'll say that 0 does not divide into anything evenly, so no number with a 0 digit divides 
# itself. Note: use % to get the rightmost digit, and / to discard the rightmost digit.
def divides_self(n):
    n_str = str(n)
    digits = [int(n) for n in list(n_str)]
    divisible_by_digits = [n % digit == 0 if digit != 0 else False for digit in digits]
    return all(divisible_by_digits)

# Given an array of positive ints, return a new array of length "count" containing the first even 
# numbers from the original array. The original array will contain at least "count" even numbers.
def copy_evens(nums, count):
    evens = [num for num in nums if num % 2 == 0]
    return evens[:count]

# We'll say that a positive int n is "endy" if it is in the range 0..10 or 90..100 (inclusive). 
# Given an array of positive ints, return a new array of length "count" containing the first endy 
# numbers from the original array. Decompose out a separate isEndy(int n) method to test if a 
# number is endy. The original array will contain at least "count" endy numbers.
def copy_endy(nums, count):
    is_endy = lambda num: (0 <= num <= 10) or (90 <= num <= 100)
    endy_nums = [num for num in nums if is_endy(num)]
    return endy_nums[:count]

# Given 2 arrays that are the same length containing strings, compare the 1st string in one array 
# to the 1st string in the other array, the 2nd to the 2nd and so on. Count the number of times 
# that the 2 strings are non-empty and start with the same char. The strings may be any length, 
# including 0.
def match_up(a, b):
    starts_with_same_char = lambda a, b: (a and b) and a[0] == b[0]
    matches = [(a_str, b_str) for a_str, b_str in zip(a, b) if starts_with_same_char(a_str, b_str)]
    return len(matches)

# The "key" array is an array containing the correct answers to an exam, like {"a", "a", "b", "b"}.
# the "answers" array contains a student's answers, with "?" representing a question left blank. 
# The two arrays are not empty and are the same length. Return the score for this array of answers, 
# giving +4 for each correct answer, -1 for each incorrect answer, and +0 for each blank answer.
def score_up(key, answers):
    def score(correct, answer):
        if correct == answer:
            return 4
        elif answer == "?":
            return 0
        else:
            return -1
    
    scores = [score(correct, answer) for correct, answer in zip(key, answers)]
    return sum(scores)

# Given an array of strings, return a new array without the strings that are equal to the target 
# string. One approach is to count the occurrences of the target string, make a new array of the 
# correct length, and then copy over the correct strings.
def words_without(words, target):
    return [word for word in words if word != target]

# Given two arrays, A and B, of non-negative int scores. A "special" score is one which is a 
# multiple of 10, such as 40 or 90. Return the sum of largest special score in A and the largest 
# special score in B. To practice decomposition, write a separate helper method which finds the 
# largest special score in an array. Write your helper method after your scoresSpecial() method 
# in the JavaBat text area.
def scores_special(a, b):
    max_special = lambda nums: max([num for num in nums if num % 10 == 0], default=0)
    return max_special(a) + max_special(b)

# We have an array of heights, representing the altitude along a walking trail. Given start/end 
# indexes into the array, return the sum of the changes for a walk beginning at the start index 
# and ending at the end index. For example, with the heights {5, 3, 6, 7, 2} and start=2, end=4 
# yields a sum of 1 + 5 = 6. The start and end index will both be valid indexes into the array 
# with start <= end.
def sum_heights(heights, start, end):
    steps = [abs(heights[i] - heights[i+1]) 
             for i in range(start, end)]
    return sum(steps)

# (A variation on the sumHeights problem.) We have an array of heights, representing the 
# altitude along a walking trail. Given start/end indexes into the array, return the sum 
# of the changes for a walk beginning at the start index and ending at the end index, however 
# increases in height count double. For example, with the heights {5, 3, 6, 7, 2} and start=2, 
# end=4 yields a sum of 1*2 + 5 = 7. The start and end index will both be valid indexes into 
# the array with start <= end.
def sum_heights_2(heights, start, end):
    double_if_increasing = lambda num: 2 * abs(num) if num > 0 else abs(num)
    steps = [double_if_increasing(heights[i+1] - heights[i])
             for i in range(start, end)]
    return sum(steps)

# (A variation on the sumHeights problem.) We have an array of heights, representing the altitude 
# along a walking trail. Given start/end indexes into the array, return the number of "big" steps 
# for a walk starting at the start index and ending at the end index. We'll say that step is big 
# if it is 5 or more up or down. The start end end index will both be valid indexes into the array 
# with start <= end.
def big_heights(heights, start, end):
    steps = [abs(heights[i] - heights[i+1])
             for i in range(start, end)]
    big_steps = [step for step in steps if step >= 5]
    return len(big_steps)

# We have data for two users, A and B, each with a String name and an int id. The goal is to order 
# the users such as for sorting. Return -1 if A comes before B, 1 if A comes after B, and 0 if they 
# are the same. Order first by the string names, and then by the id numbers if the names are the same. 
# Note: with Strings str1.compareTo(str2) returns an int value which is negative/0/positive to indicate 
# how str1 is ordered to str2 (the value is not limited to -1/0/1). (On the AP, there would be two User 
# objects, but here the code simply takes the two strings and two ints directly. The code logic is the
#  same.)
def user_compare(a_name, a_id, b_name, b_id):
    def compare(a, b):
        if a == b:
            return 0
        elif a < b:
            return -1
        else:
            return 1
    if a_name == b_name:
        return compare(a_id, b_id)
    else:
        return compare(a_name, b_name)

# Start with two arrays of strings, A and B, each with its elements in alphabetical order and 
# without duplicates. Return a new array containing the first N elements from the two arrays. 
# The result array should be in alphabetical order and without duplicates. A and B will both 
# have a length which is N or more. The best "linear" solution makes a single pass over A and B, 
# taking advantage of the fact that they are in alphabetical order, copying elements directly to 
# the new array.
def merge_two(a, b, n):
    return sorted(set(a + b))[:n]

# Start with two arrays of strings, a and b, each in alphabetical order, possibly with duplicates. 
# Return the count of the number of strings which appear in both arrays. The best "linear" solution 
# makes a single pass over both arrays, taking advantage of the fact that they are in alphabetical order.
def common_two(a, b):
    return len(set(a).intersection(set(b)))