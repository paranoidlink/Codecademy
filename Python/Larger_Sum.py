#Write your function here
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0

  for i in lst1:
    sum1 += i
  for x in lst2:
    sum2 += x
  if sum1 >= sum2:
    return lst1
  return lst2

#Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))