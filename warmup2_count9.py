# Given an array of ints, return the number of 9's in the array.


# array_count9([1, 2, 9]) → 1
# array_count9([1, 9, 9]) → 2
# array_count9([1, 9, 9, 3, 9]) → 3

def array_count9(nums):
  c=0
  for  i in nums:
    if i==9:
      c=c+1
  return c