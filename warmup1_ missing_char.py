# Given a non-empty string and an int n, return a new string where the char at index n has been removed. 
# The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).


# missing_char('kitten', 1) → 'ktten'
# missing_char('kitten', 0) → 'itten'
# missing_char('kitten', 4) → 'kittn'


def missing_char(str, n):
  a=""
  a=str[0:n]+str[n+1:]
  return a
  
  
  
  
  #EXPLANATION::

  
  #kitten -> 012345
   #for ('kitten',4)

    # str[0:n] =(0:4) which gives 0 to 3 i.e kitt
    # str[n+1:] = (5:) which is 5th till end

    # on concatinating:   str[0:n]+str[n+1:], we get : kittn  which is 0 to 3 and 5th till end so 4 is removed
