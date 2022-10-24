def not_string(str):
    result = "not " + str
    if len(str) >= 3 and str[0:3] == "not" :
        result = str
    return result

# Test code
assert not_string("candy") == "not candy"
assert not_string("x") == "not x"
assert not_string("not bad") == "not bad"
assert not_string("bad") == "not bad"
assert not_string("not") == "not"
assert not_string("is not") == "not is not"
assert not_string("no") == "not no"