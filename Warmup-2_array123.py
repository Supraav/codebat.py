
# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.


# array123([1, 1, 2, 3, 1]) → True
# array123([1, 1, 2, 4, 1]) → False
# array123([1, 1, 2, 1, 2, 3]) → True

def array123(nums):
  a=len(nums)
  for i in range(0,a-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False


