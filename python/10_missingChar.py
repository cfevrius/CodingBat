''' 
Given a string 'str' and integer 'n', return a new string with
the character at index 'n' has been removed.
'''
def missing_char(str, n):
    return str[0:n] + str[n+1:]


# Test code
assert missing_char('kitten', 1) == 'ktten'
assert missing_char('kitten', 0) == 'itten'
assert missing_char('kitten', 4) == 'kittn'
assert missing_char('Hi', 0) == 'i'
assert missing_char('Hi', 1) == 'H'
assert missing_char('code', 0) == 'ode'
assert missing_char('code', 1) == 'cde'
assert missing_char('code', 2) == 'coe'
assert missing_char('code', 3) == 'cod'
assert missing_char('chocolate', 8) == 'chocolat'