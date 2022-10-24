def makes_10(a, b):
    return a == 10 or b == 10 or a + b == 10

# Test code
assert makes_10(9, 10) == True
assert makes_10(9, 9) == False
assert makes_10(1, 9) == True
assert makes_10(10, 1) == True
assert makes_10(10, 10) == True
assert makes_10(8, 2) == True
assert makes_10(8, 3) == False
assert makes_10(10, 42) == True
assert makes_10(12, -2) == True