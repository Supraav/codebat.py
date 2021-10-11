# Given a string, return a new string where "not " has been added to the front. 
# However, if the string already begins with "not", return the string unchanged.


# not_string('candy') → 'not candy'
# not_string('x') → 'not x'
# not_string('not bad') → 'not bad'


def missing_char(str, n):
    front = str[:n]
    return front


s=missing_char('kitten',0)
print(s)