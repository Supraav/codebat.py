# Given a string, return a new string where "not " has been added to the front. 
# However, if the string already begins with "not", return the string unchanged.


# not_string('candy') → 'not candy'
# not_string('x') → 'not x'
# not_string('not bad') → 'not bad'


def not_string(str):
  s=str.split()        #splits 'not candy' into list as ['not','candy] i.e [s[0],s[1]]
  if s[0]!='not':
    return "not "+str
  else:
    return str


