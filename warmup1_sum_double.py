# Given two int values, return their sum. Unless the two values are the same, then return double their sum.


# sum_double(1, 2) → 3
# sum_double(3, 2) → 5
# sum_double(2, 2) → 8

a=int(input("1st"))
b=int(input("2nd"))
def sum_double(a, b):
  s=a+b
  if(a==b):
    s=s*2
  return s

print(sum_double(a,b))