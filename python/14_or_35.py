'''
Return true if the given non-negative number is a multiple of 3
or a multiple of 5. Use the % "mod" operator.
'''
def or_35(n):
    return n % 3 == 0 or n % 5 == 0

assert or_35(3) == True
assert or_35(10) == True
assert or_35(8) == False
assert or_35(15) == True
assert or_35(5) == True
assert or_35(9) == True
assert or_35(4) == False
assert or_35(7) == False
assert or_35(6) == True
assert or_35(17) == False
assert or_35(18) == True
assert or_35(29) == False
assert or_35(20) == True
assert or_35(21) == True
assert or_35(22) == False
assert or_35(45) == True
assert or_35(99) == True
assert or_35(100) == True
assert or_35(101) == False
assert or_35(121) == False
assert or_35(123) == True