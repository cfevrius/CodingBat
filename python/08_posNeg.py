def pos_neg(a, b, negative):
    result = (a * b) < 0;
    if negative:
        result = (a < 0 and b < 0)
    return result

# Test code
assert pos_neg(1, -1, False) == True
assert pos_neg(-1, 1, False) == True
assert pos_neg(-4, -5, True) == True
assert pos_neg(-4, -5, False) == False
assert pos_neg(-4, 5, False) == True
assert pos_neg(-4, 5, True) == False
assert pos_neg(1, 1, False) == False
assert pos_neg(-1, -1, False) == False
assert pos_neg(1, -1, True) == False
assert pos_neg(-1, 1, True) == False
assert pos_neg(1, 1, True) == False
assert pos_neg(-1, -1, True) == True
assert pos_neg(5, -5, False) == True
assert pos_neg(-6, 6, False) == True
assert pos_neg(-5, -6, False) == False
assert pos_neg(-2, -1, False) == False
assert pos_neg(1, 2, False) == False
assert pos_neg(-5, 6, True) == False
assert pos_neg(-5, -5, True) == True