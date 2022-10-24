def near_hundred(n):
    return abs(n - 100) <= 10 or abs(n - 200) <= 10


# Test code
assert near_hundred(93)   == True
assert near_hundred(90)   == True
assert near_hundred(89)   == False
assert near_hundred(110)  == True
assert near_hundred(111)  == False
assert near_hundred(121)  == False
assert near_hundred(-101) == False
assert near_hundred(-209) == False
assert near_hundred(190)  == True
assert near_hundred(209)  == True
assert near_hundred(0)    == False
assert near_hundred(5)    == False
assert near_hundred(-50)  == False
assert near_hundred(191)  == True
assert near_hundred(189)  == False
assert near_hundred(200)  == True
assert near_hundred(210)  == True
assert near_hundred(211)  == False
assert near_hundred(290)  == False